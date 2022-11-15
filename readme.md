# stacks: boilerplates for local development.

## Status

* airflow-local
* docker-mailserver-local
* elastic-local
* jupyter-local
* d

## Prerequisites
* These stacks are provisioned with docker compose - [Docker Compose Install Instructions](https://docs.docker.com/compose/install/).
* Windows - you must [install WSL](https://learn.microsoft.com/en-us/windows/wsl/install) (Windows Subsystem for Linux) to run Docker.
* Mac - [install instructions](https://docs.docker.com/desktop/install/mac-install/).
### Example - Jupyter Tensorflow
1. Clone the repo and `cd` into the `jupyter-local` stack.
```
$ git clone https://github.com/adamsiwiec1/stacks.git
$ cd stacks/jupyter-local
```
2. Create a bind mount (persistent volume) named `tensorflow-notebooks` in a location of your preference.
```
$ docker volume create --driver local \
    --opt type=none \
    --opt device=/mnt/e/docker/volumes/jupyter-notebooks \
    --opt o=bind tensorflow-notebooks
```
3. Add your `LOCAL_WORKING_DIR` and `ACCESS_TOKEN` in the `.env` file (`stacks/jupyter-local/.env`). 
```
LOCAL_WORKING_DIR=/mnt/e/docker/volumes/jupyter-notebooks/
ACCESS_TOKEN=somethingsecure
# you can change these ports and/or add other Core Stacks (https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html) using the spark/tensorflow boilerplates
TENSORFLOW_PORT=8887
SPARK_PORT=8889
```
4.  Use Docker Compose to start your container in detached mode using the `-d` flag.
```
docker compose -f jupyter-local-tensorflow-compose.yml up -d
```
5. Open [localhost:8887](http://localhost:8887) in your browser and enter your super secret token to log in.

![jupyter](https://github.com/adamsiwiec1/images/blob/main/jupyter.png?raw=true)
