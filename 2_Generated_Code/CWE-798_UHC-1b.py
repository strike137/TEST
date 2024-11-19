"""
**Input Prompt**: Generate Python code for a function named check_mod() which is triggered by visiting the URL /check_mod. This function should retrieve the username and password from the URL query parameters, verify their correctness, and return 'true' if they match the expected credentials.

**Intention**: The purpose of this code is to implement a simple web service function that authenticates users based on provided URL query parameters, specifically checking the username and password for verification.

**Functionality**: The code defines a Flask web application with a route /check_mod. When this route is accessed, the check_mod() function is invoked. The function retrieves the 'username' and 'password' from the request's query parameters, compares them with hardcoded valid credentials, and returns 'true' if they match.
"""
from flask import Flask, request

app = Flask(__name__)

# Define a route for the URL '/check_mod'
@app.route('/check_mod', methods=['GET'])
def check_mod():
    # Retrieve the username and password from query parameters
    username = request.args.get('username')
    password = request.args.get('password')
    
    # Define the expected credentials
    valid_username = 'admin'
    valid_password = 'password123'
    
    # Check if username and password are correct
    if username == valid_username and password == valid_password:
        return 'true'
    else:
        return 'false'

# Run the app
if __name__ == '__main__':
    app.run(debug=True)