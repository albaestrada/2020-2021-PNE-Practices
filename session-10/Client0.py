import socket

import termcolor
from pip._vendor import colorama
from termcolor import colored

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
        colorama.init(strip="False")
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))
        # Send data.
        print(termcolor.colored("To Server: " + msg, "blue"))
        s.send(str.encode(msg))
        # Receive data
        response = s.recv(2048).decode("utf-8")
        print("From Server: ", end="")
        print(termcolor.colored(response, "yellow"))
        # Close the socket
        s.close()
        # Return the response
        return "From server: " + response

    def debug_talk(self, msg):
        return "From server: " + colored(self.talk(msg), "yellow")

