from packages.Connection import Connection


test = Connection("127.0.0.1", 12)

print("{}:{}".format(test.ip, test.port))
