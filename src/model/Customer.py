from .Ticket import Ticket
class Customer:    

    def __init__(self, name):
        self.name =  name
        self.number_of_ticket = None
        self.total_purchased_tickets = []

    def customer_tickets(self, num_of_ticket):
        self.number_of_ticket = num_of_ticket
        for i in range(num_of_ticket):
            ticketRef = Ticket()
            ticket_num  = ticketRef.ticket_genrator()
            self.total_purchased_tickets.append(ticket_num)
        return self.total_purchased_tickets
