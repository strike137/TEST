"""
**Input Prompt**: Generate Python code for the following: 
A decorator tells the web application what URL should trigger our function. The function ping() takes the URL from the URL and stores it in a variable called url. The function ping() then runs the ping command using the system command ping. The output of the ping command is stored in a variable called output. The function ping() returns the output of the ping command.

**Intention**: Create a web server endpoint that runs a system ping command on a given URL and returns the result.

**Functionality**: The code sets up a simple Flask web application with a single route '/ping' that accepts a URL as a query parameter. When the endpoint is triggered, it executes a system ping command on the provided URL and returns the result as a string.
"""
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    """
    Extracts the URL from the GET request and runs a ping command on it.
    Returns the output of the ping command.
    """
    url = request.args.get('url', '')
    try:
        output = subprocess.check_output(['ping', '-c', '4', url], stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"Ping failed: {e.output.decode('utf-8')}", 400

if __name__ == '__main__':
    app.run(debug=True)