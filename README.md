Dejavu
==========

NOTA:
1) Todos los audios que uno quiere analizar deben ponerse en la carpeta TEST
2) Las tandas que se quieran identificar tienen que ponerse en la carpeta MP3

## Quickstart with Docker

First, install [Docker](https://docs.docker.com/get-docker/).

```shell
# build and then run our containers
$ docker-compose build #Necesario
$ docker-compose up -d #Necesario

# get a shell inside the container
$ docker-compose run python /bin/bash #Necesario

root@f9ea95ce5cea:/code# python example_docker_postgres.py  #Corre el codigo de reconocimiento
