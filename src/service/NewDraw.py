from util.constants import NEW_DRAW_POT_SIZE_FUND

def newDraw(lottery_started, money_collection_previous_draw):
    '''
    This is New Draw method  for option 1 when user want to start new draw and it addup 
    pot size by 100
    '''
    intial_fund = NEW_DRAW_POT_SIZE_FUND
    pot_size = intial_fund + money_collection_previous_draw
    lottery_started = 1
    print("```")
    print("New Raffle draw has been started. Initial pot size: $", pot_size)
     
    return lottery_started , pot_size
