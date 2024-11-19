from flask import Flask, request, render_template_string, redirect, url_for
import os

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
        return redirect(url_for('login'))  # Redirect to login page on failure

@app.route('/admin_page', methods=['GET'])
def admin_page():
    """
    Display admin page after successful login.
    """
    return "Welcome to the admin page!"

if __name__ == '__main__':
    # Check for an environment variable to determine if it's a development environment
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug_mode)