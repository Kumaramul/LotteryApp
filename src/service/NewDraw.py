import readchar

def newDraw(lottery_started, money_collection_previous_draw):
    '''
    This is New Draw method  for option 1 when user want to start new draw
    '''
    seed_fund = 100
    pot_size = seed_fund + money_collection_previous_draw
    lottery_started = 1
    print("```")
    print("New Raffle draw has been started. Initial pot size: $", pot_size)
    print("Press any key to return to main menu")
    print("```")
    readchar.readchar()  
    return lottery_started , pot_size
