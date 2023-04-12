#!/bin/bash
git clone https://github.com/docker/docker-bench-security.git
cd docker-bench-security
sh docker-bench-security.sh
cd ..
rm -rf docker-bench-security