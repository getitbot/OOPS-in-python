# inheritance :- by using the we can creat two classes and get use used the both's object in each other.
# first class would be called as the parent class
# The second class would be called as the child class.

class vehicle:
    company = "Tata steel"

    def __init__(self,wheel, seats, gears):
        self.wheel =  wheel
        self.seats = seats
        self.gears = gears

    def bike(self):
        print(f"the bike has {self.wheel} wheels , {self.gears} gears and {self.seats} seats " )

c1 = vehicle(2, 2, 5)
c1.bike()
print(c1.bike)

class Car(vehicle):

    model = "Honey singh munariya"

    def __init__(self, whee, seat, gear):
        self.seat = seat
        self.whee = whee
        self.gear = gear

    super().__init__(4, 2  , 5)

c1 = Car(2,2,5 )
c1.bike()
print(c1.bike)
print(c1.model)
        






















# Soo in this code the Vehicle is our parent class.
# class car is our child class.



9930749689