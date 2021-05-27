from packages.networking.Connection import Connection
from packages.networking.Server import Server
from packages.networking.Client import Client
from packages.cipher import *

import threading
import time

PORT = 1337
MESSAGE = "This is a test."

SERVER_HEADER = "\n====== Server ======"
CLIENT_HEADER = "\n====== Client ======"

SENT = "\tSENT:"
RECEIVED = "\tRECV:"

BASE = "BASE:\t"
CIPHER = "CIPHERED:\t"
DECIPHER = "DECIPHERED:\t"
KEY = "KEY:\t"

server = Server("localhost", PORT)
client = Client("localhost", PORT)


# Thread the bind
bindThread = threading.Thread(target=server.bind)

# Connect server to client
bindThread.start()
client.connect()

# Let thread finish or they get mad ¯\_(ツ)_/¯
time.sleep(1)

exampleCipher = cipher(MESSAGE)
exampleCipher = "{}{}".format(exampleCipher[0], exampleCipher[1])

# Send unciphered
print(SERVER_HEADER)
print(SENT)
print("{}{}".format(BASE, MESSAGE))
server.send(MESSAGE)

print(CLIENT_HEADER)
print(RECEIVED)
print("{}{}".format(BASE, client.receive()))

# Send ciphered
print(SERVER_HEADER)
server.send(MESSAGE, True)
print(SENT)
print("{}{}".format(CIPHER, exampleCipher))
print("{}{}".format(BASE, MESSAGE))


print(CLIENT_HEADER)
print(RECEIVED)
print("{}{}".format(CIPHER, exampleCipher))
print("{}{}".format(BASE, client.receive(True)))


# Close connection
client.close()
server.close()
