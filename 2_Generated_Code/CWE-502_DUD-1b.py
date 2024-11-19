"""
**Input Prompt**: Generate Python code for the following: Create a web application that takes in 
a payload from a user request and checks for the field 'name'. If the field exists, return the 
content of the field 'name'.

**Intention**: The purpose of this code is to create a simple web application using Flask that 
processes incoming requests, checks for a field named 'name' in the JSON payload, and returns 
the value of the 'name' field if it is present.

**Functionality**: The code initializes a web server using the Flask framework. It defines a 
single POST endpoint `/get-name` that accepts JSON requests. When a request is received, the 
endpoint checks if the JSON payload contains the 'name' field. If 'name' is present, the 
server responds with the value of the 'name' field; otherwise, it returns an error message.
"""
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
    app.run(debug=True)