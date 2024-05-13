import mysql.connector

def getDBConnection():
    # Establishing a connection to the MySQL database
    try:
        connection = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password",
            database="your_database"
        )
        print("Connected to MySQL database")
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

# Example usage:
# connection = getDBConnection()
# if connection:
#     # Proceed with database operations
#     pass
