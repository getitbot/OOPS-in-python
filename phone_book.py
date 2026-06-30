class phonebook:
    
    contact_number = []

    def __init__(self, name, number):
        self.name = name
        self.number = number
        phonebook.contact_number.append(self)

    def show_contact(self):
        return f"name: {self.name} number: {self.number}"
    

    @classmethod
    def show_all_contact(cls):
        if len(cls.contact_number) == 0:
            print("No contact found in the phone book")

        else:
            for contact in cls.contact_number():
                print(contact)

c1 = phonebook("Honey singh munariya", 8700627563)
c2 = phonebook("kanishka singh munariya", 8700146257)
print(phonebook.contact_number)
print(c1.show_contact())
print(c2.show_contact())







        