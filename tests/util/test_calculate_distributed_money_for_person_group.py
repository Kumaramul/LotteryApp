import pytest

from src.util.calculation_utils import calculate_distributed_money_for_person_group

class TestClass:
    group_money_distribution_test = { 'group_money_distribution_test': [
                     {'mock_total_ticket_for_person_each_group' : 4,'mock_total_group_count':12, 'mock_pot_size':2100},
                      {'mock_total_ticket_for_person_each_group' : 2,'mock_total_group_count':9, 'mock_pot_size':1300},
                      {'mock_total_ticket_for_person_each_group' : 2,'mock_total_group_count':7, 'mock_pot_size':1200}
                      ]}


    mock_group_number = [2,3,4,5]

    def  test_calculate_distributed_money_for_person_group_two_winners(self):

        for group_winner in self.group_money_distribution_test['group_money_distribution_test']:
            real_mock_price_money_for_person  = calculate_distributed_money_for_person_group(
            self.mock_group_number[0],group_winner['mock_total_ticket_for_person_each_group'],group_winner['mock_total_group_count'], group_winner['mock_pot_size']) 
            
            pot_prize_money_for_group_two = group_winner['mock_pot_size']*(10/100) 
            price_money_for_group = pot_prize_money_for_group_two / group_winner['mock_total_group_count']
            calculate_mock_distributed_money_for_person_group  = price_money_for_group * group_winner['mock_total_ticket_for_person_each_group']
            
            assert real_mock_price_money_for_person == calculate_mock_distributed_money_for_person_group
            assert real_mock_price_money_for_person < group_winner['mock_pot_size']
    
    def  test_calculate_distributed_money_for_person_group_three_winners(self):

        for group_winner in self.group_money_distribution_test['group_money_distribution_test']:
            real_mock_price_money_for_person  = calculate_distributed_money_for_person_group(
            self.mock_group_number[1],group_winner['mock_total_ticket_for_person_each_group'],group_winner['mock_total_group_count'], group_winner['mock_pot_size']) 
            
            pot_prize_money_for_group_two = group_winner['mock_pot_size']*(15/100) 
            price_money_for_group = pot_prize_money_for_group_two / group_winner['mock_total_group_count']
            calculate_mock_distributed_money_for_person_group  = price_money_for_group * group_winner['mock_total_ticket_for_person_each_group']
            
            assert real_mock_price_money_for_person == calculate_mock_distributed_money_for_person_group
            assert real_mock_price_money_for_person < group_winner['mock_pot_size']

    
    def  test_calculate_distributed_money_for_person_group_four_winners(self):

        for group_winner in self.group_money_distribution_test['group_money_distribution_test']:
            real_mock_price_money_for_person  = calculate_distributed_money_for_person_group(
            self.mock_group_number[2],group_winner['mock_total_ticket_for_person_each_group'],group_winner['mock_total_group_count'], group_winner['mock_pot_size']) 
            
            pot_prize_money_for_group_two = group_winner['mock_pot_size']*(25/100) 
            price_money_for_group = pot_prize_money_for_group_two / group_winner['mock_total_group_count']
            calculate_mock_distributed_money_for_person_group  = price_money_for_group * group_winner['mock_total_ticket_for_person_each_group']
            
            assert real_mock_price_money_for_person == calculate_mock_distributed_money_for_person_group
            assert real_mock_price_money_for_person < group_winner['mock_pot_size']
    
    def  test_calculate_distributed_money_for_person_group_five_winners(self):

        for group_winner in self.group_money_distribution_test['group_money_distribution_test']:
            real_mock_price_money_for_person  = calculate_distributed_money_for_person_group(
            self.mock_group_number[3],group_winner['mock_total_ticket_for_person_each_group'],group_winner['mock_total_group_count'], group_winner['mock_pot_size']) 
            
            pot_prize_money_for_group_two = group_winner['mock_pot_size']*(50/100) 
            price_money_for_group = pot_prize_money_for_group_two / group_winner['mock_total_group_count']
            calculate_mock_distributed_money_for_person_group  = price_money_for_group * group_winner['mock_total_ticket_for_person_each_group']
            
            assert real_mock_price_money_for_person == calculate_mock_distributed_money_for_person_group
            assert real_mock_price_money_for_person < group_winner['mock_pot_size']

    def  test_calculate_distributed_money_for_person_group_two_winners(self):

        for group_winner in self.group_money_distribution_test['group_money_distribution_test']:
            real_mock_price_money_for_person  = calculate_distributed_money_for_person_group(
            self.mock_group_number[0],group_winner['mock_total_ticket_for_person_each_group'],group_winner['mock_total_group_count'], group_winner['mock_pot_size']) 
            
            pot_prize_money_for_group_two = group_winner['mock_pot_size']*(10/100) 
            price_money_for_group = pot_prize_money_for_group_two / group_winner['mock_total_group_count']
            calculate_mock_distributed_money_for_person_group  = price_money_for_group * group_winner['mock_total_ticket_for_person_each_group']
            
            assert real_mock_price_money_for_person == calculate_mock_distributed_money_for_person_group
            assert real_mock_price_money_for_person < group_winner['mock_pot_size']


