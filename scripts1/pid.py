import os

# Set the path to the pid.sh file
pid_path = "/path/to/pid.sh"

# Set the execute permission on the file
os.chmod(pid_path, 0o755)

# Run the file
os.system(pid_path)
