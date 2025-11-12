import os
import time
from yoga import Yoga
from colorama import Fore, Back, Style, init

WAIT_TIME = 1 # When we use time.sleep(WAIT.TIME) to stop the code for 1 second.
init(autoreset=True)

def clear_screen():
    """
    To Clear The Screen To Make The Code Run Clean
    """
    os.system('cls' if os.name == 'nt' else 'clear')


# Get user info
def user_info():
    """
    Get user information and validate inputs
    """
    welcome()
    while True:
        firstname = input(Fore.LIGHTBLUE_EX + "Enter your first name: ")
        if firstname.isalpha():
            break
        else:
            print('First And Last Name Must Contain Letters Only!!')

        
    while True:
        lastname = input(Fore.LIGHTBLUE_EX + "Enter your last name: ")
        if lastname.isalpha():
            break
        else:
            print('First And Last Name Must Contain Letters Only!!')

    while True:
        age = input(Fore.LIGHTBLUE_EX + "Enter your age: ")
        if not age.isnumeric():
            print('Age Must Only Contain Numbers')
            continue

        age = int(age)
        if age <= 0:
            print('Age Must Be Older Than 0 Years Old.')
        elif age >= 85:
            print('Age Must Not Be Older Than 85 Years Old.')
            continue
        else:
            break
    
    while True:
        gender = input(Fore.LIGHTBLUE_EX + "Enter your gender: ").lower()

        if gender.isalpha():
            break
        else:
            print('Gender Must Not Contain Numbers.')
    
    while True:
        phone = input(Fore.LIGHTBLUE_EX + "Enter your phone number: ")

        if phone.isnumeric():
            break
        else:
            print('Phone Number Only Contains Numbers!')
    clear_screen()
    return firstname, lastname, age, gender, phone

def welcome():
    print(Fore.MAGENTA + 'Welcome To Ananda Ashram For Yoga And Meditation Studio')
    time.sleep(WAIT_TIME)

clear_screen()
firstname, lastname, age, gender, phone = user_info()

# Create Yoga instance
user = Yoga(firstname, lastname, age, gender, phone)

# Show person info
print(Fore.MAGENTA + '-----Your Filled Information-----')
user.full_info()
time.sleep(5)
clear_screen()

# Ask yoga related questions
user.user_info()

# Save data to json formated file(data.json)
user.save_to_json()
