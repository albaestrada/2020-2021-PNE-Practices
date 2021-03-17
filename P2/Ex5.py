from Client0 import Client
from pathlib import Path

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 6123
c = Client(IP, PORT)
print(c.talk("Sending the U5 Gene to the serever..."))
print(c.talk(Path("./P2/U5.txt").read_text()))
