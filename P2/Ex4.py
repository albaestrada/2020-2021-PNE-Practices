from Client0 import Client

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 6123
c = Client(IP, PORT)
c.debug_talk("Message1---")
c.debug_talk("Message2: Testing!!")