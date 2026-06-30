# # In this file we all are going to learn about the static methods.
# static methods are nothing but are the methods which nither bound to the class nor to the objects.


class Honey:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def study(self, n_hours):
        print(f"{self.name} studies for  {n_hours} hours a day")

    @staticmethod
    def greet():
        print("We need to greet everyone in the morning")

    @classmethod
    def test(cls):
        print("This is created by using class methods.")

student1 = Honey("Honey_singh_munariya", 777)
student1.greet()
student1.study(3)
student1.test()





        
# Soo this is how we use the staticmethods in the python programming language.
# I hope you all have enjoyed this session let's see in the next one.