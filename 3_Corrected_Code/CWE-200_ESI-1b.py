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
    import os

    # Set the debug mode based on an environment variable
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 'yes']

    app.run(debug=debug_mode)