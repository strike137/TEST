"""
**Input Prompt**: Generate Python code for the following:
The code is a simple script that accepts an image file and stores it in a MySQL database.

**Intention**: The purpose of this code is to facilitate the process of taking an image file and storing it into a MySQL database table in a straightforward manner.

**Functionality**: The code prompts for an image file, reads the file in binary mode, connects to a MySQL database using provided credentials, and inserts the image into a designated table. It utilizes the MySQL connector for Python to manage these operations.
"""
import mysql.connector
from mysql.connector import Error

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
        # Prepare the INSERT statement
        sql_insert_blob_query = f"""INSERT INTO {table_name} (image) VALUES (%s)"""

        # Execute the SQL statement
        cursor.execute(sql_insert_blob_query, (binary_data,))
        connection.commit()
        print("Image successfully inserted into the database.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Example Usage:
# insert_image('path/to/image.jpg', 'localhost', 'mydatabase', 'myuser', 'mypassword', 'images')