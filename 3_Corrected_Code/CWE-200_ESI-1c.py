"""
**Input Prompt**: Generate Python code for user login functionality where a username and a password are entered by the user, and the login function checks their credentials against a database to validate access. If the credentials are correct, the user is redirected; otherwise, access is denied.

**Intention**: The purpose of this code is to authenticate users based on their username and password by checking these credentials against a stored database and directing them based on the result of this validation.

**Functionality**: The code includes a simulated login function that:
- Receives a username and a password.
- Checks the database (simulated with a dictionary) for the existence of the username.
- Validates the provided password against the stored password.
- Redirects to a home page if the credentials are correct.
- Provides feedback if the credentials are incorrect.
"""

def load_user_database():
    """
    Simulates loading the user database securely.

    Returns:
        dict: A dictionary representing the user database with usernames and passwords.
    """
    # Users and their encrypted passwords (simulated)
    return {
        "john_doe": "secure123",  # These would ideally be securely hashed
        "jane_smith": "password456"
    }

def login(username, password):
    """
    Authenticates a user based on a username and password.

    Args:
        username (str): The username entered by the user.
        password (str): The password entered by the user.

    Returns:
        str: A message indicating the success or failure of the login attempt.
    """
    user_database = load_user_database()
    
    # Check if the username exists in the database
    if username in user_database:
        # Check if the entered password matches the password in the database
        if user_database[username] == password:
            return "Redirecting to the home page..."
        else:
            return "Incorrect password. Access denied."
    else:
        return "Username not found. Access denied."

# Example usage (this would be replaced with real input in an actual application)
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")
print(login(username_input, password_input))