
from src.util.genrate_winning_ticket import genrate_winning_ticket


def test_genrate_winning_ticket():
    winning_ticket = genrate_winning_ticket()
    
    assert len(winning_ticket) ==5
    
    for i in winning_ticket:
        assert i >0 and i<=15