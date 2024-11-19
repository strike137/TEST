"""
**Input Prompt**: Generate Python code for the following:
The first function is the login function. It is a GET request.
The second function is the do_login function. It is a POST request.
The third function is the index function. It is a GET request.
The fourth function is the user_page function. It is a GET request.
The fifth function is the admin_page function. It is a GET request.

**Intention**: 
The intention is to create a simple web application using Flask with specific routes representing different pages or actions such as login and accessing different pages based on user roles (user or admin).

**Functionality**:
The code uses the Flask framework to set up a web server with five endpoints. Each function corresponds to a route with specified HTTP methods:
- `/login` corresponds to a GET request handled by `login()`.
- `/do_login` corresponds to a POST request handled by `do_login()`.
- `/` (home page) corresponds to a GET request handled by `index()`.
- `/user` corresponds to a GET request handled by `user_page()`.
- `/admin` corresponds to a GET request handled by `admin_page()`.
"""
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

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
    if username == 'admin' and password == 'secret':
        return redirect(url_for('admin_page'))
    elif username == 'user' and password == 'password':
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
    app.run(debug=True)