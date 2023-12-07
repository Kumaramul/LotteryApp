from .menu_banner import menu_banner

def main_menu_input(lottery_started, pot_size):
    '''
    This method use for get user input for menu 
    '''
    while True:
        entered_option = input(">input: ").strip()
        print()
        if entered_option =="" or  (not entered_option.isnumeric()) or int(entered_option)>3 or int(entered_option)<=0:
            print("/n Enter Valid  Number 1, 2 or 3 Option input ....")
            menu_banner(lottery_started, pot_size)
        else:
            break
    return entered_option 