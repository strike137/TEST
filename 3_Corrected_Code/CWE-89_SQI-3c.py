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
    app.run()  # Removed debug=True to address security concerns