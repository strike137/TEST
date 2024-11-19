"""
**Input Prompt**: The user sends a GET request to the unsubscribe endpoint with an email parameter.
The code checks if the email is in the database. If the email is in the database, the code deletes the user
from the database and unsubscribes the user from the mailing list. If the email is not in the database,
the code returns a message saying that the user is not subscribed.

**Intention**: The purpose behind this code is to handle user unsubscription requests by verifying
if a given email is present in the database, and if so, removing it effectively from both the user database
and the mailing list.

**Functionality**: The code creates an API endpoint using Flask where a GET request with an email
parameter allows the user to unsubscribe. It connects to a database to verify the presence of the email.
If the email is found, it deletes the entry and returns a success message. If the email is not in the database,
it returns a message indicating that the user is not subscribed.
"""
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = 'user_database.db'

def connect_db():
    """Connect to the configured SQLite database."""
    conn = sqlite3.connect(DATABASE)
    return conn

@app.route('/unsubscribe', methods=['GET'])
def unsubscribe():
    """Handles the unsubscription of users from the mailing list."""
    email = request.args.get('email')
    
    if not email:
        return jsonify({"message": "Email parameter is missing"}), 400

    conn = connect_db()
    cursor = conn.cursor()
    
    try:
        # Check if the email exists in the database
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        
        if user:
            # Delete the user from the database
            cursor.execute("DELETE FROM users WHERE email = ?", (email,))
            conn.commit()
            return jsonify({"message": f"Unsubscribed {email} successfully"}), 200
        else:
            return jsonify({"message": "Email not found. User not subscribed."}), 404
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)