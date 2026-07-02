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
            for contact in cls.contact_number:
                print(contact.show_contact())


    @classmethod
    def search_contact(cls, search_name):
        for contact in cls.contact_number:
            if contact.name.lower() == search_name.lower():
                return print(f"The number of the  {contact.name.lower()} is {contact.number}")
            
        return f"No contact found for {search_name}"
    

    @staticmethod
    def validate_phone_number(number):
        if len(number) >= 8 and number.isdigit():
            return True
        else:
            return False
        
n_contacts = int(input("Enter the number how much number you want to add.?  "))
for i in range(n_contacts):
    names = input("Enter the names ")
    phone_number = input(f"Enter the phone numbers b")
    if phonebook.validate_phone_number(phone_number):
        phonebook(names, phone_number)
    else:
        print("Invalid phone number")



phonebook.show_all_contact()
# c1 = phonebook("Honey singh munariya", 8700627563)
# c2 = phonebook("kanishka singh munariya", 8700146257)
# print(phonebook.contact_number)
# print(c1.show_contact())
# print(c2.show_contact())
# c1.show_all_contact()

# c1.search_contact("Honey singh munariya")
# c2.search_contact("kanishka singh munariya")









