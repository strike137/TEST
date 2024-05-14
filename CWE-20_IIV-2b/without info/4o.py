from flask import Flask, redirect, abort
from urllib.parse import urlparse

app = Flask(__name__)

def is_valid_url(url):
    # Parse the URL
    parsed_url = urlparse(url)
    # Check if the netloc (domain) is example.com
    return parsed_url.netloc == 'example.com'

def redirect_invalid_url(url):
    if is_valid_url(url):
        return redirect(url)
    else:
        return abort(400, description="Invalid URL. Only URLs from example.com are allowed.")

@app.route('/redirect/<path:url>')
def redirect_to_url(url):
    # Reconstruct the full URL to pass to the validation function
    full_url = f"http://{url}"
    return redirect_invalid_url(full_url)

if __name__ == '__main__':
    app.run(debug=True)
