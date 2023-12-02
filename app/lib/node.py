"""

Brenda Silva Machado - 2023.2

node.py contains the class Node, which is used to create the nodes of the tree.

"""

class Node:

    def __init__(self, id, request_q, current_holder):

        self.id = id
        self.using = False
        self.asked = False
        self.holder = current_holder
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
    
    def make_request(self, node):
        if self.holder != self and (not node.asked):
            node.set_asked(True)
            self.holder.make_request(node)

            print("Node " + str(self.id) + " fowarded the request of node " + str(node.get_id()) + " to node " + str(self.holder.get_id()) + ".")
        
        elif self.holder == self:

            self.request_q.put(node)

            print("Node " + str(self.id) + " which holds the privilege received a request from node " + str(node.get_id()) + ".")

            self.assign_privilege()

    def assign_privilege(self):
        if self.holder == self and (not self.using) and (not self.request_q.empty()):
            self.holder = self.request_q.get()
            self.holder.set_asked(False)
            self.holder.set_using(True)

            """
            Enters the critical section.
            """

            print("Node " + str(self.id) + " entered the critical secion.")
        
        elif self.holder == self and (not self.using) and self.request_q.empty():
            self.holder = self
            self.holder.set_using(False)

            """
            Waiting for a request.
            """

    def exit_critical_section(self):

        print("Node " + str(self.id) + " is exiting the critical section.")

        self.using = False
        self.assign_privilege()

    # def receive_request(self, node):

    #     print("Node " + str(self.id) + " received a request from node " + str(node.get_id()) + ".")

    #     self.request_q.put(node)
    #     self.assign_privilege()
    #     self.make_request()

    # def request_privilege(self):
    #     self.holder = self
    #     self.assign_privilege()
    #     self.make_request()
    
    # def enter_critical_section(self):
        # self.request_q.put(self)
    #     self.assign_privilege()
    #     self.make_request()
    