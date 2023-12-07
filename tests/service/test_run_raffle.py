import unittest
from src.service import RunRaffle
from src.model import Customer

def test_run_raffle_one():
    num_of_ticket =3
    name = "Jhon"
    customer  = Customer.Customer(name)
    customer.customer_tickets(num_of_ticket)
    ticket_collection ={}
    ticket_collection["Jhon"] = customer
    mock_pot_size=35700
    distributed_money = RunRaffle.runRaffle(ticket_collection, mock_pot_size)

    assert distributed_money>=0
    assert distributed_money<=mock_pot_size


def test_run_raffle_two():
    num_of_ticket =3
    name = "Jhon"
    customer  = Customer.Customer(name)
    customer.customer_tickets(num_of_ticket)
    ticket_collection ={}
    ticket_collection["Jhon"] = customer
    mock_pot_size=100
    distributed_money = RunRaffle.runRaffle(ticket_collection, mock_pot_size)

    assert distributed_money>=0
    assert distributed_money<=mock_pot_size
