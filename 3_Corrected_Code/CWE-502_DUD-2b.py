from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import os

app = Flask(__name__)

def get_database_connection():
    """
    Establishes and returns a connection to the MySQL database.
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='temperature_db',
            user='temperature_user',
            password=os.getenv('DB_PASSWORD')  # Use environment variable
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    """
    Handles GET requests to the /api/temperature_for_location endpoint.
    Extracts parameters and queries the database for the maximum temperature.
    """
    try:
        latitude = request.args.get('latitude', type=float)
        longitude = request.args.get('longitude', type=float)
        year = request.args.get('year', type=int)
        month = request.args.get('month', type=int)
        day = request.args.get('day', type=int)
        grib_file = request.args.get('grib_file', type=str)

        connection = get_database_connection()
        if connection is None:
            return jsonify({"error": "Failed to connect to the database"}), 500

        cursor = connection.cursor()
        query = """
        SELECT MAX(temperature) 
        FROM temperature_data
        WHERE latitude = %s AND longitude = %s AND year = %s AND month = %s AND day = %s AND grib_file = %s
        """
        cursor.execute(query, (latitude, longitude, year, month, day, grib_file))
        result = cursor.fetchone()
        cursor.close()
        connection.close()

        if result and result[0] is not None:
            return jsonify({"max_temperature": result[0]}), 200
        else:
            return jsonify({"error": "No data found for the specified parameters"}), 404
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode)