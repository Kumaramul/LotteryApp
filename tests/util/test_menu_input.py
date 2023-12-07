import unittest
from unittest.mock import patch
from src.util import menu_input



class TestClass(unittest.TestCase):
    

    @patch('builtins.input', lambda *args: '1')
    def test_menu_input_one(self):
        lottery_started =1 
        pot_size =100
        mock_entered_option= menu_input.main_menu_input(lottery_started, pot_size)
       
        assert mock_entered_option == '1'

    @patch('builtins.input', lambda *args: '3')
    def test_menu_input_three(self):
        lottery_started =0 
        pot_size =100
        mock_entered_option= menu_input.main_menu_input(lottery_started, pot_size)
       
        assert mock_entered_option == '3', "Option three not allowed if lottery not started"


    @patch('builtins.input', lambda *args: '2')
    def test_menu_input_four(self):
        lottery_started =1 
        pot_size =100
        mock_entered_option= menu_input.main_menu_input(lottery_started, pot_size)
       
        assert mock_entered_option == '2'