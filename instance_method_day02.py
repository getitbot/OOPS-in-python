class Student:
    """My name is honey and I'm going to be a good person in life"""

    def study(self, N_hours):
        print(f"Honey studys for {N_hours} hours a day....")
    
    def sport(self, N_hours):
        print(f"Honey plays sport for {N_hours} hours a day... ")
    
    def watch(self, N_hours):
        print(f"Honey watchs TV for {N_hours}  min a day")

student1 = Student()
print(Student)
student1.study(3)

student2= Student()
print(Student)
student2.sport(2)

student3 = Student()
print(Student)
student3.watch(30)

#  Creating a class for a book store. 

class bookstore():

    print('''This is the class where we manage info about our book store''')
    def __init__(self, bookname, quentity, order):
        self.bookname = bookname
        self.quentity = quentity
        self.order = order

    
bookstore1 = bookstore("Math", 345, "There are three orders")

print(bookstore1.__dict__)