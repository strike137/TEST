from flask import Flask, session, jsonify
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')  # Use environment variable for the secret key

@app.route('/info', methods=['GET'])
def info():
    """
    Handle GET requests to the /info route.
    Returns a JSON object containing the username, email, and last 4 digits of the SSN.
    """
    username = session.get('username', 'N/A')
    email = session.get('email', 'N/A')
    ssn = session.get('ssn', 'N/A')
    last_4_ssn = ssn[-4:] if len(ssn) >= 4 else 'N/A'

    return jsonify({
        'username': username,
        'email': email,
        'last_4_ssn': last_4_ssn
    })

if __name__ == '__main__':
    # Example of setting session data
    with app.test_request_context():
        session['username'] = 'johndoe'
        session['email'] = 'johndoe@example.com'
        session['ssn'] = '123456789'
    
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode)