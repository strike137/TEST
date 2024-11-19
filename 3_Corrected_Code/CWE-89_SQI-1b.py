from flask import Flask, request, jsonify
import sqlite3
import os

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
    # Set debug mode based on an environment variable
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() in ['true', '1', 'yes']
    app.run(debug=debug_mode)