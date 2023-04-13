#!/bin/bash

# Create a Docker container with the specified configuration
docker run -d -v /:/host --name escape --privileged --cap-add=ALL --pid=host --userns=host ubuntu sleep 3600

# Execute commands in the Docker container
docker exec -it escape bash -c "echo 'Hello' > /host/hello; cd /host; ls"

