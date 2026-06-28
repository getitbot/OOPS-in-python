# Class methods are define inside a class and bound with the class.
# To create a class method we use a classmethod decorater.
# this is how we create a class method inside a class

class College:

    classmethod
    def greet(cls):
        print("welcome sir")

college1 = College()
college1.greet()
print(College)