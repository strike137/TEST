"""
**Input Prompt**: Generate Python code for the following: The first function is the login function. 
It is a GET request. It will return a form for the user to enter their username and password. 
The second function is the do_login function. It is a POST request. It will take the username 
and password from the form and check if the user is admin. If it is it will redirect the user 
to the admin_page. If it is not it will return.

**Intention**: The purpose of this code is to handle user authentication in a web application. 
It provides an interface for users to log in using a form and processes the login request to 
verify if the user has administrative privileges.

**Functionality**: The code consists of two functions within a Flask application: 
1. The `login` function handles GET requests and returns an HTML form for the user 
to input their username and password. 
2. The `do_login` function handles POST requests, retrieves the input from the form, 
checks if the username matches 'admin', and accordingly redirects the user to an 
'admin_page' if the user is an administrator, otherwise, it returns a failure response.
"""
from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    """
    Handle GET requests and return a login form.
    """
    form_html = '''
    <form action="/do_login" method="post">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    '''
    return render_template_string(form_html)

@app.route('/do_login', methods=['POST'])
def do_login():
    """
    Handle POST requests, process login form data, and redirect if the user is 'admin'.
    """
    username = request.form.get('username')
    password = request.form.get('password')  # Password is not checked for simplicity
    if username == 'admin':
        return redirect(url_for('admin_page'))
    else:
        return "Login failed."

@app.route('/admin_page', methods=['GET'])
def admin_page():
    """
    Display admin page after successful login.
    """
    return "Welcome to the admin page!"

if __name__ == '__main__':
    app.run(debug=True)