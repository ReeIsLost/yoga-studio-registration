# 🧘‍♀️ Ananda Ashram Yoga & Meditation CLI

A simple **command-line application** that helps users register at **Ananda Ashram Yoga Studio**, track their yoga practice, and save their progress to a JSON file.  

This project demonstrates **object-oriented programming (OOP)** in Python with classes, inheritance, input validation, and file handling.

---

## 📁 Project Structure

├── main.py # Entry point – handles user input and program flow
├── person.py # Defines the Person class (basic user information)
├── yoga.py # Defines the Yoga class (extends Person with yoga-related logic)
├── data.json # (Auto-generated) Stores saved user data
└── README.md # Project documentation

---

## 🚀 Features

✅ Collects and validates user information (name, age, gender, phone)  
✅ Offers interactive questions about yoga experience  
✅ Displays a color-coded yoga style selection menu  
✅ Records finished yoga sessions  
✅ Automatically determines your yoga level (Beginner, Intermediate, Instructor)  
✅ Saves user data to a **JSON file**  
✅ Includes helpful screen-clearing and colorized text for clean CLI experience  

---

## 🧩 How It Works

1. Run the program (`python main.py`).
2. Enter your personal information (name, age, gender, phone).
3. Answer whether you have done yoga before:
   - **Yes** → record previously completed yoga styles.
   - **No** → explore new yoga styles from the menu.
4. Your information and yoga progress are saved to `data.json`.

---

## 💻 Requirements

- Python 3.8 or higher  
- Dependencies:
  ```bash
  pip install colorama
▶️ How to Run
Clone this repository:

bash
Copy code
git clone https://github.com/ReeIsLost/ananda-yoga-cli.git
cd ananda-yoga-cli
Run the program:

bash
Copy code
python main.py
Follow the on-screen prompts.

🧠 Example Interaction
yaml
Copy code
Welcome To Ananda Ashram For Yoga And Meditation Studio
Enter your first name: Sarah
Enter your last name: Jones
Enter your age: 29
Enter your gender: Female
Enter your phone number: 5551234567

-----Your Filled Information-----
FirstName: Sarah
LastName: Jones
Age: 29
Gender: Female
Phone Number: 5551234567

Have you done Yoga before? (Yes / No): no

What Would You Like To Learn?
[1] Hatha Yoga
[2] Vinyasa Yoga
[3] Ashtanga Yoga
[4] Bikram Yoga
[5] Yin Yoga
[6] Exit
[+] Enter Your Option: 1
Selected Yoga: Hatha Yoga
🗂️ Data Storage Example (data.json)
json
Copy code
[
    {
        "First Name": "Sarah",
        "Last Name": "Jones",
        "Age": 29,
        "Gender": "Female",
        "Phone Number": "5551234567",
        "Level": "Beginner",
        "Learning Yoga": ["Hatha Yoga"],
        "Finished Yoga": []
    }
]
🧱 Object-Oriented Design
Person → Handles personal data

Yoga(Person) → Inherits from Person, adds yoga features (menu, progress, saving)

⚖️ License
This project is not licensed.
All rights reserved. You may not copy, modify, or distribute this code without explicit permission from the author.
