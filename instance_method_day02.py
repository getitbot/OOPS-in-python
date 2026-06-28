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

