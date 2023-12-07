import pytest
from src.service import NewDraw


def test_new_draw_one():
    lottery_started = 0
    money_collection_previous_draw =38
    lottery_started, pot_size= NewDraw.newDraw(lottery_started, money_collection_previous_draw)

    assert lottery_started ==1
    assert pot_size == (money_collection_previous_draw+100)

def test_new_draw_two():
    lottery_started = 1
    money_collection_previous_draw =5902
    lottery_started, pot_size= NewDraw.newDraw(lottery_started, money_collection_previous_draw)

    assert lottery_started ==1
    assert pot_size == (money_collection_previous_draw+100)