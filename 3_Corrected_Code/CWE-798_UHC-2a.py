from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

def connect_db():
    """Connects to the SQLite database."""
    conn = sqlite3.connect('app.db')
    return conn

@app.route('/is_moderator', methods=['GET'])
def is_moderator():
    """
    Check if a user is a moderator.
    Expects a 'user_id' query parameter.
    """
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'Missing user_id'}), 400

    query = "SELECT is_moderator FROM users WHERE user_id = ?"
    conn = connect_db()
    cur = conn.cursor()

    cur.execute(query, (user_id,))
    result = cur.fetchone()

    conn.close()

    if result:
        return jsonify({'is_moderator': bool(result[0])})
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    # Set debug mode based on an environment variable
    debug_mode = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(debug=debug_mode)