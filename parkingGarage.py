import random
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")


class Garage():
    def __init__(self, tickets, parkingSpaces, currentTicket = {'ticket_number': 0, 'parking_space_number': 0, 'paid': False}):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
    
    def takeTicket(self):
        temp_ticket_number =  random.choice(self.tickets)
        self.currentTicket["ticket_number"] = temp_ticket_number
        self.tickets.remove(temp_ticket_number)
        temp_parkingSpaces = random.choice(self.parkingSpaces)
        self.currentTicket["parking_space_number"] = temp_parkingSpaces
        self.parkingSpaces.remove(temp_parkingSpaces)
        inout("\nThe current time is " + current_time)
        input("\nYour parking space is " + str(temp_parkingSpaces))
        input("\nYour ticket number is " + str(temp_ticket_number))
        input("\nPlease pay for your ticket once your ready to leave.")




    def payForParking(self):
       payment =  input("\nHow much are you paying for your ticket?")




# justin section start
tickets = []
parkingSpaces = []
for i in range(100):
    tickets.append(i + 1)
for i in range(100):
    parkingSpaces.append(i + 1)
garage = Garage(tickets, parkingSpaces, {})