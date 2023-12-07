import unittest
from unittest.mock import patch
from src.util import selling_tickets

class TestClass(unittest.TestCase):
    
    @patch('builtins.input', lambda _: 'ABC,2') 
    def test_selling_tickets(self):
        mock_ticket_collection_before_selling = {}
        _ , name , num_ticket =  selling_tickets.selling_tickets(mock_ticket_collection_before_selling)

        assert name =='ABC' 
        assert num_ticket == 2 
