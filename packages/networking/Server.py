import socket
from .Connection import Connection

class Server(Connection):
    def __init__(self, ip="", port=0):
        # Construct using superclass
        super().__init__(ip, port)
    
    # Binds to the given port
    def bind(self):
        # Binds to the port
        self.sock.bind((self.ip, self.port))

        # Allows given number of connections
        self.sock.listen(2)

        # Grabs connected addresses and new connection interface
        self.conn, self.addr = self.sock.accept()
    
    # Calls superclass send with interface
    def send(self, msg=""):
        return super().send(self.conn, msg)

    # Calls superclass receive with interface
    def receive(self):
        return super().receive(self.conn)

    # Closes the open connection by calling super
    def close(self):
        return super().close(self.conn)
