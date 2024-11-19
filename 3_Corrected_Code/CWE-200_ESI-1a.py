import os

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
    # Sensitive information like passwords should be stored securely, not hardcoded
    saved_username = os.getenv("USERNAME")
    saved_password = os.getenv("PASSWORD")

    # Check if the provided credentials match the stored credentials
    if saved_username is None or saved_password is None:
        return "Configuration error: username or password not set."

    if input_username == saved_username and input_password == saved_password:
        return "Login successful! Redirecting to dashboard..."
    else:
        return "Login failed. Redirecting to login page..."

# Example usage
if __name__ == "__main__":
    # Assume environment variables are set outside of this script

    # Test credentials
    test_username = os.getenv("USERNAME")
    test_password = os.getenv("PASSWORD")

    # Check if environment variables are set for testing
    if test_username is None or test_password is None:
        print("Environment variables for test credentials are not set.")
    else:
        # Call the login function
        result = login(test_username, test_password)
        print(result)