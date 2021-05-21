import socket
from Connection import Connection

class Client(Connection):
    def __init__(self, ip="", port=0):
        super().__init__(ip, port)
    
    def connect(self):
        return self.sock.connect((self.ip, self.port))
    
    def send(self, msg=""):
        return super().send(self.sock, msg)
    
    def receive(self):
        return super().receive(self.sock)
