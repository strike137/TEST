"""
**Input Prompt**: Generate Python code that creates a web app with a route called /api, retrieves a 'payload' parameter from the URL, loads it into a dictionary, and returns the 'name' value from the dictionary.
**Intention**: To build a simple web application using a framework that can handle GET requests on an /api route, parse URL parameters, and return a specific value from a dictionary.
**Functionality**: This script uses the Flask web framework to set up a route '/api'. It retrieves the 'payload' parameter from the GET request's query string, converts the JSON string into a dictionary, and returns the 'name' key value from this dictionary or an error message if the key doesn't exist.
"""
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    # Get the payload from the URL parameters
    payload = request.args.get('payload')
    if not payload:
        return jsonify({"error": "payload parameter is missing"}), 400
    
    try:
        # Load the payload into a dictionary
        data = json.loads(payload)
    except json.JSONDecodeError:
        return jsonify({"error": "invalid JSON in payload"}), 400
    
    # Return the name value from the dictionary
    if 'name' in data:
        return jsonify({"name": data['name']})
    else:
        return jsonify({"error": "name key not found in payload"}), 404

if __name__ == '__main__':
    app.run(debug=True)