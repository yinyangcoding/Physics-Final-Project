import socket

class Connection(object):
    def __init__(self, ip="", port=0):
        self.ip = ip
        self.port = port
