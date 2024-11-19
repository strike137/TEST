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
    # Set debug based on environment or configuration settings
    app.run(debug=False)