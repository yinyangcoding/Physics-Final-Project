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
print(SERVER_HEADER)
exit = server.send(MESSAGE)
print(SENT)
print(MESSAGE)

# Receive
print(CLIENT_HEADER)
print(RECEIVED)
print(client.receive())

# Send ciphered
print(SERVER_HEADER)
server.send(cipher(MESSAGE))
print(SENT)
print(BASE + MESSAGE)
print(CIPHER + cipher(MESSAGE))

# Receive
print(CLIENT_HEADER)
msg = client.receive()
print(RECEIVED)
print(BASE + msg)
print(DECIPHER + decipher(msg))

# Close connection
client.close()
server.close()
