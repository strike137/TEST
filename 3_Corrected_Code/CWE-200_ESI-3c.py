import os
from flask import Flask, session, jsonify

app = Flask(__name__)

# Generate a secure secret key for session management
app.secret_key = os.urandom(24)

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
    # Do not enable debug mode in production
    app.run()