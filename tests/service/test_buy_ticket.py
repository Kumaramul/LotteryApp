import unittest
from unittest.mock import patch
from src.service import BuyTicket

class TestClass(unittest.TestCase):
    
    @patch('builtins.input', lambda _: 'Jhon,2')   
    def test_buy_ticket(self):
        mock_pot_size =100
        mock_ticket_price = 5
        number_of_ticket = 2
        mock_ticket_collection_before_selling= {}
        mock_ticket_collection ,returned_pot_size = BuyTicket.buyTicket(mock_ticket_collection_before_selling , mock_pot_size, mock_ticket_price)

        self.assertEqual(returned_pot_size, mock_pot_size+(number_of_ticket*mock_ticket_price))
        self.assertEqual(mock_ticket_collection['Jhon'].number_of_ticket,number_of_ticket)

    @patch('builtins.input', lambda _: 'AB, 3')   
    def test_buy_ticket_two(self):
        mock_pot_size =3500
        mock_ticket_price = 5
        number_of_ticket = 3
        mock_ticket_collection_before_selling= {}
        mock_ticket_collection ,returned_pot_size = BuyTicket.buyTicket(mock_ticket_collection_before_selling , mock_pot_size, mock_ticket_price)

        self.assertEqual(returned_pot_size, mock_pot_size+(number_of_ticket*mock_ticket_price))
        self.assertEqual(mock_ticket_collection['AB'].number_of_ticket,number_of_ticket)
    
    