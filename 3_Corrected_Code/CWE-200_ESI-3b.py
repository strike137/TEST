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
    # Avoid using debug=True in a production environment
    app.run()