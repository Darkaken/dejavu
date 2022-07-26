import audioop
import json

from dejavu import Dejavu
from dejavu.logic.recognizer.file_recognizer import FileRecognizer
from time import time
import os

from pydub import AudioSegment

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

    ### PARA HACER HUELLAS DE LAS TANDAS, SOLO UNA VEZ

    directorio_tandas = "test"

    for filename in os.listdir(directorio_tandas):
        audiofile = AudioSegment.from_file(os.path.join(directorio_tandas, filename))

        quality = 44100 / (2 * audiofile.frame_rate)
        audiofile = audiofile.set_frame_rate(int(audiofile.frame_rate * quality))

        audiofile.export(os.path.join(directorio_tandas, filename), format="mp3")

    djv.fingerprint_directory(directorio_tandas, [".mp3"])

    ##############################################

    b = time()
    # Recognize audio from a file

    to_recognize = "mp3/tanda_4.mp3"

    try:
        audiofile = AudioSegment.from_file(to_recognize)

        quality = 44100 / (2 * audiofile.frame_rate)
        audiofile = audiofile.set_frame_rate(int(audiofile.frame_rate * quality))

        audiofile.export(to_recognize, format="mp3")

    except audioop.error:
        print("Error en estandarizacion de calidad")


    results = djv.recognize(FileRecognizer, to_recognize)
    print(f'Tiempo de identificacion: {time() - b} seg')

    return_vector = [[x, 0] for x in os.listdir('test')]

    for i in results['results']:
        if float(i['fingerprinted_confidence']) > 0.5:
            for j in range(len(return_vector)):

                if return_vector[j][0] == f'{i["song_name"].decode()}.mp3':
                    return_vector[j] = [i['song_name'].decode(), 1]
                    print(f'Se identifico: {i["song_name"].decode()}')

    print(return_vector)