import random

class Ticket:
    '''
    This is Ticket Class contains ticket number  and getting for genrating ticket number.
    '''
    def __init__(self):
        self.__ticket_number = random.sample(range(1, 15),5)

    def getTicketNumber(self):
        return self.__ticket_number
    
    def setTicketManualNumber(self, ticketnumber):
        'This mehtod is use for internal testing only'
        set = 0
        if len(ticketnumber) == 5:
            for t in ticketnumber:
                if t>0 and t<=15:
                    set =1
            if set == 1:           
                self.__ticket_number  = ticketnumber
