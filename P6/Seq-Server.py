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
    formatted_message = formatted_message.split(" ")

    if len(formatted_message) == 1:
        message = formatted_message[0]
    else:
        message = formatted_message[0]
        argument = formatted_message[1]

    if message == "PING":
        server_utils.ping(cs)
        print("OK!")

    elif message == "GET":
        n = int(formatted_message[1])
        server_utils.get(cs, n, SEQUENCES_LIST)

    elif message == "INFO":
        seq = formatted_message[1]
        server_utils.info(cs, seq)

    elif message == "COMP":
        seq = formatted_message[1]
        server_utils.comp(cs, seq)

    elif message == "REV":
        seq = formatted_message[1]
        server_utils.rev(cs, seq)

    elif message == "GENE":
        filename = f"{formatted_message[1]}.txt"
        server_utils.gene(cs, filename)






