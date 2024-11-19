from flask import Flask, request, jsonify
import sqlite3
import os

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
    # Set debug mode based on environment variable
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 'yes']
    app.run(debug=debug_mode)