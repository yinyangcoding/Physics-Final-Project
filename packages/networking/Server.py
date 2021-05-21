import socket
from .Connection import Connection

class Server(Connection):
    def __init__(self, ip="", port=0):
        super().__init__(ip, port)
    
    def bind(self):
        self.sock.bind((self.ip, self.port))
        self.sock.listen(2)
        self.conn, self.addr = self.sock.accept()
    

    def send(self, msg=""):
        return super().send(self.conn, msg)

    def receive(self):
        return super().receive(self.conn)

    def close(self):
        return self.conn.close()
