
from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)

def insert_user_message_in_db(username, message):
    # Dummy implementation of a function to insert message into the database
    pass

def get_all_messages_from_db():
    # Dummy implementation to get all messages from the database
    return [
        {'username': 'Alice', 'message': 'Hello everyone!'},
        {'username': 'Bob', 'message': 'Good to see you all!'}
    ]

@app.route('/post', methods=['POST'])
def post():
    """
    Handles the POST request when a user submits a message.
    
    Extracts username and message from the request, inserts it into the database,
    and redirects the user to the main page.
    """
    username = request.form.get('username')
    message = request.form.get('message')
    # Check if username and message are not None or empty
    if username and message:
        insert_user_message_in_db(username, message)
    return redirect('/')

@app.route('/', methods=['GET'])
def main_page():
    """
    Renders the main page displaying all the user messages.
    """
    messages = get_all_messages_from_db()
    return render_template('main.html', messages=messages)

if __name__ == '__main__':
    # Only enable debug mode if the environment is set to development
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=debug_mode)
