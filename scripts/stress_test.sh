#!/bin/bash

docker run --rm -it ubuntu sh -c 'apt-get update && apt-get install stress -y && stress --vm 2 --vm-bytes 2G --timeout 30'

