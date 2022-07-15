import json

from dejavu import Dejavu
from dejavu.logic.recognizer.file_recognizer import FileRecognizer
from time import time
import os

# load config from a JSON file (or anything outputting a python dictionary)
config = {
    "database": {
        "host": "db",
        "user": "postgres",
        "password": "password",
        "database": "dejavu"
    },
    "database_type": "postgres"
}

if __name__ == '__main__':

    # create a Dejavu instance
    djv = Dejavu(config)

    # Fingerprint all the mp3's in the directory we give it

    a = time()
    djv.fingerprint_directory("test", [".mp3"])

    # Recognize audio from a file
    b = time()
    results = djv.recognize(FileRecognizer, "mp3/tanda_3.mp3")
    print(f'Tiempo de identificacion: {time() - b} seg')

    return_vector = [[x, 0] for x in os.listdir('test')]

    for i in results['results']:
        if float(i['fingerprinted_confidence']) > 0.5:
            for j in range(len(return_vector)):

                if return_vector[j][0] == f'{i["song_name"].decode()}.mp3':
                    return_vector[j] = [i['song_name'].decode(), 1]
                    print(f'Se identifico: {i["song_name"].decode()}')

    print(return_vector)