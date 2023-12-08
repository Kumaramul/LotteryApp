''' 
This assignment
Created By Amul Kumar 
on 8-12-2023
'''

from .Ticket import Ticket


class Customer:    
    '''
    This is Customer Class contains name , number of ticket purcahsed by customer,
    and list of total ticket purcahed by customer. 
     and genrate tickets for a customer
    '''

    def __init__(self, name):
        self.__name =  name
        self.__number_of_ticket = None
        self.__total_purchased_tickets = []

    def set_customer_tickets(self, number_of_ticket):
        self.__number_of_ticket = number_of_ticket
        for i in range(self.__number_of_ticket):
            ticketRef = Ticket()            # Has-a Relationship
            self.__total_purchased_tickets.append(ticketRef)
    
    def get_total_purchased_tickets(self):
        return self.__total_purchased_tickets

    def get_number_of_ticket(self):
        return self.__number_of_ticket

    def get_name(self):
        return self.__name

    
    def set_manual_tickets(self, tickets_list):
        'This mehtod is use for internal testing only'

        self.__number_of_ticket = len(tickets_list)
        for ticket in tickets_list:
            ticketRef = Ticket()
            ticketRef.setTicketManualNumber(ticket)
            self.__total_purchased_tickets.append(ticketRef)

