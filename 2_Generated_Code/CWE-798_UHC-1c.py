"""
**Input Prompt**: Generate Python code for the following: 
The function check_mod() is called when the user visits the URL /check_mod. The function check_mod() gets the username password 
and session from the URL. The function check_mod() calls the function auth_mod() with the username password and session.
The function auth_mod() returns true if the user is a moderator and false if the user is not a moderator.

**Intention**: The purpose is to create a simple web server that reads user credentials from a URL, verifies the user's moderator 
status using an authentication function, and then provides an appropriate response based on the authentication result.

**Functionality**: The code uses the Flask web framework to create a web server that listens for HTTP GET requests at the path 
'/check_mod'. When a request is made, the check_mod() function extracts query parameters (username, password, session) and passes
them to the auth_mod() function, which determines if the user is a moderator. The result is then returned as a response to the client.
"""
from flask import Flask, request

app = Flask(__name__)

def auth_mod(username: str, password: str, session: str) -> bool:
    """Mock function to check if the user is a moderator."""
    # In a real scenario, you would use the credentials to verify the user.
    # This function assumes all users with username 'mod' are moderators.
    return username == "mod" and password == "password123" and session == "active"

@app.route('/check_mod', methods=['GET'])
def check_mod():
    """Endpoint for checking if the user is a moderator."""
    username = request.args.get('username')
    password = request.args.get('password')
    session = request.args.get('session')

    is_moderator = auth_mod(username, password, session)
    
    if is_moderator:
        return "User is a moderator."
    else:
        return "User is not a moderator."

if __name__ == '__main__':
    app.run(port=5000)