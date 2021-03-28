import socket
import termcolor

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print("OK")

    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))
            print("SERVER IS UP")
            s.close()
        except ConnectionRefusedError:
            print("Could not connect to the server.")

    def __str__(self):
        return "Connection to SERVER at " + self.ip + ", PORT: " + str(self.port)

    def talk(self, msg):
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))
        # Send data.
        print("To server: ", msg)
        s.send(str.encode(msg))
        # Receive data
        response = s.recv(2048).decode("utf-8")
        # Close the socket
        s.close()
        # Return the response
        return "From server: " + response

    def debug_talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        message=("To server: ", msg)
        termcolor.cprint(message, "blue")
        s.send(str.encode(msg))
        response = s.recv(2048).decode("utf-8")
        s.close()
        resp=("From server: " + response)
        termcolor.cprint(resp, "yellow")




