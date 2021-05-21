import socket

class Connection(object):
    def __init__(self, ip="", port=0):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    
    def send(self, interface, msg=""):
        if not msg:
            return False

        try:
            return interface.sendall(msg.encode())
        except Exception as e:
            print(e)
            return False

    def receive(self, interface):
        try:
            return str(interface.recv(1024).decode("ascii"))

        except Exception as e:
            print(e)
            return False