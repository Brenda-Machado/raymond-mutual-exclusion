"""

Brenda Silva Machado - 2023.2

server.py contains the methods that keep and update the database.

"""

import socket
import json
import queue
import threading
from lib.node import Node
from time import sleep

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

Creates the request queue and the nodes, where each node is a client.

"""

request_q = queue.Queue()
nodes = []

"""

Method main() is used to receive commands from the client.

"""

def main():

    server.listen(10)
    
    print("Server is listening...")

    while True:
        conn, addr = server.accept()

        print("Connected by", addr)

        if len(nodes) == 0:
            node = Node(0, request_q, None)
            node.set_holder(node)
            nodes.append(node)
            nodes[0].make_request(node)

        else:
            nodes.append(Node(len(nodes), request_q, nodes[0]))

        thread = threading.Thread(target=new_node, args=(conn, addr, len(nodes) - 1))
    
        thread.start()
    
    thread.join()

def new_node(conn, addr, id):

    while True:
        
        data = conn.recv(1024)
        data = data.decode("utf-8")
        data = data.split(" ")

        if data[0] == "get":
            value = get(data[1])
            conn.sendall(value.encode("utf-8"))

        elif data[0] == "set":

            nodes[id].make_request(nodes[id])

            """

            Critical section

            """

            while not nodes[id].get_using():
                sleep(1)

            set(data[1], data[2])

            nodes[id].exit_critical_section()


            conn.sendall("1".encode("utf-8"))
            
        elif data[0] == "exit":
            conn.sendall("-1".encode("utf-8"))

            conn.close()
            exit()


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


if __name__ == "__main__":
    main()