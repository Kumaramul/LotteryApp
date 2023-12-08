from model.Customer import Customer
from util.calculation_utils import buying_tickets

def buyTicket(ticket_collection, pot_size, ticket_price):
    '''
    This is buy Ticket method  for option 2 . user can call  after lottery start
    and when customer want to buy tickets.
    '''
    name =  None
    num_ticket =  None
    sold_tickets , name , num_ticket = buying_tickets(ticket_collection)
    pot_size = pot_size + (num_ticket * ticket_price)
    if ticket_collection.get(name):
        Customer_obj= ticket_collection.get(name)
        Customer_obj.set_customer_tickets(num_ticket)
    else:
        Customer_obj  = Customer(name)
        Customer_obj.set_customer_tickets(num_ticket)
        ticket_collection[name] = Customer_obj

    print()
    print("Hi ", name,", you have purchased", num_ticket,"ticket(s)-")
    for i, ticket in enumerate(Customer_obj.get_total_purchased_tickets()):
        print("Ticket ", (i+1),":",' '.join(str(e) for e in ticket.getTicketNumber()))
    print()

    return sold_tickets , pot_size