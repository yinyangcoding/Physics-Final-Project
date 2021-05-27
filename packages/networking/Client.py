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
    def send(self, msg="", isCiphered=False):
        return super().send(self.sock, msg, isCiphered)
    
    # Receives data using superclass method
    def receive(self, isCiphered=False):
        return super().receive(self.sock, isCiphered)
    
    # Closes the open connection using Connection
    def close(self):
        return super().close(self.sock)
