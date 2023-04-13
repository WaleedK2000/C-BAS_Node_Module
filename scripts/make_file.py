import subprocess

# Make the escape-container.sh script executable
subprocess.run(["chmod", "+x", "make_file.sh"])

# Run the escape-container.sh script
subprocess.run(["./make_file.sh"])
