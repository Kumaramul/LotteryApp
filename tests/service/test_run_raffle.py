import unittest
from src.service import RunRaffle
from src.model import Customer


class TestClass:

    mock_ticket_test = { 'mock_ticket_test': [
                     {'name':'testuser1', 
                      'tickets':[[ 5, 4, 3 ,14, 2],
                                           [ 3, 4, 6 ,2, 8],
                                           [ 7, 9, 12 ,14, 2],
                                           [ 5, 7, 9 ,4, 12],
                                           [ 6, 9, 12 ,14, 2]],
                    },
                     {'name':'testuser2', 
                      'tickets':[[ 1, 4, 8 ,9, 3],
                                           [ 8, 6, 5 ,2, 1],
                                           [ 7, 9, 13 ,14, 2],
                                           [ 3, 9, 15 ,12, 11],
                                           [ 9, 3, 12 ,4, 2]],
                     },
                     {'name':'testuser2', 
                      'tickets':[[ 5, 7, 3 ,13, 2],
                                           [ 3, 2, 6 ,9, 8],
                                           [ 7, 8, 12 ,13, 2],
                                           [ 8, 7, 6 ,14, 15],
                                           [ 6, 7, 4 ,5, 1]],
                     }
                      ]}

    mock_winning_ticket = [8,1,13,2,12]
    mock_distributed_money = 525
    mock_pot_size =1500

    def buy_mock_tickets_for_customer(self, customers):
            ticket_collection = {}

            customerObj  = Customer.Customer(customers['name'])
            customerObj.set_manual_tickets(customers['tickets'])
            ticket_collection[customers['name']]  = customerObj
            return ticket_collection

    def test_run_raffle_for_distributed_total_money(self):
        for cus in self.mock_ticket_test['mock_ticket_test']: 
            ticket_collection = self.buy_mock_tickets_for_customer(cus)
        winning_ticket_number = self.mock_winning_ticket
        distributed_money, winning_ticket_number  = RunRaffle.runRaffle(ticket_collection, self.mock_pot_size, winning_ticket_number)
        assert distributed_money == self.mock_distributed_money

    
    def test_pot_size_after_run_raffle_for_distributed_total_money(self):
            for cus in self.mock_ticket_test['mock_ticket_test']: 
                ticket_collection = self.buy_mock_tickets_for_customer(cus)
            winning_ticket_number = self.mock_winning_ticket
            distributed_money, winning_ticket_number  = RunRaffle.runRaffle(ticket_collection, self.mock_pot_size, winning_ticket_number)
            pot_size_after_draw_result = self.mock_pot_size - self.mock_distributed_money
            assert (self.mock_pot_size -distributed_money) == pot_size_after_draw_result
