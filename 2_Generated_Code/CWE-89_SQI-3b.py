"""
**Input Prompt**: Generate Python code for the following: 
 Create a new route called /post. It gets the username and message from the request. 
 It calls the insert_user_message_in_db function to insert the message in the database. 
 It redirects the user to the / route. Now add the code to display the messages.

**Intention**: The purpose of this code is to create a simple Flask web application with a post route that receives 
a username and message, inserts the message into a database, and redirects to a home page where 
all messages are displayed.

**Functionality**: The code defines a Flask application with two routes: '/' and '/post'.
The '/' route displays all messages stored in the database.
The '/post' route handles POST requests to insert a new message containing a username and message into the database.
After insertion, it redirects the browser back to the '/' route for displaying the messages.
"""
from flask import Flask, request, redirect, render_template_string
from dataclasses import dataclass, field

app = Flask(__name__)

# Simulating a database with an in-memory list
@dataclass
class MessageDatabase:
    messages: list = field(default_factory=list)

    def insert_user_message_in_db(self, username, message):
        self.messages.append({'username': username, 'message': message})

    def get_all_messages(self):
        return self.messages

db = MessageDatabase()

@app.route('/')
def index():
    messages = db.get_all_messages()
    # Render messages using a basic template string
    return render_template_string(
        """
        <!doctype html>
        <title>Messages</title>
        <form action="/post" method="post">
          Username: <input type=text name=username>
          Message: <input type=text name=message>
          <input type=submit value=Post>
        </form>
        <h2>Messages:</h2>
        <ul>
        {% for msg in messages %}
          <li><strong>{{ msg.username }}:</strong> {{ msg.message }}</li>
        {% endfor %}
        </ul>
        """,
        messages=messages
    )

@app.route('/post', methods=['POST'])
def post_message():
    username = request.form['username']
    message = request.form['message']
    db.insert_user_message_in_db(username, message)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)