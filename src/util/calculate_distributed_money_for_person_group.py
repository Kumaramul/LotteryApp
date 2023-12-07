
def calculate_distributed_money_for_person_group(group_number , total_ticket_per_person_each_group, group_count, pot_size):
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
    