import mysql.connector
from mysql.connector import Error
import re

def insert_image(image_path, host, database, user, password, table_name):
    """
    Inserts an image into a MySQL database table.
    
    :param image_path: Path to the image file to be inserted.
    :param host: Host of the MySQL database.
    :param database: Name of the MySQL database.
    :param user: Username for the MySQL database.
    :param password: Password for the MySQL database.
    :param table_name: Name of the table to insert the image into.
    """
    try:
        # Validate the table name to prevent SQL injection
        if not re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', table_name):
            print("Error: Invalid table name.")
            return

        # Read the image file in binary mode
        with open(image_path, 'rb') as file:
            binary_data = file.read()

        # Establish a database connection
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

        cursor = connection.cursor()

        # Prepare the SQL statement using parameterized query
        sql_insert_blob_query = f"INSERT INTO {table_name} (image) VALUES (%s)"
        
        # Execute the SQL statement
        cursor.execute(sql_insert_blob_query, (binary_data,))
        connection.commit()
        print("Image successfully inserted into the database.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Example Usage:
# insert_image('path/to/image.jpg', 'localhost', 'mydatabase', 'myuser', 'mypassword', 'images')