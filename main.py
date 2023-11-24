"""

Brenda Silva Machado - 2023.2

main.py contains the class Main, which is used to run the program.

"""

import threading
import node

class Main:
    def __init__(self, nodes, request_q):
        self.nodes = nodes
        self.request_q = request_q

    