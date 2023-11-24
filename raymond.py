"""

Brenda Silva Machado - 2023.2

raymond.py contains the class Raymond, which is used to implement the Raymond's algorithm.

"""

import handler
import threading
import time

class Raymond:
    def __init__(self):
        self.lock = threading.Lock()
        self.handler = handler.Handler()
        self.request_q = self.handler.get_request_q()

    def get_lock(self):
        return self.lock
    
    def get_handler(self):
        return self.handler
    
    def get_request_q(self):
        return self.request_q
    
    