"""

Brenda Silva Machado - 2023.2

client.py contains the methods that send requests to the server.

"""

import socket

"""

Creates the client socket.

"""

HOST = "127.0.0.1"  # O hostname ou endereço IP do servidor
PORT = 65432  # A porta usada pelo servidor

client =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))


"""
Method main() is used to send commands to the server.

"""

def main():
    
    client.connect((HOST, PORT))

    while True:

        print("Commands:")
        print("get <key>")
        print("set <key> <value>")
        print("exit")
        print("help")

        data = input("Enter a command: ")
        client.sendall(data.encode("utf-8"))
        data = client.recv(1024)

        print("Received", repr(data.decode("utf-8")))

        if data.decode("utf-8") == "-1":
            break

    client.close()