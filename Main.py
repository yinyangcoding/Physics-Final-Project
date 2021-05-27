from packages.networking.Connection import Connection
from packages.networking.Server import Server
from packages.networking.Client import Client
from packages.cipher import *

import threading
import time

PORT = 1322
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


# Send unciphered
server.send(MESSAGE)
print(client.receive(True))

print()
print()
# Receive
server.send(MESSAGE, True)
print(client.receive(True))

# Close connection
client.close()
server.close()
