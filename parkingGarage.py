import random

class Garage():
    def __init__(self, tickets, parkingSpaces, currentTicket = {'ticket_number': 0, 'parking_space_number': 0, 'paid': False}):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
    
    def payForParking(self):
       payment =  input("\nHow much are you paying for your ticket?")




tickets = []
parkingSpaces = []
for i in range(100):
    tickets.append(i + 1)
for i in range(100):
    parkingSpaces.append(i + 1)
garage = Garage(tickets, parkingSpaces, {})