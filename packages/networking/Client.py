import socket
from .Connection import Connection

class Client(Connection):
    def __init__(self, ip="", port=0):
        # Calls superclass constructor
        super().__init__(ip, port)
    
    # Connects to given port
    def connect(self):
        return self.sock.connect((self.ip, self.port))
    
    # Sends data using superclass method
    def send(self, msg=""):
        return super().send(self.sock, msg)
    
    # Receives data using superclass method
    def receive(self):
        return super().receive(self.sock)