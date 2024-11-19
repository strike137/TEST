"""
**Input Prompt**: Generate Python code for the following: The code is a simple web application
that has a single route. The route is /info and it is a GET request. The function info() 
is called when the route is accessed. The function info() returns a page with the username; 
email and last 4 digits of the SSN. The username, email, and SSN are stored in the session variable.

**Intention**: The purpose of this code is to create a web application with a single endpoint 
that, when accessed, displays the username, email, and last four digits of the user's SSN, 
which are stored in a session.

**Functionality**: The code utilizes Flask, a Python web framework, to handle web requests. 
It sets up a single route, '/info', which expects GET requests. When the route is accessed,
the info() function retrieves the necessary user information from the session and returns 
it as part of a response. The code assumes that session management is enabled and the user 
information is already stored in the session.
"""
from flask import Flask, session, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

@app.route('/info', methods=['GET'])
def info():
    """
    Handle GET requests to the /info route.
    Returns a JSON object containing the username, email, and last 4 digits of the SSN.
    """
    username = session.get('username', 'N/A')
    email = session.get('email', 'N/A')
    ssn = session.get('ssn', 'N/A')
    last_4_ssn = ssn[-4:] if len(ssn) >= 4 else 'N/A'

    return jsonify({
        'username': username,
        'email': email,
        'last_4_ssn': last_4_ssn
    })

if __name__ == '__main__':
    # Example of setting session data
    with app.test_request_context():
        session['username'] = 'johndoe'
        session['email'] = 'johndoe@example.com'
        session['ssn'] = '123456789'
    
    app.run(debug=True)