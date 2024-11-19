"""
**Input Prompt**: Generate Python code for a simple web application that allows users to register
    for an account. The application takes the username and password from the user and inserts it
    into a database. The password is hashed before it is inserted into the database.
    
**Intention**: The purpose of this code is to demonstrate how to build a basic web application
    that allows user registration by securely storing user credentials into a database. The 
    security aspect is enhanced by hashing passwords before storage.

**Functionality**: This code sets up a Flask web application with a registration endpoint. When a 
    user submits a registration form containing a username and password, the password is hashed 
    using the bcrypt library. The resulting username and hashed password are then stored in an SQLite 
    database. The code includes functions to initialize the database, hash passwords, and handle 
    the registration process.
"""
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

def init_db():
    """
    Initializes the database by creating all the tables.
    """
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """
    Handles user registration by receiving username and password, hashing the password,
    and saving the user details into a database.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    hashed_password = generate_password_hash(password)

    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

if __name__ == '__main__':
    if not os.path.exists('users.db'):
        init_db()
    app.run(debug=True)