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
    
    def make_request(self):
        if self.holder != self and (not self.request_q.empty()) and (not self.asked):
            self.asked = True
            self.holder.receive_request(self)

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

                self.execute()
                self.exit_critical_section()

                """
                Leaves the critical section.
                """
 

            else:
                
                print("Node " + str(self.id) + " passed the privilege to node " + str(self.holder.get_id()) + ".")

                self.holder.request_privilege()

        print("Node " + str(self.holder.get_id()) + " get the token.")

    def execute(self):
        print("Node " + str(self.id) + " is executing.")
    
    def exit_critical_section(self):

        print("Node " + str(self.id) + " is exiting the critical section.")

        self.using = False
        self.assign_privilege()
        self.make_request()

    def receive_request(self, node):

        print("Node " + str(self.id) + " received a request from node " + str(node.get_id()) + ".")

        self.request_q.put(node)
        self.assign_privilege()
        self.make_request()

    def request_privilege(self):
        self.holder = self
        self.assign_privilege()
        self.make_request()
    
    def enter_critical_section(self):
        self.request_q.put(self)
        self.assign_privilege()
        self.make_request()
    