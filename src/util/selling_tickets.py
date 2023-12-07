
def selling_tickets(ticket_collection):
    while True:
        name = None
        num_ticket = None
        print("~~~ \nEnter your name, no of tickets to purchase \n~~~")
        print()
        input_values = input(">input: ").split(",")
        print()
        if len(input_values)==2:
            if  all( x.isalpha() or x.isspace() for x in input_values[0].strip()) or input_values[0].strip()!= '':
                if ticket_collection.get(input_values[0].strip()) is None:
                    name = input_values[0].strip()   
                else:
                    print("~~~ \nUsername already register in Ongoing lottery enter another vaild name \n~~~")
            else:
                print("~~~ \nEnter vaild name \n~~~")
            if input_values[1].strip().isnumeric() and int(input_values[1].strip())>0 and int(input_values[1].strip())<=5:
                num_ticket = int(input_values[1].strip())
            else:
                print("~~~ \nEnter vaild number of tickets range(1-5) \n~~~")
        if name and num_ticket:
            break
    return ticket_collection, name, num_ticket