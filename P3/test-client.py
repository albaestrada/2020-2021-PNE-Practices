from Client0 import Client

IP = "127.0.0.1"
PORT = 8080

print("-----| Practice 3, Exercise 7 |------")

c = Client(IP, PORT)
print(c)

print("* Testing PING...")
response = c.talk("PING")
print(response)

print("* Testing GET...")
seq0 = c.talk("GET 0")
print("GET 0", seq0)
seq1 = c.talk("GET 1")
print("GET 1", seq1)
seq2 = c.talk("GET 2")
print("GET 2", seq2)
seq3 = c.talk("GET 3")
print("GET 3", seq3)
seq4 = c.talk("GET 4")
print("GET 4", seq4)

print()

print("* Testing INFO...")
response = c.talk(f"INFO {seq0}")
print(response)

print("* Testing COMP...")
print(f"COMP {seq0}")
response = c.talk("COMP", seq0)
print(response)

print("* Testing REV...")
print("REV", seq0)
response = c.talk("REV", seq0)
print(response)

print("* Testing GENE...")
print("GENE U5")
response = c.talk("GENE U5")
print(response)

print()

print("GENE ADA")
response = c.talk("GENE ADA")
print(response)

print()

print("GENE FRAT1")
response = c.talk("GENE FRAT1")
print(response)

print()

print("GENE FXN")
response = c.talk("GENE FXN")
print(response)

print()

print("GENE RNU6_269P")
response = c.talk("GENE RNU6_269P")
print(response)

print()