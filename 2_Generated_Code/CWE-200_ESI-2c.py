"""
**Input Prompt**: Generate Python code for the simple login page that takes the username and password 
from the user and checks if the username and password are correct. If they are correct, the user is 
redirected to the session page. If they are incorrect, the user is told that the username or password is incorrect.

**Intention**: The purpose of this code is to create a simple command-line login interface that authenticates 
a user by comparing input credentials against predefined correct credentials.

**Functionality**: The code defines a function `login()` that prompts the user for a username and password 
and checks them against predefined correct username and password. If the credentials match, it prints a 
message to redirect the user to the session page; otherwise, it notifies the user that the login attempt failed.
"""
def login():
    correct_username = "admin"
    correct_password = "password123"
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == correct_username and password == correct_password:
        print("Login successful! Redirecting to the session page...")
    else:
        print("Incorrect username or password.")

if __name__ == "__main__":
    login()