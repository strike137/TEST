"""
**Input Prompt**: Generate Python code for the following: 
The code is a simple login system that allows a user to change their email. 
The user must be logged in to change their email. The user must also enter their old email and confirm their password. 
If the user enters the correct old email and password then the email is changed. 
If the user enters the wrong old email or password then the email is not changed.

**Intention**: To create a basic authentication and email update system for users, requiring users to be logged in and confirm their old credentials before they update their email address.

**Functionality**: This code defines a simple user login system where:
1. A User class is created with properties for username, email, and password.
2. Users must be logged in before updating their email.
3. The email update requires verification of the current email and password.
4. The email is only updated if the entered credentials are correct.
"""
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.logged_in = False

    def login(self, password):
        """Log in the user if the password matches."""
        if self.password == password:
            self.logged_in = True
            print("Login successful.")
        else:
            print("Incorrect password.")

    def logout(self):
        """Log out the user."""
        self.logged_in = False
        print("Logged out.")

    def change_email(self, old_email, password, new_email):
        """
        Change the email of the user if logged in and the provided 
        old email and password are correct.
        """
        if not self.logged_in:
            print("You must be logged in to change your email.")
            return

        if self.email == old_email and self.password == password:
            self.email = new_email
            print("Email changed successfully.")
        else:
            print("Incorrect email or password. Email not changed.")

# Example Usage
user = User(username="john_doe", email="john@example.com", password="securepassword")

# User attempts to change email without logging in
user.change_email(old_email="john@example.com", password="securepassword", new_email="john.doe@example.com")

# User logs in
user.login(password="securepassword")

# User changes email with correct old email and password
user.change_email(old_email="john@example.com", password="securepassword", new_email="john.doe@example.com")

# User logs out
user.logout()

# Attempt to change email after logging out
user.change_email(old_email="john.doe@example.com", password="securepassword", new_email="johnny.doe@example.com")