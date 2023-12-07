# from src.util import winner_calculation


# def test_winner_calculation():
#     winning_ticket_number = [ 5, 12, 3, 7, 2]
#     ticket_collection = {
#     "A":[[12 , 4, 3 , 5 ,2],  
#          [1, 4, 12, 3, 7],  
#          [6, 4, 8, 5, 3]]  ,
    
#     "B":[[7 , 12, 3 , 9 ,2] , 
#          [3, 4, 2, 9, 7]]  

#     }
    
    
#     [(grouptwowinners, grouptwo_count),
#             (groupthreewinners, groupthree_count),
#             (groupfourwinners, groupfour_count),
#             (groupfivewinners, groupfive_count)] = winner_calculation.winner_calculation(winning_ticket_number,ticket_collection)

#     assert len(groupfourwinners) == 3
#     assert groupfour_count == 3

#     assert len(groupthreewinners) == 1
#     assert groupthree_count == 1

#     assert len(grouptwowinners) == 1
#     assert grouptwo_count == 1