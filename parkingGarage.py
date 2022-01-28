import random

class Garage():
    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
    
    def payForParking(self):
       payment =  input("\nHow much are you paying for your ticket?")



tickets = []
for i in range(100):
    tickets.append(i + 1)
garage = Garage([], [], {})