🔐 Password Strength Evaluator

This is the first project in a cybersecurity roadmap, designed to help beginners understand fundamental security concepts through practical application. This tool, built in Python, evaluates the strength of a password by calculating its entropy and providing a simple strength rating.


✨ Features

Entropy Calculation: Determines the randomness of a password in bits, a key metric for security.
Strength Rating: Provides a clear rating (e.g., "Weak," "Strong") based on the calculated entropy.
Simple Command-Line Interface (CLI): Easy to use for quick checks.


💻 How It Works

The tool uses a simple but effective formula to calculate password entropy:
L is the length of the password.
C is the size of the character set used (e.g., lowercase letters, uppercase letters, numbers, special characters).
By calculating this value, the script can provide an objective measure of how difficult a password would be to crack via a brute-force attack.

🚀 Getting Started

Prerequisites
Python 3.x installed on your machine.

Installation
Clone this repository or download the password_checker.py file.
Open your terminal or command prompt.
Navigate to the directory where the file is saved.
Usage
Run the script from your terminal:
python password_checker.py
The script will prompt you to enter a password. After you type it in and press Enter, it will display the password's length, entropy, and strength rating.


📄 Terminology
Entropy: A measure of a password's randomness and unpredictability. Higher entropy means a more secure password.
Brute-Force Attack: A method of cracking a password by trying every possible combination of letters, numbers, and symbols until the correct one is found.
Character Set: The collection of all possible characters that could be used in a password (e.g., a-z, A-Z, 0-9, special characters).


💡 Next Steps

This project can be extended with the following features to make it a more robust tool:
Estimated Crack Time: Calculate and display an estimated time to crack the password based on current technology.
Secure Password Suggestions: Generate and suggest secure, high-entropy passwords.
GUI (Graphical User Interface): Create a more user-friendly interface using a library like Tkinter or PyQt.
Password Policies: Implement checks against common password policies (e.g., minimum length, required character types).
