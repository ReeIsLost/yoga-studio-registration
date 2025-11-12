from colorama import Fore, Back, Style, init

class Person:
    def __init__(self, firstname, lastname, age, gender, phonenumber):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.phonenumber = phonenumber

    def full_info(self):
        print(Fore.GREEN + f"FirstName: {self.firstname}\nLastName: {self.lastname}\nAge: {self.age}\nGender: {self.gender}\nPhone Number: {self.phonenumber}")