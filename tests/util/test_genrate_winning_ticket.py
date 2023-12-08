
from src.model.Ticket import  Ticket
from src.util.calculation_utils import genrate_winning_ticket


def test_genrate_winning_ticket():
    ticket = Ticket()
    winning_ticket = ticket.getTicketNumber()
    
    assert len(winning_ticket) ==5
    
    for i in winning_ticket:
        assert i >0 and i<=15