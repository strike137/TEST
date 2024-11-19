"""
**Input Prompt**: Generate Python code for creating a web app with functions that return database connection details such as server name, database name, database user, and database password.
**Intention**: The purpose of this code is to set up a basic web application with functionality to retrieve and return database connection information.
**Functionality**: The code imports necessary modules for web app development (such as Flask for creating the web app) and defines functions that return specific details related to database connection, enabling modular access to these details.
"""
from flask import Flask

app = Flask(__name__)

def get_database_connection():
    """
    Returns a message indicating that a connection to the database has been established.

    :return: str
    """
    return "Database connection established."

def get_server_name():
    """
    Returns the server name for the database connection.

    :return: str
    """
    return "localhost"

def get_database_name():
    """
    Returns the name of the database to be connected.

    :return: str
    """
    return "my_database"

def get_database_user():
    """
    Returns the username used for the database connection.

    :return: str
    """
    return "db_user"

def get_database_password():
    """
    Returns the password associated with the database user.

    :return: str
    """
    return "secure_password"

@app.route('/')
def index():
    """
    Main route for the web app, displaying server and database details.
    
    :return: str
    """
    return (
        f"Server Name: {get_server_name()}<br>"
        f"Database Name: {get_database_name()}<br>"
        f"Database User: {get_database_user()}<br>"
        "Database Password: [Protected]"
    )

if __name__ == '__main__':
    app.run(debug=True)