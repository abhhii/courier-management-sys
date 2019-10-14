import sqlite3
import random



################################################################

# User Address Class
class Address:
    def __init__(self, A_lane, A_station, A_pin):
        self.lane = A_lane
        self.station = A_station
        self.PIN = A_pin

#User Class
class User:
    def __init__(self, U_name, U_lane, U_station, U_PIN):
        self.loc = Address(U_lane, U_station, U_PIN)
        self.name = U_name


# Delivery class
class Delivery:

    def __init(self):
        self.d_id = 3333
        self.weight = 0
        self.price = 0
        self._sender =[]
        self._receiver =[]

        # result of this will be sent as sender
    def _senderInfo(self,_askForPrompts):
        print("Sender's Info: ")
        # self._sender = (_askForPrompts())

        self._sender = User(*(_askForPrompts()))
        self._calcWeight()
        # print("SENDER'S INFORMATION: ", U_SENDER.name, U_SENDER.loc.lane, U_SENDER.loc.station, U_SENDER.loc.PIN)
        # result of this will be sent as receiver
    def _receiverInfo(self, _askForPrompts):
        print("Receiver's Info: ")
        # self._receiver = (_askForPrompts())

        self._receiver = User(*(_askForPrompts()))

        # print("RECEIVER'S INFORMATION: ", U_RECEIVER.name, U_RECEIVER.loc.lane, U_RECEIVER.loc.station, U_RECEIVER.loc.PIN)


    def _calcWeight(self):
        self.weight = int(input("Weight of Order: "))
        # claculating price of the delivery
        self.price = 50*self.weight + 100
        print("The price will be : ", self.price)




################################################################

# connecting to database
# conn = sqlite3.connect('courier.db')
#
# cur = conn.cursor()
# cur.execute()


################################################################
# getting user inputs
print("Enter user details: ")

def askPrompts():
    prompt_name = input("Name: ")
    prompt_address_lane = input("Address Lane:")
    prompt_address_station = input("Address Station:")
    prompt_address_PIN = input("Address PIN:")

    return [prompt_name, prompt_address_lane, prompt_address_station, prompt_address_PIN]


Order = Delivery()
Order._senderInfo(askPrompts)
Order._receiverInfo(askPrompts)


# printing user inputs
# print(f"Delivery INFO -----  of delivery_id - ", Order.d_id)
print("SENDER: ", Order._sender.name)
print("RECEIVER: ", Order._receiver.name)



################################################################
