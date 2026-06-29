# In this file we are going to use classmethod.
# The useful of the class method in program.
# I know after 3-5 years I'll laugh to my code but I have to write this comment.

class Honey:


    DOB = 18
    Name = "Honey singh munariya"
    Gadgets = ["mobile", "laptop", "Tablat", "Desktop"]

    def __init__(self, language, career, project):
        print("Honey singh munariya is the main character in his life and will achive everthing.")
        self.language = language
        self.career = career
        self.project = project

    def study(self):
        print("He studies for 5 to 8 hours a day...")

    @classmethod
    def Munariya(cls):
        print(f"Using the classmethod {cls.DOB} ")

    for gadget in Gadgets:
        print(gadget)

student1 = Honey
student1.Munariya()
print(Honey)


