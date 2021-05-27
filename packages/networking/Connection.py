from os import cpu_count
import socket

from .. import cipher

# Parent class for Client and Server
class Connection(object):
    def __init__(self, ip="", port=0):
        # Construct the object
        self.ip = ip
        self.port = port
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.transmitionTerminator = "/0/"
    
    # Ciphers a given message returning string
    def vi_cipher(self, msg):
        cPack = cipher.cipher(msg)

        return "{}{}".format(cPack[0], cPack[1])
    
    # Deciphers given message
    def vi_decipher(self, msg):
        cPack = (msg[:-1], int(msg[-1]))

        return cipher.decipher(cPack)

    # Sends data to the port using given interface
    def send(self, interface, msg="", isCiphered=False):
        # Make sure msg is written
        if not msg:
            return False

        # Check if they want to encrypt
        if isCiphered:
            msg = self.vi_cipher(msg)
        
        # Appends transmission terminator
        # Since msg is a tuple (or can be a tuple), that needs to be checked before appending "/0"
        # We can do msg[0] += "/0"
        msg += "/0/"

        try:
            # Return result of sending msg
            return interface.sendall(msg.encode())
        
        except Exception as e:
            # Return false if it fails
            print(e)
            return False

    # Reads outstanding data on the port
    def receive(self, interface, isCiphered=False):
        try:
            # Returns the data if successful
            ## Loops through and ensures transmission is complete
            data = ""
            while data[-1 * len(self.transmitionTerminator):] != self.transmitionTerminator:
                data += str(interface.recv(1024).decode("ascii"))
            
            # Cut terminator
            final = data[:-1 * len(self.transmitionTerminator)]

            if isCiphered:
                final = self.vi_decipher(final)

            return final

        except Exception as e:
            # Throws error and returns false if exception is raised
            print(e)
            return False

    # Closes the open connection
    def close(self, interface):
        return interface.close()