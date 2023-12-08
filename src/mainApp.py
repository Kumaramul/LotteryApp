from util.menu_utils import menu_banner
from util.menu_utils import main_menu_input
from service.NewDraw import newDraw
from service.BuyTicket import buyTicket
from service.RunRaffle import runRaffle
import readchar

def main():
    ticket_price = 5
    money_collection_previous_draw = 0
    pot_size = None
    
    while True:
        lottery_started = 0  
        ticket_collection = {}
        menu_banner(lottery_started, pot_size)
        entered_option = int(main_menu_input(lottery_started, pot_size))
        if entered_option == 1:
            lottery_started,  pot_size = newDraw(lottery_started, money_collection_previous_draw)
            print("Press any key to return to main menu")
            print("```")
            readchar.readchar() 
        elif entered_option == 2:
            print("Cannot Buy Ticket first need to start lottery choose option 1")
        elif entered_option == 3:
            print("Cannot Run Raffle first need to start lottery choose option 1")
        else:
            print("/n Enter Valid  Number 1, 2 or 3 Option input ..")

        while lottery_started:               
            menu_banner(lottery_started, pot_size)
            entered_option_after_start = int(main_menu_input(lottery_started, pot_size))
            
            if entered_option_after_start == 2:
                ticket_collection, pot_size = buyTicket(ticket_collection, pot_size, ticket_price)
                print("Press any key to return to main menu")
                print("~~~")
                readchar.readchar()
                
            elif entered_option_after_start == 3:
                winning_ticket = None
                distributed_money, winning_ticket  = runRaffle(ticket_collection, pot_size, winning_ticket)
                print("Press any key to return to main menu")
                print("~~~") 
                readchar.readchar()  
                lottery_started = 0
                money_collection_previous_draw = pot_size - distributed_money
                print()
                
                

if __name__ == "__main__":
    main()