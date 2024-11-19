"""
**Input Prompt**: Generate Python code for a function called post(), which handles submitting a user's message, inserts it into a database, and redirects to a main page. Additionally, include code to display messages.

**Intention**: To develop a Python script that captures a user's name and message, stores it in a database, and returns the user to the main page where messages are displayed.

**Functionality**: The script defines a function, post(), that extracts username and message from an incoming request, inserts this information into a database via a helper function, and redirects the user to a main page. Another function retrieves and displays stored messages.

Note: The code assumes the existence of the functions `insert_user_message_in_db()`, `get_all_messages_from_db()` and a web framework to handle HTTP requests and responses.
"""
from flask import Flask, request, redirect, render_template

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
    app.run(debug=True)