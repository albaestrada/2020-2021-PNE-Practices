import socket
import server_utils
from Seq1 import Seq

SEQUENCES_LIST = ["AATTCCGG", "ATACGATAGCA", "ATAGACACACATGAT", "AACACACAGAGATTAGA", "ACAGATGA"]

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"


# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))
count_connections = 0
# -- Step 3: Configure the socket for listening
ls.listen()
print("The server is configured!")



client_address_list = []
while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
        client_address_list.append(client_ip_port)
        count_connections += 1
        print("CONNECTION " + str(count_connections) + ". Client IP, PORT: " + str(client_ip_port))
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    # -- Read the message from the client
    # -- The received message is in raw bytes
    msg_raw = cs.recv(2048)

    # -- We decode it for converting it
    # -- into a human-redeable string
    msg = msg_raw.decode()
    formatted_message = server_utils.format_command(msg)

    if formatted_message == "PING":
        server_utils.ping()

        # -- Send a response message to the client
        response = "OK"
        # -- The message has to be encoded into bytes
        cs.send(response.encode())
        print(response)
        cs.close()
    elif formatted_message.starswith("GET"):
        slices = msg.split(" ")
        if len(slices) == 2 and slices[0] == "GET":
            try:
                n = int(slices[1])
                if 0 <= n <= len(SEQUENCES_LIST):
                    termcolor.cprint(f"GET", 'green')
                    seq = SEQUENCES_LIST[n]
                    termcolor.cprint(f"{seq}\n", 'white')
                    cs.send(f"{seq}".encode())
                    cs.close()
            except ValueError:
                pass


    else:
        response = "NOT AVAILABLE COMMAND"
        cs.send(response.encode())
    # -- Close the data sockets
    cs.close()
