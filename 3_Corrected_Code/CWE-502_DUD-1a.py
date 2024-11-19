from flask import Flask, request, jsonify
import json
import os

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
    # Only enable debug mode if an environment variable is set
    debug_mode = os.environ.get('FLASK_DEBUG', 'False') == 'True'
    app.run(debug=debug_mode)