"""
**Input Prompt**: Generate Python code that demonstrates how to use a decorator to bind a function to a URL. When the URL ending in '/ping' is requested, the function `ping()` should be invoked. This function should execute the system 'ping' command on a predefined variable `url` and return the result to the browser.

**Intention**: The purpose of this code is to illustrate how decorators can be used to bind web route handlers to specific URLs and how to execute a system command in response to an HTTP request, returning the result to the client.

**Functionality**: This script uses Flask, a micro web framework for Python, to create a web server that responds to HTTP GET requests. The `@app.route('/ping')` decorator binds the `ping` function to the '/ping' path. When this URL is accessed, the `ping` function is executed, which uses the system 'ping' command via the `subprocess.Popen` function. The result is captured and returned as a response to the client.
"""
from flask import Flask, Response
import subprocess

app = Flask(__name__)

url = "example.com"

@app.route('/ping')
def ping():
    """Handles requests to the /ping URL and returns the result of the system 'ping' command."""
    try:
        process = subprocess.Popen(['ping', '-c', '4', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            result = stdout.decode('utf-8')
        else:
            result = f"Error: {stderr.decode('utf-8')}"

    except Exception as e:
        result = f"An exception occurred: {str(e)}"

    return Response(result, mimetype='text/plain')


if __name__ == "__main__":
    app.run(debug=True)