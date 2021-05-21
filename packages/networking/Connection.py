import socket


# Parent class for Client and Server
class Connection(object):
    def __init__(self, ip="", port=0):
        # Construct the object
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    # Sends data to the port using given interface
    def send(self, interface, msg=""):
        # Make sure msg is written
        if not msg:
            return False

        try:
            # Return result of sending msg
            return interface.sendall(msg.encode())
        
        except Exception as e:
            # Return false if it fails
            print(e)
            return False

    # Reads outstanding data on the port
    def receive(self, interface):
        try:
            # Returns the data if successful
            return str(interface.recv(1024).decode("ascii"))

        except Exception as e:
            # Throws error and returns false if exception is raised
            print(e)
            return False