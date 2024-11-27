import subprocess

# Copy the file dz1.py to the file dz1_run.py
subprocess.run(['cp', 'dz1.py', 'dz1_run.py'])

# Append bash shebang to the beginning of dz1_run.py
with open('dz1_run.py', 'r+', newline='') as file:
    content = file.read()
    file.seek(0)
    file.write('#!/usr/bin/python3\n' + content)
    file.truncate()
# Change the permissions on the file
# Permission: Access is completely denied to everyone except the oexitwner
# The owner can read and run the file
subprocess.run(['chmod', '700', 'dz1_run.py'])

# Run dz1_run.py
subprocess.run(['./dz1_run.py'])