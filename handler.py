"""

Brenda Silva Machado - 2023.2

handler.py contains the class Handler, which is used to handle the requests from the nodes.

"""

import queue

class Handler:
    def __init__(self):
        self.request_q = queue.Queue()

    def get_request_q(self):
        return self.request_q
    
    def handle_request(self, node):
        self.request_q.put(node)

        print("Request from node " + str(node.get_id()) + " received.")
    
    def delete_request(self, node):
        self.request_q.get(node)
    
    def assign_privilege(self, node):
        self.delete_request(node)
        node.set_using(True)
        node.set_asked(False)

        print("Node " + str(node.get_id()) + " get the token.")
        


    
