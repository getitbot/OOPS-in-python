# __init_ methods
# It's an instance method.
# It's uesd for create and initialize the attributes during the object creation.

class Honeysinghmunariya():
    print("Honey is the main character in his life and will achive everything he wants to achive.")

    def __init__(self, name, roll, dept):
        self.name = name
        self.roll = roll
        self.department = dept

    # def sports(self):
    #     print("I play to win or Enjoy not to loss.")

    # def Watch(self):
    #     print("I watch what I want to be in future.....")

student1 = Honeysinghmunariya("Hoeny singh munariya", 7, "Science")
# print(student1.name, student1.roll, student1.department)
student2 = Honeysinghmunariya("Kanishka", 7, "Arts")
# print(student2.name, student2.roll, student2.department)

print(student1.__dict__)
print(student2.__dict__)



