from flask import Flask, Response
import subprocess
import socket
import shlex

app = Flask(__name__)

url = "example.com"

@app.route('/ping')
def ping():
    """Handles requests to the /ping URL and returns the result of the system 'ping' command."""
    try:
        # Resolve the domain first using socket to check for validity
        ip = socket.gethostbyname(url)

        # Using a full path for the 'ping' command for added security
        # Using resolved IP to avoid unexpected behavior
        command = ['/bin/ping', '-c', '4', shlex.quote(ip)]
        
        # Ensure shell=False for security
        process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False, shell=False)

        if process.returncode == 0:
            result = process.stdout.decode('utf-8')
        else:
            result = f"Error: {process.stderr.decode('utf-8')}"

    except socket.gaierror:
        result = "Invalid domain: Unable to resolve host"
    except Exception as e:
        result = f"An exception occurred: {str(e)}"

    return Response(result, mimetype='text/plain')


if __name__ == "__main__":
    # Set debug to False to secure the application
    app.run(debug=False)