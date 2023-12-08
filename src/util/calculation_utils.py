''' 
This assignment
Created By Amul Kumar 
on 8-12-2023
'''

from model.Ticket import Ticket

def genrate_winning_ticket():
    '''
    This method use for genrating winnig ticket 
    '''
    return Ticket().getTicketNumber()

def buying_tickets(ticket_collection):
    '''
    This method use for  calculate total ticket collection, customer name and 
    number of ticket purchased by customer. 
    '''
    while True:
        name = None
        num_ticket = None
        print("~~~ \nEnter your name, no of tickets to purchase \n~~~")
        print()
        input_values = input(">input: ").split(",")
        print()
        if len(input_values)==2:
            if input_values[1].strip().isnumeric() and int(input_values[1].strip())>0 and int(input_values[1].strip())<=5:
                num_ticket = int(input_values[1].strip())
            else:
                print("~~~ \nEnter valid number of tickets range(1-5) \n~~~")
            
            if  all( x.isalpha() or x.isspace() for x in input_values[0].strip()) or input_values[0].strip()!= '':
                previous_ticket = ticket_collection.get(input_values[0].strip())
                if  previous_ticket is None:
                    name = input_values[0].strip()   
                else:
                    previous_ticket_len = previous_ticket.get_number_of_ticket()
                    if previous_ticket_len<5 and  num_ticket!=None and (previous_ticket_len+num_ticket)<=5:
                        name = input_values[0].strip()
                    else:
                        print("~~~ \n Username  exceeding maximum number of tickets  in Ongoing lottery enter another valid name \n~~~")
            else:
                print("~~~ \nEnter valid name \n~~~")
            
        if name and num_ticket:
            break
    return ticket_collection, name, num_ticket

def calculate_distributed_money_for_person_group(group_number , total_ticket_per_person_each_group, group_count, pot_size):
    '''
    This method use for  calculate distributed money for  a person of particular group
    '''
    price_money_for_person =None
    if group_number ==2:
        pot_prize_money_for_group_two = pot_size*(1/10) 
        price_money_for_group = pot_prize_money_for_group_two / group_count
        price_money_for_person = price_money_for_group * total_ticket_per_person_each_group
    if group_number ==3:
        pot_prize_money_for_group_three = pot_size*(3/20)
        price_money_for_group = pot_prize_money_for_group_three / group_count
        price_money_for_person = price_money_for_group *total_ticket_per_person_each_group
    if group_number ==4:
        pot_prize_money_for_group_four = pot_size*(1/4)
        price_money_for_group = pot_prize_money_for_group_four / group_count
        price_money_for_person = price_money_for_group *total_ticket_per_person_each_group
    if group_number ==5:
        pot_prize_money_for_group_five = pot_size*(1/2)
        price_money_for_group = pot_prize_money_for_group_five / group_count
        price_money_for_person = price_money_for_group *total_ticket_per_person_each_group

    return price_money_for_person

def winner_calculation(winning_ticket_number, ticket_collection):
    '''
    This method use for  calculate winners of ongoing lottery   for diffrrent groups 2,3,4 and 5. 
    '''
    grouptwowinners = {}
    grouptwo_count =0
    groupthreewinners = {}
    groupthree_count =0
    groupfourwinners = {}
    groupfour_count =0
    groupfivewinners = {}
    groupfive_count =0

    for name, collection in ticket_collection.items():
        tickets = collection.get_total_purchased_tickets()

        for i in tickets:
            number_matches = list(set(i.getTicketNumber()).intersection(winning_ticket_number))

            if len(number_matches) == 2:
                grouptwo_count+=1
                grouptwowinners[name] = grouptwowinners.get(name,0) +1
            elif len(number_matches) == 3:
                groupthree_count+=1
                groupthreewinners[name] =  groupthreewinners.get(name,0) +1
            elif len(number_matches) == 4:
                groupfour_count+=1
                groupfourwinners[name] =  groupfourwinners.get(name,0) +1
            elif len(number_matches) == 5:
                groupfive_count+=1
                groupfivewinners[name] =  groupfivewinners.get(name,0) +1
    
    return [(grouptwowinners, grouptwo_count),
            (groupthreewinners, groupthree_count),
            (groupfourwinners, groupfour_count),
            (groupfivewinners, groupfive_count)]

