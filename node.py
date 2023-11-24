"""

Brenda Silva Machado - 2023.2

node.py contains the class Node, which is used to create the nodes of the tree.

"""

import socket

class Node:

    def __init__(self, id):

        self.id = id
        self.using = False
        self.asked = False
        self.holder = None
        
    def get_id(self):
        return self.id
    
    def get_using(self):
        return self.using
    
    def get_asked(self):
        return self.asked
    
    def get_holder(self):
        return self.holder
    
    def set_using(self, using):
        self.using = using

    def set_asked(self, asked):
        self.asked = asked
    
    def set_holder(self, holder):
        self.holder = holder
