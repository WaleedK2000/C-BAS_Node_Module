#!/bin/bash



# Get a list of all running Docker container IDs

container_ids=$(docker ps -q)



# Loop through each container ID and check for open ports

for id in $container_ids

do

    echo "Scanning container $id for open ports..."



    # Use Nmap to scan for open ports on the container

    open_ports=$(nmap -p- --min-rate=1000 -T4 $(docker inspect --format '{{ .NetworkSettings.IPAddress }}' $id))



    # Check if port 80 or 443 is open

    if echo "$open_ports" | grep -qE '^(80|443)/tcp'; then

        echo "Port 80 or 443 is open on container $id. Checking for RCE vulnerabilities..."



        # Use Nmap NSE to check for RCE vulnerabilities

        nmap -sV --script=http-vuln-cve2017-5638.nse $(docker inspect --format '{{ .NetworkSettings.IPAddress }}' $id)



    else

        echo "Port 80 and 443 are closed on container $id. Skipping..."

    fi

done

