
def menu_banner(lottery_started, pot_size):
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