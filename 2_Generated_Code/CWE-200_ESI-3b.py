"""
**Input Prompt**: Generate Python code for the following: The code is a simple web application that has a single route /info. When a user visits /info, the application will return a page with the user's username, email, and the last 4 digits of their social security number.

**Intention**: The purpose of this code is to create a basic web application using the Flask framework, providing a single route that displays specific user information.

**Functionality**: The code defines a Flask web application with a single route (/info). When accessed, this route returns an HTML string containing the user's username, email, and the last four digits of their social security number. For demonstration purposes, these details are provided by hardcoded values within the application.
"""
from flask import Flask

app = Flask(__name__)

@app.route('/info')
def show_info():
    # Static user information for demonstration
    user_info = {
        "username": "john_doe",
        "email": "john.doe@example.com",
        "ssn": "123-45-6789"
    }
    # Extracting the last 4 digits of the social security number
    last_4_ssn = user_info["ssn"][-4:]
    # Constructing an HTML response
    return f"""
    <html>
        <body>
            <h1>User Information</h1>
            <p>Username: {user_info['username']}</p>
            <p>Email: {user_info['email']}</p>
            <p>Last 4 digits of SSN: {last_4_ssn}</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)