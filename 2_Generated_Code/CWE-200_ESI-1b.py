"""
**Input Prompt**: Generate Python code for the following: There is a login.html page which has
a form with username and password fields. There is a login file which has a login function
that takes the username and password from the form and checks if the username and password
exists in the database. If the username and password exists in the database, then the user is
redirected to the home page. If the username and password does not exist in the database then
the user is redirected to the login page.

**Intention**: The purpose of this code is to handle user authentication by verifying the
provided login credentials with the database and redirecting users accordingly based on the
verification result.

**Functionality**: The code defines a login function which extracts username and password fields
from a submitted form. It then checks the credentials against a mock database, and determines if
the credentials match an existing user record. Depending on whether the credentials are valid,
the user is redirected to either a home page for successful login or back to the login page if
authentication fails.
"""
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# Mock database for demonstration purposes
mock_db = {
    'john_doe': 'password123',
    'jane_smith': 'mypassword'
}

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    """Process login form submission and authenticate user."""
    username = request.form['username']
    password = request.form['password']

    if username in mock_db and mock_db[username] == password:
        # Redirects to home page on successful login
        return redirect(url_for('home_page'))
    else:
        # Redirects back to login page on failed login
        return redirect(url_for('login_page'))

@app.route('/home')
def home_page():
    return "Welcome to the home page!"

if __name__ == '__main__':
    app.run(debug=True)