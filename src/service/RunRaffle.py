''' 
This assignment
Created By Amul Kumar 
on 8-12-2023
'''

from util.calculation_utils import genrate_winning_ticket
from util.calculation_utils import winner_calculation
from util.calculation_utils import calculate_distributed_money_for_person_group

def runRaffle(ticket_collection, pot_size, winning_ticket_number):
    '''
    This is run raffle method  for option 3. user can call  to show winners
    for ongoing draw
    '''
    distributed_money =0
    print("~~~ \nRunning Raffle..") 
    if winning_ticket_number:
        pass #this block is for internal testing only
    else:
        winning_ticket_number = genrate_winning_ticket()
    print("Winning Ticket is",' '.join(str(e) for e in winning_ticket_number))
    [(grouptwowinners, grouptwo_count),
    (groupthreewinners, groupthree_count),
    (groupfourwinners, groupfour_count),
    (groupfivewinners, groupfive_count)] =  winner_calculation(winning_ticket_number, ticket_collection)
    
    print()
    print("Group 2 Winners:")
    if grouptwo_count == 0:
        print("Nil")
    else:
        for person in grouptwowinners:
            price_money_for_group_two= calculate_distributed_money_for_person_group(2, grouptwowinners[person], grouptwo_count,pot_size)
            distributed_money+=price_money_for_group_two
            print(person, "with ",grouptwowinners[person],"winning ticket(s)- $",round(price_money_for_group_two,4))
    print()
    print("Group 3 Winners:")
    if groupthree_count==0:
        print("Nil")
    else:
        for person in groupthreewinners:
            price_money_for_group_three=calculate_distributed_money_for_person_group(3, groupthreewinners[person], groupthree_count,pot_size)
            distributed_money+=price_money_for_group_three
            print(person, "with ",groupthreewinners[person],"winning ticket(s)- $",round(price_money_for_group_three,4))
    print()
    print("Group 4 Winners:")
    if groupfour_count==0:
        print("Nil")
    else:
        for person in groupfourwinners:
            price_money_for_group_four=calculate_distributed_money_for_person_group(4, groupfourwinners[person], groupfour_count,pot_size)
            distributed_money+=price_money_for_group_four
            print(person, "with ",groupfourwinners[person],"winning ticket(s)- $",round(price_money_for_group_four,4))
    print()
    print("Group 5 Winners: (Jackpot)")
    if groupfive_count==0:
        print("Nil")
    else:
        for person in groupfivewinners:
            price_money_for_group_five=calculate_distributed_money_for_person_group(5, grouptwowinners[person], groupfive_count,pot_size)
            distributed_money+=price_money_for_group_five
            print(person, "with ",groupfivewinners[person],"winning ticket(s)- $",round(price_money_for_group_five,4))
    print()
    
    return distributed_money, winning_ticket_number