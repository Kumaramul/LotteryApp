import pytest

from src.util.calculate_distributed_money_for_person_group import calculate_distributed_money_for_person_group

## Test for group 2
def  test_calculate_distributed_money_for_person_group_two():
    mock_group_number =2 
    mock_total_ticket_for_person_each_group =3 
    mock_group_count = 4 
    mock_pot_size = 1500

    real_mock_price_money_for_person  = calculate_distributed_money_for_person_group(
        mock_group_number,mock_total_ticket_for_person_each_group,mock_group_count, mock_pot_size) 
    
    pot_prize_money_for_group_two = mock_pot_size*(10/100) 
    price_money_for_group = pot_prize_money_for_group_two / mock_group_count
    calculate_mock_distributed_money_for_person_group  = price_money_for_group * mock_total_ticket_for_person_each_group
    
    assert real_mock_price_money_for_person == calculate_mock_distributed_money_for_person_group
    assert real_mock_price_money_for_person < mock_pot_size

## Test for group 4
def  test_calculate_distributed_money_for_person_group_four():
    mock_group_number =4 
    mock_total_ticket_for_person_each_group =2 
    mock_group_count = 2 
    mock_pot_size = 2000

    real_mock_price_money_for_person  = calculate_distributed_money_for_person_group(
        mock_group_number,mock_total_ticket_for_person_each_group,mock_group_count, mock_pot_size) 
    
    pot_prize_money_for_group_four = mock_pot_size*(25/100)
    price_money_for_group = pot_prize_money_for_group_four / mock_group_count
    calculate_mock_distributed_money_for_person_group = price_money_for_group *mock_total_ticket_for_person_each_group
    
    assert real_mock_price_money_for_person == calculate_mock_distributed_money_for_person_group
    assert real_mock_price_money_for_person < mock_pot_size