from random import randint

class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(self,fro,to):
        print(f"Ticket is booked in Train No:{self.trainNo} From {fro} To {to}")

    def getStatus(self):
          print(f"Train No:{self.trainNo} is Running On Time")

    def getFare(self,fro,to):
        print(f"Ticket is Fare in Train No:{self.trainNo} From {fro} To {to} is:{randint(200,5000)}")

t = Train(1548963)
t.book("Bhavnagar","Dwarka")
t.getStatus()
t.getFare("Bhavangar","Somanath")