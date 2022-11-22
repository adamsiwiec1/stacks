VOL1=image_name_data

DIR1_EXISTS=$(ls /opt/docker | grep -w $VOL1)

VOL1_EXISTS=$(docker volume ls | grep -w $VOL1)


if [ -z "$DIR1_EXISTS" ]; then
    echo "creating /opt/docker/$VOL1.."
    sudo mkdir -p /opt/docker/$VOL1
else
    echo "/opt/docker/$VOL1 already exists.."
fi


if [ -z "$VOL1_EXISTS" ]; then
    echo "creating $VOL1 bind mount.."
    docker volume create --driver local \
    --opt type=none \
    --opt device=/opt/docker/$VOL1/ \
    --opt o=bind $VOL1
else
    echo "$VOL1 bind mount already exists.."
fi