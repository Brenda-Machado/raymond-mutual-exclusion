"""

Brenda Silva Machado - 2023.2

server.py contains the methods that keep and update the database.

"""

import socket
import json
from lib.node import Node

"""

Creates the server socket.

"""

HOST = "127.0.0.1"  
PORT = 65432  

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))


"""

Loads the database.

"""

database = json.load(open("app/database.json"))


"""

Method main() is used to receive commands from the client.

"""

def main():
    
    server.listen()
    print("Server is listening...")

    while True:
        conn, addr = server.accept()

        print("Connected by", addr)

        while True:
            data = conn.recv(1024)
            if not data:
                break

            data = data.decode("utf-8")
            data = data.split(" ")

            if data[0] == "get":
                value = get(data[1])

                # mandar o valor pro cliente


            elif data[0] == "set":

                """

                Critical section

                """

                set(data[1], data[2])
            
            elif data[0] == "exit":
                server.sendall("-1".encode("utf-8"))

                exit()

            elif data[0] == "help":

                print("Commands:")
                print("get <key> - returns the value of the key")
                print("set <key> <value> - sets the value of the key")
                print("exit - exits the program")
        

        conn.close()

"""

Method get() returns the value of the key.

"""

def get(key):

    if key not in database:
        return "Key not found."
        
    else:
        return database[key]


"""
Method set() sets the value of the key.

"""

def set(key, value):

    database[key] = value

    json.dump(database, open("app/database.json", "w"))


set("a", "b")

print(database)

print(get("a"))