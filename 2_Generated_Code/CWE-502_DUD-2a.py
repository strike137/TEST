"""
**Input Prompt**: Generate Python code for the following: 
The function `temperature_for_location()` is called when the URL /api/temperature_for_location is requested.
The function gets the latitude, longitude, and date from the payload. 
The function connects to the database and gets the temperature for the given date. 
The function returns the temperature. The code is a simple example of how to use the database. 
The database is called Sensor.

**Intention**: The purpose of this code is to demonstrate a simple example of connecting to a database 
called Sensor to retrieve temperature data based on inputs provided via an API request. 

**Functionality**: 
1. Define a Flask app to handle a POST request to the endpoint /api/temperature_for_location.
2. Extract latitude, longitude, and date from the request payload.
3. Connect to a hypothetical SQLite database called Sensor.
4. Query the database to find and return the temperature for the specified location and date.
"""
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_temperature_from_db(latitude, longitude, date):
    """
    Connects to the Sensor database and retrieves the temperature for the given latitude, longitude, and date.
    
    :param latitude: float, the latitude of the location
    :param longitude: float, the longitude of the location
    :param date: str, the date for which the temperature is requested in 'YYYY-MM-DD' format
    :return: float, the temperature for the given location and date or None if not found
    """
    conn = sqlite3.connect('sensor.db')
    cursor = conn.cursor()

    query = """
    SELECT temperature FROM temperature_data 
    WHERE latitude = ? AND longitude = ? AND date = ?
    """
    
    cursor.execute(query, (latitude, longitude, date))
    result = cursor.fetchone()
    
    conn.close()
    
    return result[0] if result else None

@app.route('/api/temperature_for_location', methods=['POST'])
def temperature_for_location():
    """
    Handles the API request to get temperature for a specific location and date. Expects JSON payload with 
    'latitude', 'longitude', and 'date' fields. Returns the temperature as a JSON response or an error message if not found.
    """
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    date = data.get('date')

    if latitude is None or longitude is None or date is None:
        return jsonify({'error': 'Missing required parameters'}), 400

    temperature = get_temperature_from_db(latitude, longitude, date)

    if temperature is not None:
        return jsonify({'temperature': temperature}), 200
    else:
        return jsonify({'error': 'Temperature data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)