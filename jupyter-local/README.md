# Run Jupyter locally without environment/package management!
Containers come prepackaged with dependencies, making it much easier to spin up a dev environment.
* [Core Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html)
* [Docker Hub Jupyter Project](https://hub.docker.com/u/jupyter)

You can use `jupyter-local-tensorflow-compose.yml` as a template to create a docker compose file using any of Jupyter Project's dockerhub images.

## Example
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