from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get-name', methods=['POST'])
def get_name():
    """
    Handles POST requests to the /get-name endpoint. Checks for the 'name' field in the JSON
    payload and returns its value, or an error message if 'name' is not found.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON payload provided"}), 400

    if 'name' in data:
        return jsonify({"name": data['name']}), 200
    else:
        return jsonify({"error": "Field 'name' not found"}), 400

if __name__ == '__main__':
    app.run()  # Removed debug=True for production safety