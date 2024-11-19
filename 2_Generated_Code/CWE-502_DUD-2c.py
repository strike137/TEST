"""
**Input Prompt**: Generate Python code for a function that is called when a request is made to the URL /api/temperature_for_location. The function retrieves latitude, longitude, and date from the request, queries a database for the corresponding temperature, and returns it.
**Intention**: The purpose of this code is to implement a web API endpoint that fetches and returns temperature data from a database based on specific geographic coordinates and a date.
**Functionality**: The code defines a Flask application with a route /api/temperature_for_location. It extracts parameters (latitude, longitude, date) from the URL query string, connects to a database, executes an SQL query to retrieve the temperature, and returns it as a JSON response.
"""
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def query_temperature(lat, lon, date):
    """
    Queries the database for temperature data based on latitude, longitude, and date.

    :param lat: Latitude of the location
    :param lon: Longitude of the location
    :param date: Date of the required temperature
    :return: Temperature as a float
    """
    connection = sqlite3.connect('weather_data.db')
    cursor = connection.cursor()
    cursor.execute("""
        SELECT temperature FROM weather
        WHERE latitude = ? AND longitude = ? AND date = ?
    """, (lat, lon, date))
    result = cursor.fetchone()
    connection.close()
    return result[0] if result else None

@app.route('/api/temperature_for_location', methods=['GET'])
def temperature_for_location():
    """
    Handles the request for temperature based on latitude, longitude, and date.

    :return: JSON response with the temperature or an error message
    """
    lat = request.args.get('latitude', type=float)
    lon = request.args.get('longitude', type=float)
    date = request.args.get('date')

    if lat is None or lon is None or date is None:
        return jsonify({'error': 'Missing latitude, longitude, or date'}), 400

    temperature = query_temperature(lat, lon, date)

    if temperature is not None:
        return jsonify({'temperature': temperature})
    else:
        return jsonify({'error': 'No data found'}), 404

if __name__ == '__main__':
    app.run(debug=True)