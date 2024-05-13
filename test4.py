import mysql.connector

def getDBConnection():
    # Specify your database credentials
    config = {
        'user': 'your_username',
        'password': 'your_password',
