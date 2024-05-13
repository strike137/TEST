import mysql.connector

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    try:
        # Modify the following parameters according to your MySQL server configuration
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="your_database"
        )
        print("Connection established successfully!")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
