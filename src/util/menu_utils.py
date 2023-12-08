
def menu_banner(lottery_started, pot_size):
    '''
    This method use for display menu banner 
    '''
    print()
    print("~~~")
    print("Welcome to My Raffle App")
    if lottery_started==0:
        print("Status: Draw has not started\n")
    else:
        print("Status: Draw is ongoing. Raffle pot size is $", pot_size,"\n")
    print("[1] Start a New Draw")
    print("[2] Buy Tickets")
    print("[3] Run Raffle\n")
    print("~~~\n")


def main_menu_input(lottery_started, pot_size):
    '''
    This method use for get user input for menu 
    '''
    while True:
        entered_option = input(">input: ").strip()
        print()
        if entered_option =="" or  (not entered_option.isnumeric()) or int(entered_option)>3 or int(entered_option)<=0:
            print("\n Enter Valid  Number 1, 2 or 3 Option input ....")
            menu_banner(lottery_started, pot_size)
        else:
            break
    return entered_option 

