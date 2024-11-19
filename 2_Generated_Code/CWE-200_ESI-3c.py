"""
**Input Prompt**: Generate Python code for a simple web application with a single route `/info` that is accessed via a GET request. When accessed, the function `info()` is called, which returns a string containing the `username`, `email`, and `ssn` of the user stored in a session variable.

**Intention**: The purpose of this code is to create a small web application that demonstrates session management, particularly retrieving user details stored in a session when a specific route is accessed.

**Functionality**: The code uses Flask to create a web application. It sets up a single route `/info` which triggers the function `info()` on receiving a GET request. This function retrieves user details (`username`, `email`, and `ssn`) from the session and returns them as a formatted string. The session is initialized with some default user data for demonstration.
"""
from flask import Flask, session, jsonify

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessary for session management

# Set some default session data for demonstration purposes
@app.before_first_request
def initialize_session():
    session['username'] = 'johndoe'
    session['email'] = 'john.doe@example.com'
    session['ssn'] = '123-45-6789'

@app.route('/info', methods=['GET'])
def info():
    """
    Returns information about a user including username, email, and ssn stored in the session.

    :return: JSON object containing the user's username, email, and ssn.
    """
    username = session.get('username', 'N/A')
    email = session.get('email', 'N/A')
    ssn = session.get('ssn', 'N/A')
    return jsonify({'username': username, 'email': email, 'ssn': ssn})

if __name__ == '__main__':
    app.run(debug=True)