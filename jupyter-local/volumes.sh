# MONGO_EXISTS=$(docker volume ls | grep mongo_data)
# PYPARSERS_EXISTS=$(docker volume ls | grep pyparsers_data)

if [ -z "$MONGO_EXISTS" ]; then
    docker volume create --driver local \
    --opt type=none \
    --opt device=/mnt/e/docker/volumes/jupyter-notebooks \
    --opt o=bind tensorflow-notebooks

fi

if [ -z "$PYPARSERS_EXISTS" ]; then
docker volume create --driver local \
    --opt type=none \
    --opt device=/mnt/e/keras \
    --opt o=bind keras
fi
