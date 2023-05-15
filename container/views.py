from rest_framework.response import Response
from rest_framework.decorators import api_view

import docker
import subprocess
import os
import re

from blue_team_scripts import main_scan


@api_view(["GET"])
def getData(request):
    client = docker.from_env()
    lis = client.containers.list()

    containerList = []

    dictContainer = {}
    if len(lis) > 0:
        for container in lis:
            dictContainer[container.name] = container.attrs

    response = {"running ": len(lis), "error": "none", "data": dictContainer}

    person = {"name": "Dennis", "age": 28}
    return Response(response)


@api_view(["GET"])
def executeExploit(request):
    response = {}

    client = docker.from_env()
    con = False
    try:
        con = client.containers.get("musing_pasteur")
    except:
        response = {"error": "No Container Found"}
        return Response(response)
    else:
        con.exec_run("apt-get update")
        con.exec_run("apt-get install docker.io -y")

        res = con.exec_run("docker ps")

        print(res.output)

        subs = "CONTAINER ID"

        ter = str(res.output, "UTF-8")

        print(type(ter))
        result = subs in ter

        response = {"status": "Container Found", "RES": result, "m": ter}
        return Response(response)


@api_view(["POST"])
def executeExploit1(request):
    containerId = request.data.get("conId")

    response = {}

    client = docker.from_env()
    con = False
    try:
        con = client.containers.get(containerId)
    except:
        response = {"error": "No Container Found"}
        return Response(response)
    else:
        con.exec_run("apt-get update")
        con.exec_run("apt-get install docker.io -y")

        res = con.exec_run("docker ps")

        print(res.output)

        subs = "CONTAINER ID"

        ter = str(res.output, "UTF-8")

        print(type(ter))
        result = subs in ter

        response = {
            "status": "Container Found",
            "execution": "200",
            "result": result,
            "output": ter,
        }
        return Response(response)


@api_view(["POST"])
def executePIDshell(request):
    pid_path = "./scripts/pid.sh"
    os.chmod(pid_path, 0o755)

    output = subprocess.check_output(pid_path).decode()
    return Response({"execution": "200", "output": output, "result": True})


@api_view(["POST"])
def executeExposeHostFp(request):
    pid_path = "./scripts/expose_host_file_path.sh"
    os.chmod(pid_path, 0o755)

    output = subprocess.check_output(pid_path).decode()
    return Response({"execution": "200", "output": output, "result": True})


@api_view(["POST"])
def executeStressTest(request):
    pid_path = "./scripts/stress_test.sh"
    os.chmod(pid_path, 0o755)

    output = subprocess.check_output(pid_path).decode()
    return Response({"execution": "200", "output": output, "result": True})


@api_view(["POST"])
def executeShowHashes(request):
    pid_path = "./scripts/show_hashes.sh"
    os.chmod(pid_path, 0o755)

    output = subprocess.check_output(pid_path).decode()
    return Response({"execution": "200", "output": output, "result": True})


@api_view(["POST"])
def executeContainerAnalysis(request):
    pid_path = "./blue_team_scripts/DockerBenchmark.sh"
    os.chmod(pid_path, 0o755)

    output = subprocess.check_output(pid_path).decode()
    return Response({"execution": "200", "output": output, "result": True})


@api_view(["POST"])
def executesharedNamespaces(request):
    pid_path = "./scripts/sharednamespace.sh"
    os.chmod(pid_path, 0o755)

    output = subprocess.check_output(pid_path).decode()
    return Response({"execution": "200", "output": output, "result": True})


# remoteCodeExecution


@api_view(["POST"])
def executeRemoteCodeExecution(request):
    pid_path = "./scripts/remoteCodeExecution.sh"
    os.chmod(pid_path, 0o755)

    output = subprocess.check_output(pid_path).decode()
    return Response({"execution": "200", "output": output, "result": True})


@api_view(["POST"])
def executeExploitingPrivilegedAccess(request):
    pid_path = "./scripts/exploitingPrivilegedAccess.sh"
    os.chmod(pid_path, 0o755)

    output = subprocess.check_output(pid_path).decode()
    return Response({"execution": "200", "output": output, "result": True})


@api_view(["POST"])
def executeContainerCredentialScanner(request):
    pid_path = "./scripts/containerCredentialScanner.sh"
    os.chmod(pid_path, 0o755)

    output = subprocess.check_output(pid_path).decode()
    return Response({"execution": "200", "output": output, "result": True})


@api_view(["POST"])
def execute(request):
    pid_path = "./scripts/sharednamespace.sh"
    os.chmod(pid_path, 0o755)

    output = subprocess.check_output(pid_path).decode()
    return Response({"execution": "200", "output": output, "result": True})


@api_view(["POST"])
def executeMakeFile(request):
    pid_path = "./scripts/make_file.sh"
    os.chmod(pid_path, 0o755)

    output = subprocess.check_output(pid_path).decode()
    return Response({"execution": "200", "output": output, "result": True})


@api_view(["POST"])
def executeDockerLog(request):
    pid_path = "./scripts/dockerLog.sh"

    containerId = request.data.get("conId")

    containerName = containerId
    os.chmod(pid_path, 0o755)

    output = subprocess.check_output(args=[pid_path, containerName]).decode("utf-8")

    # output = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    # output = output.sub('', output)

    # output = ''.join([char for char in output if ord(char)
    #                  >= 32 and ord(char) <= 126])

    lines = output.split("\n")

    return Response({"execution": "200", "output": output, "result": True})


@api_view(["POST"])
def executeDockerscan(request):
    containerId = request.data.get("conId")

    high, low_count, medium_count, high_count = main_scan.scanning(containerId)

    retJson = {
        "high": high,
        "low_count": low_count,
        "medium_count": medium_count,
        "high_count": high_count,
    }

    return Response({"execution": "200", "output": retJson, "result": True})


# @api_view(['POST'])
# def executePIDshell(request):
#     pid_path = './scripts/pid.sh'  # Set the path to the pid.sh file
#     os.chmod(pid_path, 0o755)  # Set the execute permission on the file
#     os.system(pid_path)  # Run the file
#     return Response({'message': 'Script executed successfully!'})
