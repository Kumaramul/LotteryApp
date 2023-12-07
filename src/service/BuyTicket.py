import readchar

from model.Customer import Customer
from util.selling_tickets import selling_tickets

def buyTicket(ticket_collection, pot_size, ticket_price):
    name =  None
    num_ticket =  None
    sold_tickets , name , num_ticket = selling_tickets(ticket_collection)
    pot_size = pot_size + (num_ticket * ticket_price)
    ticket_obj  = Customer(name)
    ticket_per_person = ticket_obj.customer_tickets(num_ticket)
    ticket_collection[name] = ticket_obj
    print()
    print("Hi ", name,", you have purchased", num_ticket,"ticket(s)-")
    for i, per_ticket in enumerate(ticket_per_person):
        print("Ticket ", (i+1),":",' '.join(str(e) for e in per_ticket))
    print()
    print("Press any key to return to main menu")
    print("~~~")
    readchar.readchar()

    return sold_tickets , pot_size