import socket


# Parent class for Client and Server
class Connection(object):
    def __init__(self, ip="", port=0):
        # Construct the object
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.transmitionTerminator = "/0/"
        
    # Sends data to the port using given interface
    def send(self, interface, msg=""):
        # Make sure msg is written
        if not msg:
            return False
        
        # Appends transmission terminator
        msg += "/0/"

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
            ## Loops through and ensures transmission is complete
            data = ""
            while data[-3:] != self.transmitionTerminator:
                data += str(interface.recv(1024).decode("ascii"))
            
            return data[:-3]

        except Exception as e:
            # Throws error and returns false if exception is raised
            print(e)
            return False

    # Closes the open connection
    def close(self, interface):
        return interface.close()