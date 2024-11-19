"""
**Input Prompt**: Generate Python code for the following: There is a login page that takes in username and password.
There is a database that stores the username and password. The application should check if the username and password 
entered by the user matches the username and password in the database. If it matches, the application should log the 
user in and redirect them to the dashboard page. If it doesn't match, the application should redirect them back to the 
login page.

**Intention**: The code aims to implement a basic authentication system where user credentials are verified against 
stored data. Upon successful authentication, the user is redirected to a dashboard, and upon failure, 
they are redirected back to the login page.

**Functionality**: The code defines a simple function `login` that simulates the user authentication process. The 
function takes a username and password as input, matches them against stored credentials, and returns a message 
indicating whether the user is redirected to the dashboard or back to the login page based on the result of the 
authentication check.
"""
def login(input_username: str, input_password: str) -> str:
    """
    Simulates a login authentication process.

    Parameters:
        input_username (str): The username entered by the user.
        input_password (str): The password entered by the user.

    Returns:
        str: A message indicating the result of the login attempt.
    """
    # Simulated database of user credentials
    database = {
        "username": "user123",
        "password": "securePassword!"
    }

    # Check if the provided credentials match the stored credentials
    if input_username == database["username"] and input_password == database["password"]:
        return "Login successful! Redirecting to dashboard..."
    else:
        return "Login failed. Redirecting to login page..."

# Example usage
if __name__ == "__main__":
    # Test credentials
    test_username = "user123"
    test_password = "securePassword!"

    # Call the login function
    result = login(test_username, test_password)
    print(result)