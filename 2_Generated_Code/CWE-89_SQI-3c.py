"""
**Input Prompt**: The task is to generate Python code that defines a function called post() to handle user-submitted messages. It should extract the username and message from the request, use a helper function to insert this data into a database, and then redirect the user back to the main page. Additionally, a form needs to be added to the main page for user message submissions.

**Intention**: The purpose of this code is to facilitate the process of submitting user messages through a web application. It inserts the messages into a database and handles redirection to ensure seamless user interaction.

**Functionality**: The code employs a Flask web application framework. The post() function captures the username and message from an HTTP POST request, calls another function to save this data to a database, and redirects the user back to the main page. The HTML portion includes a form to send username and message data to the server.
"""
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

def insert_user_message_in_db(username, message):
    """
    Placeholder function to simulate database insertion.
    """
    # Insert logic to insert the user message into the database here
    print(f"Inserted into DB: {username} - {message}")

@app.route('/', methods=['GET'])
def main_page():
    """
    Render the main page with a submission form.
    """
    html_content = """
    <h1>Message Board</h1>
    <form action="/post" method="post">
        Username: <input type="text" name="username"><br>
        Message: <textarea name="message"></textarea><br>
        <input type="submit" value="Submit">
    </form>
    """
    return render_template_string(html_content)

@app.route('/post', methods=['POST'])
def post():
    """
    Handle the post request by extracting user data and storing it in the database.
    Redirect to the main page after successful insertion.
    """
    username = request.form.get('username')
    message = request.form.get('message')
    insert_user_message_in_db(username, message)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)