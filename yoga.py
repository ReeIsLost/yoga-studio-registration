import time
import json
import os
from person import Person
from colorama import Fore, Back, Style, init

class Yoga(Person):
    WAIT_TIME = 1
    init(autoreset=True)

    yoga_plain_dict = {
    '1': 'Hatha Yoga',
    '2': 'Vinyasa Yoga',
    '3': 'Ashtanga Yoga',
    '4': 'Bikram Yoga',
    '5': 'Yin Yoga',
    '6': 'Exit'
    }
    
    yoga_menu_dict = {
    '1': Fore.MAGENTA + '[1] Hatha Yoga' + Style.RESET_ALL,
    '2': Fore.MAGENTA + '[2] Vinyasa Yoga' + Style.RESET_ALL,
    '3': Fore.MAGENTA + '[3] Ashtanga Yoga' + Style.RESET_ALL,
    '4': Fore.MAGENTA + '[4] Bikram Yoga' + Style.RESET_ALL,
    '5': Fore.MAGENTA + '[5] Yin Yoga' + Style.RESET_ALL,
    '6': Fore.MAGENTA + '[6] Exit' + Style.RESET_ALL
    }
    
    def __init__(self, firstname, lastname, age, gender, phonenumber, level='Beginner'):
        super().__init__(firstname, lastname, age, gender, phonenumber)
        self.level = level
        self.finished_yoga = []
        self.yoga_menu_options = []
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def user_info(self):
        """
        Prompt the user to ask if they have done Yoga before and handle their response

        This method repeatedly asks the user the question: "Have you done Yoga before? (Yes / No)"
        until a valid response is provided. Depending on the user's input:

        - If the input is empty, the screen is cleared and a warning message is shown.
        - If the user answers 'yes', the method calls self.record_finished_yoga() to handle
          finished yoga records.
        - If the user answers 'no', the method calls elf.show_menu() to display the main menu.
        - If the input is anything else, an error message is displayed asking for a valid response.

        The screen is cleared and messages are shown with a small delay by using self.WAIT_TIME.
        """
        while True:
            userinput = input(Fore.MAGENTA + "Have you done Yoga before? (Yes / No): ").lower()

            if userinput == '':
                self.clear_screen()
                print('Information Field Cannot Be Empty!')
                time.sleep(self.WAIT_TIME)
                self.clear_screen()
                continue

            elif userinput == 'yes':
                self.clear_screen()
                self.record_finished_yoga()
                break

            elif userinput == 'no':
                self.show_menu()
                break

            else:
                print('Please Enter Yes Or No Only!!')
                time.sleep(self.WAIT_TIME)
                self.clear_screen()


    def record_finished_yoga(self):
        """
        Prompt the user to enter Yoga practices they have completed and record them

        The user is asked to input all Yoga practices they have done, separated by a '/' character
        Each entry is stripped of leading/trailing whitespace, converted to a list, and appended 
        to the self.finished_yoga list. 

        After recording, the updated list of finished Yoga practices is displayed

        Example:
            Input: "Meditation / Hatha / Vinyasa"
            self.finished_yoga will be extended with ['Meditation', 'Hatha', 'Vinyasa']
        """
        done_yoga = input(Fore.LIGHTCYAN_EX + "Please Enter Yoga You Have Done (Seperate Them With /):\n")
        done_list = [y.strip() for y in done_yoga.split('/')]
        self.finished_yoga.extend(done_list)
        print(Fore.GREEN + "Recorded Yoga:", self.finished_yoga)

    def show_menu(self):
        """
        Display the Yoga menu and allow the user to select one or more Yoga types

        The menu options are taken from self.yoga_menu_dict. The user is prompted to 
        enter the number corresponding to their choice. Each selected Yoga type is 
        added to self.yoga_menu_options and is displayed.

        Special behavior:
        - Entering '6' will exit the menu and display waht the user selected
        - Invalid inputs will prompt the user to try again
    
        The screen is cleared before each menu display, and a short delay is applied
        after valid or invalid selections by self.WAIT_TIME
        """
        while True:
            self.clear_screen()
            print(Fore.LIGHTMAGENTA_EX + 'What Would You Like To Learn?' + Style.RESET_ALL)
            for key, value in self.yoga_menu_dict.items():
                print(f"{value}")

            user_option = input(Fore.LIGHTCYAN_EX + "[+] Enter Your Option: " + Style.RESET_ALL)

            if user_option == '6':
                print(Fore.GREEN + "Selected Yoga:", ', '.join(self.yoga_menu_options))
                break
            elif user_option in self.yoga_plain_dict:
                yoga_choice = self.yoga_plain_dict[user_option]
                if yoga_choice in self.yoga_menu_options:
                    print(Fore.YELLOW + f"You already added {yoga_choice}!")
                else:
                    self.yoga_menu_options.append(yoga_choice)
                    print(Fore.GREEN + "Selected Yoga:", ', '.join(self.yoga_menu_options))
                time.sleep(self.WAIT_TIME)
            else:
                print(Fore.RED + "Not An Option. Please Try Again!")
                time.sleep(self.WAIT_TIME)

    def save_to_json(self, filename='data.json'):
        """
        Save the user's information and yoga progress to json file

        It collects user details such as name, age, gender, phone number,
        current yoga level, current yoga practices, and finished yoga practices

        The user's yoga level is automatically updated based on the number of 
        finished yoga sessions:
            - 3 or more: "Intermediate"
            - 5 or more: "Instructor"
            - Otherwise: "Beginner"

        If the specified json file exists, the new data is appended otherwise, 
        a new file is created. The final data is saved with the user infomation

        Args:
            filename (str): The name of the json file(data.json) to save the data to. 

        Example:
            save_to_json('user_data.json')
        """
        data = {
            'First Name': self.firstname,
            'Last Name': self.lastname,
            'Age': self.age,
            'Gender': self.gender,
            'Phone Number': self.phonenumber,
            'Level': self.level,
            'Learning Yoga': self.yoga_menu_options,
            'Finished Yoga': self.finished_yoga
        }

        # Check How Many Yoga User Has Completed
        finished_yoga_count = len(data["Finished Yoga"])

        # Update User Yoga Level
        if finished_yoga_count >= 3:
            data["Level"] = "Intermediate"
        elif finished_yoga_count >= 5:
            data["Level"] = "Instructor"
        else:
            data["Level"] = "Beginner"
        try:
            with open(filename, 'r') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []
        
        # Add Data
        existing_data.append(data)

        # Save data
        with open(filename, 'w') as file:
            json.dump(existing_data, file, indent=4)
        print(Fore.RED + f'Data Saved To {filename} successfully!')