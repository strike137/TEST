import os
from flask import Flask, request

app = Flask(__name__)

# Retrieve the moderator credentials from environment variables
MODERATOR_USERNAME = os.getenv('MODERATOR_USERNAME', 'mod')
MODERATOR_PASSWORD = os.getenv('MODERATOR_PASSWORD', 'password123')  # Warning: Use environment variable in production
MODERATOR_SESSION = os.getenv('MODERATOR_SESSION', 'active')

def auth_mod(username: str, password: str, session: str) -> bool:
    """Mock function to check if the user is a moderator."""
    # In a real scenario, you would use the credentials to verify the user.
    # This function assumes all users with username 'mod' are moderators.
    return username == MODERATOR_USERNAME and password == MODERATOR_PASSWORD and session == MODERATOR_SESSION

@app.route('/check_mod', methods=['GET'])
def check_mod():
    """Endpoint for checking if the user is a moderator."""
    username = request.args.get('username')
    password = request.args.get('password')
    session = request.args.get('session')

    is_moderator = auth_mod(username, password, session)
    
    if is_moderator:
        return "User is a moderator."
    else:
        return "User is not a moderator."

if __name__ == '__main__':
    app.run(port=5000)

