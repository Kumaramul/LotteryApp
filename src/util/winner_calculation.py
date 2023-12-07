
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

    for collection in ticket_collection.values():
        name = collection.name
        tickets = collection.total_purchased_tickets

        for i in tickets:
            number_matches = list(set(i).intersection(winning_ticket_number))

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
    
    