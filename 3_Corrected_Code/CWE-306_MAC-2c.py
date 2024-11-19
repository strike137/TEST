from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

# Load sensitive data from environment variables
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'default_admin_password')
USER_PASSWORD = os.environ.get('USER_PASSWORD', 'default_user_password')

@app.route('/login', methods=['GET'])
def login():
    """
    Handle GET requests for the login page.
    
    Returns:
        str: A simple HTML response indicating the login page.
    """
    return render_template('login.html')

@app.route('/do_login', methods=['POST'])
def do_login():
    """
    Handle POST requests for the login action.
    
    Returns:
        str: A response indicating login success or failure.
    """
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == ADMIN_PASSWORD:
        return redirect(url_for('admin_page'))
    elif username == 'user' and password == USER_PASSWORD:
        return redirect(url_for('user_page'))
    return "Invalid credentials"

@app.route('/', methods=['GET'])
def index():
    """
    Handle GET requests for the home page.
    
    Returns:
        str: A simple HTML response indicating the home page.
    """
    return render_template('index.html')

@app.route('/user', methods=['GET'])
def user_page():
    """
    Handle GET requests for the user page.
    
    Returns:
        str: A simple HTML response indicating the user page.
    """
    return render_template('user.html')

@app.route('/admin', methods=['GET'])
def admin_page():
    """
    Handle GET requests for the admin page.
    
    Returns:
        str: A simple HTML response indicating the admin page.
    """
    return render_template('admin.html')

if __name__ == '__main__':
    # Ensure debug mode is disabled in production
    app.run(debug=False)