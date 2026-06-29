# So this is the third time I'm practicing for the class methods.
# Now we  are going to create a class and will use a class methods and class variables

class Kanishka:
    
    honey = "Honey loves kanishka"
    honey_singh_munariya  = "Honey singh munariya will merry to Kanishka"

    def __init__(self, love, heart, loyal):
        self.love = love
        self.heart = heart
        self.loyal = loyal


    @classmethod
    def singh(cls):
        print(f"Honey is loyal to Kanishka and {cls.honey_singh_munariya}")

        
kanishka_singh_munariya = Kanishka("Honey loves kanishka", "His heart belongs to kanishka", "He is loyal to kanishka")
kanishka_singh_munariya.singh()
print(Kanishka)
print(kanishka_singh_munariya)



