import random

class Ticket:
    def __init__(self):
        self.ticket_number = None

    def ticket_genrator(self):
         self.ticket_number=  random.sample(range(1, 15),5)
         return self.ticket_number    