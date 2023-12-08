import pytest
from unittest import mock
import  builtins
from src.util.menu_utils import main_menu_input



class TestClass:
    mock_menu_test = { 'mock_menu_test': [
                     {'lottery_started' : 0,'pot_size':100},
                     {'lottery_started' : 1,'pot_size':1500},
                     {'lottery_started' : 0,'pot_size':5000}
                      ]}


    options = [1,2,3]

    def test_menu_input_for_oprtion_one(self):
        for put in self.mock_menu_test['mock_menu_test']:
            mock_lottery_started = put['lottery_started']
            mock_pot_size= put['pot_size']
            with mock.patch.object(builtins, 'input', lambda _: str(self.options[0])):
                    mock_entered_option = main_menu_input(mock_lottery_started, mock_pot_size)
                    assert mock_entered_option == '1' 


