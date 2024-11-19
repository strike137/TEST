import os
from flask import Flask, request, redirect, url_for, session, render_template_string

app = Flask(__name__)

# Set secret key from environment variable or default to a secure random key
app.secret_key = os.environ.get('FLASK_SECRET_KEY', os.urandom(24))

# Load credentials from environment variables, defaults are omitted for security
VALID_USERNAME = os.environ.get('VALID_USERNAME', '')
VALID_PASSWORD = os.environ.get('VALID_PASSWORD', '')

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

def get_secret_page_content():
    # Encapsulate the secret content in a function to emphasize that it's non-sensitive
    return '''
    <h1>Welcome to the Secret Page</h1>
    <p>Here you can find exclusive content.</p>
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
        return render_template_string(get_secret_page_content())
    return redirect(url_for('login'))

if __name__ == '__main__':
    # Use debug mode conditionally based on environment variable
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode)