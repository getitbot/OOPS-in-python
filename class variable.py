# class variable are created on a class level...
# The copy of class variable distribute amoungs the objects....


class House():
    wall = "Group of the brick"
    Gate = ["main gate", "Kitchen gate", "Bathroom gate"]

    def __init__(self, name, number, area):
        self.name = name
        self.number = number
        self.area = area

home = House("Welcome", 1, "60sq feet")

print(home.__dict__)


print(home.wall)
print(House.Gate)


# this is how we use the class variable and the object variable 
# We can use the class variable's copy in objects.

