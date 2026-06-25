# In this file we will study about the instance method.
# Methods, defined inside a class which is bound to/ associated with the instance/Object. 

class Student:
    """This is class student to manage info and activity of studentds"""

    def study(self):
        print("The student study 3 hours for a day")

Student1 = Student()
print(Student1)
Student1.study()





# try one more time for


class Honey:
    """ Honey is the most handsome person and he is a Good boy.😁"""
    def handsome(arg):
        print("Honey is going to be a Devops in his life and will secure atleast 30LPA package in google or other MNC company")

Honey1 = Honey()
print(Honey1)

Honey1.handsome()



