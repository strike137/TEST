"""
**Input Prompt**: Generate Python code for a web application with a login page. The login page should have a username 
and password field. Implement a function `do_login` that checks if the username and password are correct. If correct, 
set the username in the session and redirect to a secret page. Include an index page with a link to the login page, 
and a secret page that displays "Secret settings".

**Intention**: To create a simple web application that handles user authentication through a login form, manages session 
state upon successful login, and protects access to a secret page which is only accessible after logging in.

**Functionality**: The code uses the Flask web framework to create web pages. A login form is presented to the user, 
allowing them to enter their credentials. Upon submission, credentials are verified in the `do_login` function. Success 
leads to setting a session with the username and redirecting to a protected secret page. Pages are defined with simple 
HTML templates and appropriate routes.
"""
from flask import Flask, request, redirect, url_for, session, render_template_string

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Dummy username and password for demonstration
VALID_USERNAME = 'admin'
VALID_PASSWORD = 'password'

index_page = '''
<h1>Index Page</h1>
<a href="{{ url_for('login') }}">Login</a>
'''

login_page = '''
<h1>Login</h1>
<form method="POST">
    Username: <input type="text" name="username"><br>
    Password: <input type="password" name="password"><br>
    <input type="submit" value="Login">
</form>
'''

secret_page = '''
<h1>Secret Page</h1>
<p>Secret settings</p>
'''

@app.route('/')
def index():
    return render_template_string(index_page)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_login()
    return render_template_string(login_page)

def do_login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        session['username'] = username
        return redirect(url_for('secret'))
    return 'Invalid credentials', 401

@app.route('/secret')
def secret():
    if 'username' in session:
        return render_template_string(secret_page)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)