
from flask import Flask, redirect, url_for, abort
import re
import os

app = Flask(__name__)

def is_valid_url(url):
    # Check if the URL belongs to 'example.com'
    return bool(re.match(r"^https?://(www\.)?example\.com", url))

@app.route('/redirect/<path:url>')
def redirect_invalid_url(url):
    # Decode the URL-encoded path component
    decoded_url = re.sub(r'%([0-9A-Fa-f]{2})', lambda m: chr(int(m.group(1), 16)), url)
    
    # Prepend 'http://' if the scheme is not provided
    if not re.match(r"^https?://", decoded_url):
        decoded_url = "http://" + decoded_url
    
    # Use the corrected decoded_url to check if the URL is valid
    if is_valid_url(decoded_url):
        return redirect(decoded_url)
    else:
        abort(400, "Invalid URL: Only URLs from 'example.com' are allowed.")

if __name__ == '__main__':
    # Run the app in debug mode only if the FLASK_DEBUG environment variable is set to '1'
    debug_mode = os.getenv('FLASK_DEBUG', '0') == '1'
    app.run(debug=debug_mode)
```