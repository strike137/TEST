from flask import Flask, request, jsonify
import subprocess
import re

app = Flask(__name__)

def is_valid_hostname(hostname: str) -> bool:
    """
    Validates a hostname for correct syntax.
    """
    if len(hostname) > 255:
        return False
    if hostname[-1] == ".":
        hostname = hostname[:-1]  # Strip the trailing dot
    allowed = re.compile(r"(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in hostname.split("."))

@app.route('/ping', methods=['GET'])
def ping():
    """
    Extracts the URL from the GET request and runs a ping command on it.
    Returns the output of the ping command.
    """
    url = request.args.get('url', '')
    
    if not is_valid_hostname(url):
        return "Invalid hostname", 400
    
    try:
        # Ensure the subprocess does not use shell=True and check the given URL
        # Use a safe, fixed command format to prevent injection
        output = subprocess.check_output(
            ['/usr/bin/ping', '-c', '4', url],  # use the absolute path to ping
            stderr=subprocess.STDOUT,
            text=True,  # This automatically decodes the output to a string
            timeout=10  # Add a timeout to prevent hanging
        )
        return jsonify({"output": output})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": "Ping failed", "output": e.output}), 400
    except Exception as e:
        # Handle other potential exceptions and return a generic error message
        return jsonify({"error": "An error occurred", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Ensure debug is set to False in production