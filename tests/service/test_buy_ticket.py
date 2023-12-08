from unittest import mock
import  builtins
from src.service import BuyTicket

class TestClass:
    
    buy_dict_test = { 'buy_dict_test': [
                     {'name':'test1','mock_pot_size': 3500,'mock_ticket_price' : 5,'number_of_ticket' : 4},
                     {'name':'test2','mock_pot_size': 100,'mock_ticket_price' : 5,'number_of_ticket' : 5},
                     {'name':'test3','mock_pot_size': 1233,'mock_ticket_price' : 5,'number_of_ticket' : 1}
                      ]}

    def test_for_validate_pot_size_after_buying_ticket(self):
            
            for obj in self.buy_dict_test['buy_dict_test']:
                input_name = obj['name']
                input_number_of_ticket = obj['number_of_ticket']
                with mock.patch.object(builtins, 'input', lambda _: input_name+','+str(input_number_of_ticket) ):
                    
                    mock_ticket_collection_before_selling= {}
                    mock_ticket_collection ,returned_pot_size = BuyTicket.buyTicket(mock_ticket_collection_before_selling , obj['mock_pot_size'], obj['mock_ticket_price'])

                    assert returned_pot_size == (obj['mock_pot_size']+(obj['number_of_ticket']*obj['mock_ticket_price']))
            

    def test_for_validate_customer_tickets_after_buying_ticket(self):
            
            for obj in self.buy_dict_test['buy_dict_test']:
                input_name = obj['name']
                input_number_of_ticket = obj['number_of_ticket']
                with mock.patch.object(builtins, 'input', lambda _: input_name+','+str(input_number_of_ticket) ):
                    
                    mock_ticket_collection_before_selling= {}
                    mock_ticket_collection ,returned_pot_size = BuyTicket.buyTicket(mock_ticket_collection_before_selling , obj['mock_pot_size'], obj['mock_ticket_price'])

                    assert  mock_ticket_collection[input_name].get_number_of_ticket() == obj['number_of_ticket']

       

 