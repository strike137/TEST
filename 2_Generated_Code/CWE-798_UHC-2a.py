"""
**Input Prompt**: Generate Python code for the following: 
Create a web app. Define a route for the app. Define a function that will be called 
when the route is called. Connect to the database. Execute a query to check if the 
user is a moderator. Return the result of the query.
**Intention**: The purpose of this code is to set up a simple web application using 
Flask that can handle HTTP requests by defining a specific route. Upon hitting this 
route, the app will connect to a database and execute a query to determine if the 
requesting user is a moderator, then return the query result.
**Functionality**: The code initializes a Flask application, sets up a route, and 
defines an associated function that is responsible for connecting to a database. 
Within this function, a query is executed to check the moderation status of a user 
retrieved possibly from a query parameter, and the result of whether the user is a 
moderator is returned as an HTTP response.
"""
from flask import Flask, request, jsonify
import sqlite3

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
    app.run(debug=True)