from packages.networking.Connection import Connection
from packages.networking.Server import Server
from packages.networking.Client import Client

test = Server("127.0.0.1", 1337)

test.bind()

test.close()
