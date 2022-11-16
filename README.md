# stacks: boilerplates for local development.


| stack | status |
| ----------- | ----------- |
| aws-local  | ![airflow-local-status](https://img.shields.io/static/v1?label=status&message=dev&color=blueviolet) |
| airflow-local  | ![airflow-local-status](https://img.shields.io/static/v1?label=status&message=stable&color=lightgreen) |
| docker-mailserver-local | ![airflow-local-status](https://img.shields.io/static/v1?label=status&message=dev&color=blueviolet) |
| elastic-local | ![airflow-local-status](https://img.shields.io/static/v1?label=status&message=stable&color=lightgreen) |
| jupyter-local | ![airflow-local-status](https://img.shields.io/static/v1?label=status&message=finished&color=cyan) |
| kafka-local | ![airflow-local-status](https://img.shields.io/static/v1?label=status&message=stable&color=lightgreen) |
| logtsash-local | ![airflow-local-status](https://img.shields.io/static/v1?label=status&message=stable&color=lightgreen) |
| mongo-local | ![airflow-local-status](https://img.shields.io/static/v1?label=status&message=stable&color=lightgreen) |
| mysql-local | ![airflow-local-status](https://img.shields.io/static/v1?label=status&message=stable&color=lightgreen) |
| nginx-reverse-proxy-local | ![airflow-local-status](https://img.shields.io/static/v1?label=status&message=dev&color=blueviolet) |
| pentest-local | ![airflow-local-status](https://img.shields.io/static/v1?label=status&message=stable&color=lightgreen) |
| postgres-local | ![airflow-local-status](https://img.shields.io/static/v1?label=status&message=stable&color=lightgreen) |
| rabbitmq-local | ![airflow-local-status](https://img.shields.io/static/v1?label=status&message=stable&color=lightgreen) |
| rocketchat-local | ![airflow-local-status](https://img.shields.io/static/v1?label=status&message=dev&color=blueviolet) |
| snipe-it-local | ![airflow-local-status](https://img.shields.io/static/v1?label=status&message=broken&color=red) |
| traefik-reverse-proxy-local | ![airflow-local-status](https://img.shields.io/static/v1?label=status&message=dev&color=blueviolet) |


| Key |  Description|
| ----------- | ----------- |
| ![airflow-local-status](https://img.shields.io/static/v1?label=status&message=stable&color=lightgreen) | Basic boilerplate from the documentation that runs and functions correctly. |
| ![airflow-local-status](https://img.shields.io/static/v1?label=status&message=finished&color=cyan) | Additional functionality outside of the documentation or the scope of basic deployment was implemeted succcesfully. |
| ![airflow-local-status](https://img.shields.io/static/v1?label=status&message=dev&color=blueviolet) | Additional functionality or testing scripts are being implemented. Possibly stable. |
| ![broken-status](https://img.shields.io/static/v1?label=status&message=broken&color=red) | Not functioning 100% correctly, impediment remains unresolved. (create gh issue for these)|

## How to Contribute

### Adding onto an exisiting stack


### Creating a new stack
Follow the naming convention of `{STACK_NAME}-local` and try to pick a concise stack name. Make a fork and create a pull request, I'll probably merge it in within hours. 

If there's a software or service you see fit for this repository, please feel free to create a new stack for it. Don't create stacks that have licensing requirements. 

I'd love to implement services like Datadog, Databricks, Snowflake, etc.. but they don't support local development unless you have an account/license with them. I'd like to keep this repo as open-source as possible, only create stacks that allow you to develop locally without licensing requirements. (example of an exception: Localstack - some minor additional features are included with Pro. Services like this are fine.)

### Issues
Feel free to create an issue if you see anything outdated or something that doesn't follow best practices.

## Prerequisites
* These stacks are provisioned with docker compose - [Docker Compose Install Instructions](https://docs.docker.com/compose/install/).
* Windows - you must [install WSL](https://learn.microsoft.com/en-us/windows/wsl/install) (Windows Subsystem for Linux) to run Docker.
* Mac - [install instructions](https://docs.docker.com/desktop/install/mac-install/).
## Basic Docker Compose Example - Jupyter Tensorflow
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
This bind mount is referenced in your Docker Compose file `jupyter-local-tensorflow-compose.yml`:
```
services:
  jupyter-tensorflow-local:
    container_name: jupyter-tensorflow-local
    image: jupyter/tensorflow-notebook
    volumes:
      - tensorflow-notebooks:/home/jovyan/work   # <-- HERE
    ports:
      - ${TENSORFLOW_PORT}:${TENSORFLOW_PORT}
    command: bash -c "jupyter notebook --port ${TENSORFLOW_PORT} --NotebookApp.token=${ACCESS_TOKEN}"
    tty: true

volumes:
  tensorflow-notebooks:    # <-- AND HERE
    external: true         # <-- 'external: true' rather than 'driver: local' tells docker compose this is an external bind mount volume. compose does not create or delete this volume, only attatches to it. it will persist upon destruction of the compose project.
```

3. Change your `ACCESS_TOKEN` and ports in the `.env` file (`stacks/jupyter-local/.env`) if you'd like. 
```
ACCESS_TOKEN=somethingsecure
# you can change these ports and/or add other Core Stacks (https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html) using the spark/tensorflow boilerplates
TENSORFLOW_PORT=8887
SPARK_PORT=8889
```
4.  Use `docker compose -f compose-filename.yml up` and start your container in detached mode using the `-d` flag.
```
$ docker compose -f jupyter-local-tensorflow-compose.yml up -d
```
5. Open [localhost:8887](http://localhost:8887) in your browser and enter your super secret `ACCESS_TOKEN` inside of `.env` to log in.

![jupyter](https://github.com/adamsiwiec1/images/blob/main/stacks/jupyter.png?raw=true)

6. Upload a file to test your bind mount/persistant docker volume. 
![jupyter-upload](https://github.com/adamsiwiec1/images/blob/main/stacks/jupyter-upload.png?raw=true)
7. Your test file should appear on your local machine in the `LOCAL_WORKING_DIR` that you specified in the `stacks/jupyter-local/.env` file.

![jupyter-explorer](https://github.com/adamsiwiec1/images/blob/main/stacks/jupyter-explorer.png?raw=true)
8. Use `docker compose -f compose-filename.yml down`  to tear down your deployment.
```
$ docker compose -f jupyter-local-tensorflow-compose.yml down
```
`docker compose down` will tear down all the resources specified in your docker compose file; containers, networks, volumes, etc. However, since we created an external bind mount on our local system (`tensorflow-notebooks` in step 2) which we are referencing in our compose file, our data will persist next time we start our compose project. 