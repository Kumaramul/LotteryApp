import pytest
from src.service import NewDraw



class TestClass:
    new_draw_test = { 'new_draw_test': [
                     {'lottery_started': 0,'money_collection_previous_draw' : 53255},
                     {'lottery_started': 1,'money_collection_previous_draw' : 100},
                     {'lottery_started': 0,'money_collection_previous_draw' : 73}
                      ]}

    def test_new_draw_for_lottery_initiated(self):
        for new_draw in self.new_draw_test['new_draw_test']:
            lottery_started, pot_size= NewDraw.newDraw(new_draw['lottery_started'], new_draw['money_collection_previous_draw'])

            assert lottery_started == 1
            

    def test_new_draw_for_pot_size_after_lottery_initiated(self):
        for new_draw in self.new_draw_test['new_draw_test']:
            lottery_started, pot_size= NewDraw.newDraw(new_draw['lottery_started'], new_draw['money_collection_previous_draw'])

            assert pot_size == (new_draw['money_collection_previous_draw']+100)