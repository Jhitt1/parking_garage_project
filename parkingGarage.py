import random
from datetime import datetime #I copied this from Derek's code
now = datetime.now()
current_time = now.strftime("%H:%M:%S")


class Garage():
    def __init__(self, tickets, parkingSpaces, currentTicket = {'ticket_number': 0, 'parking_space_number': 0, 'paid': False}, leave = False):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
        self.leave = leave

# Jesse section start    
    def takeTicket(self):
        temp_ticket_number =  random.choice(self.tickets)
        self.currentTicket["ticket_number"] = temp_ticket_number
        self.tickets.remove(temp_ticket_number)
        temp_parkingSpaces = random.choice(self.parkingSpaces)
        self.currentTicket["parking_space_number"] = temp_parkingSpaces
        self.parkingSpaces.remove(temp_parkingSpaces)
        input("\nThe current time is " + current_time + ". ")
        input("\nYour parking space is " + str(temp_parkingSpaces) + ". ")
        input("\nYour ticket number is " + str(temp_ticket_number) + ". ")
        input("\nPlease pay for your ticket once your ready to leave. ")
# Jesse secion end

# Justin section start
    def payForParking(self):
        try:
            payment = float(input("\nHow much are you paying for your ticket?"))
            payment = float("{:.2f}".format(payment)) #I copied this from Derek's code
        except:
            input("\nThat is an invalid payment. Please try again. ")
        if payment > 0:
            self.currentTicket['paid'] = True
            input("\nThank you for paying! Please leave in the next 15 minutes, or you will be charged. ")
        else:
            input("\nThat payment is not acceptable. Please pay more $0.00.")
# Justin section end

#Jesse secion start
    def leaveGarage(self):
        if self.currentTicket['paid'] == False:
            input("\nYou must pay before you can leave! ")  
            try:
                payment = float(input("\nHow much are you paying for your ticket? "))
                payment = float("{:.2f}".format(payment))
            except:
                input("\nThat is an invalid payment. Please try again. ")
            if payment > 0:
                self.currentTicket['paid'] = True
            else:
                input("\nThat payment is not acceptable. Please pay more $0.00.")
        if self.currentTicket['paid'] == True:
            self.tickets.append(self.currentTicket["ticket_number"])
            self.parkingSpaces.append(self.currentTicket["parking_space_number"])
            input("\nThank you, have a nice day. ")
            self.leave = True
# Jesse section end

# Justin section start
tickets = []
parkingSpaces = []
for i in range(100):
    tickets.append(i + 1)
for i in range(100):
    parkingSpaces.append(i + 1)
garage = Garage(tickets, parkingSpaces)
# Justin section end

# Justin section start
garage.takeTicket()
while garage.leave == False:
    choice = input("""What would you like to do in the garage?
    ----------------
    •"Pay"
    ----------------
    •"Leave"
    ----------------
    """).lower()
    if choice == 'pay':
        if garage.currentTicket['paid'] == False:
            garage.payForParking()
        else:
            input("\nYou've already paid. Please leave before 15 minutes after the time you paid. ")
    elif choice == 'leave':
        garage.leaveGarage()
# Justin section end