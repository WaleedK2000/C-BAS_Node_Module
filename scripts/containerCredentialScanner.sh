#!/bin/bash



# Define the filename to search for

filename="creds.txt"



# Create a directory on the host system if it doesn't exist

if [ ! -d "/tmp/dockerfile-creds" ]; then

    mkdir /tmp/dockerfile-creds

fi



# Change to the directory where the credentials file will be created

cd /tmp/dockerfile-creds



# Create a credentials file

echo 'password123' > "$filename"



# Get a list of all running container IDs

container_ids=$(docker ps -q)



# Loop over each container ID

for id in $container_ids; do

    # Get the container image name

    image_name=$(docker inspect --format '{{.Config.Image}}' $id)



    # Run the find command within the container

    if docker exec $id sh -c "find / -name '$filename'" >/dev/null 2>&1; then

        echo "Found $filename in container $id ($image_name)"

        echo "Contents of $filename:"

        docker exec $id cat $(docker exec $id sh -c "find / -name '$filename'")

    fi

done

