from rest_framework.response import Response
from rest_framework.decorators import api_view

import docker
import subprocess
import os

@api_view(['GET'])
def getData(request):

    client = docker.from_env()
    lis = client.containers.list()

    containerList = []
    

    dictContainer = {}
    if len(lis) > 0:

        for container in lis:
            dictContainer[container.name] = container.attrs


    response = {"running ": len(lis), "error": "none", "data":dictContainer }

    person = {'name': 'Dennis', 'age': 28}
    return Response(response)


@api_view(['GET'])
def executeExploit(request):

    response = {}
    
    client = docker.from_env()
    con = False
    try:
        con = client.containers.get("musing_pasteur")
    except:
        response = {"error": "No Container Found" }
        return Response(response)
    else:

        con.exec_run('apt-get update')
        con.exec_run('apt-get install docker.io -y')

        res = con.exec_run('docker ps')

        print(res.output)

        subs = 'CONTAINER ID'

        ter = str(res.output, 'UTF-8')

        print(type(ter))
        result =  subs in ter
 
        response = {"status": "Container Found",
            "RES": result,
            "m": ter
         }
        return Response(response)


@api_view(['POST'])
def executeExploit1(request):

    containerId = request.data.get('conId')
   

    response = {}
    
    client = docker.from_env()
    con = False
    try:
        con = client.containers.get(containerId)
    except:
        response = {"error": "No Container Found" }
        return Response(response)
    else:

        con.exec_run('apt-get update')
        con.exec_run('apt-get install docker.io -y')

        res = con.exec_run('docker ps')

        print(res.output)

        subs = 'CONTAINER ID'

        ter = str(res.output, 'UTF-8')

        print(type(ter))
        result =  subs in ter
 
        response = {"status": "Container Found",
            "result": result,
            "m": ter
         }
        return Response(response)

@api_view(['POST'])
def executePIDshell(request):

    pid_path = './scripts/pid.sh'

    output = subprocess.check_output(pid_path).decode()
    return Response({'message': 'Script executed successfully!', 'output': output})

    # returncode = shellscript.wait()
    
    # response = {'result': result}

    # return Response(response)


# @api_view(['POST'])
# def executePIDshell(request):
#     pid_path = './scripts/pid.sh'  # Set the path to the pid.sh file
#     os.chmod(pid_path, 0o755)  # Set the execute permission on the file
#     os.system(pid_path)  # Run the file
#     return Response({'message': 'Script executed successfully!'})
