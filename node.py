"""

Brenda Silva Machado - 2023.2

node.py contains the class Node, which is used to create the nodes of the tree.

"""

class Node:

    def __init__(self, id, request_q):

        self.id = id
        self.using = False
        self.asked = False
        self.holder = None
        self.request_q = request_q
        
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
    
    def make_request(self):
        if self.holder != self and (not self.request_q.empty()) and (not self.asked):
            self.asked = True
            self.request_q.put(self)

            print("Node " + str(self.id) + " made a request.")

    def assign_privilege(self):
        if self.holder == self and (not self.using) and (not self.request_q.empty()):
            self.holder = self.request_q.get()
            self.asked = False
            
            if self.holder == self:
                self.using = True

                """
                Enters the critical section.
                """
            else:
                self.holder.assign_privilege()

        print("Node " + str(self.holder.get_id()) + " get the token.")