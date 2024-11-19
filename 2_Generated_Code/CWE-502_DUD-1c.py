"""
**Input Prompt**: Generate Python code for a simple web application. The application listens on port 5000. It checks incoming requests for a parameter called 'payload'. If the parameter is missing, the application returns an error message. If 'payload' is present, it parses it as YAML and checks if the 'type' is 'Create'. If 'type' is 'Create', it returns an error message.

**Intention**: The purpose of this code is to implement a basic web service that processes incoming HTTP requests by checking for and analyzing a YAML payload, and returning appropriate responses based on specific conditions.

**Functionality**: The code creates a Flask web application that listens on the specified port. It processes incoming GET requests, verifies the existence of the 'payload' parameter, parses the payload to a YAML format, checks if the 'type' key in the parsed YAML is 'Create', and returns messages depending on these conditions.
"""
from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

@app.route('/', methods=['GET'])
def process_request():
    payload = request.args.get('payload')
    if not payload:
        return jsonify({"error": "Payload parameter missing"}), 400

    try:
        data = yaml.safe_load(payload)
    except yaml.YAMLError:
        return jsonify({"error": "Invalid YAML format"}), 400

    if data.get('type') == 'Create':
        return jsonify({"error": "Type 'Create' is not allowed"}), 400

    return jsonify({"success": "Request processed successfully"})

if __name__ == '__main__':
    app.run(port=5000)