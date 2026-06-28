# In this file I would write the code again so I will remember the code and syntax for a long time in my life.
# __init__ method is a instance method 
# Is used for to create or initilize the attribut while creating the objects.

class mukoo():
    print("Mukoo is an intelligent dog who follows my command...")

    def __init__(self, freedom, Eat, Bark):
        self.freedom = freedom
        self.Eat = Eat
        self.Barking = Bark

dog = mukoo("5 km from home", "Eggs, meat and vegetable", "When he hears the horn and unknown sounds")
print(dog.__dict__)

# Now I will nerve forgot this in my whole life.