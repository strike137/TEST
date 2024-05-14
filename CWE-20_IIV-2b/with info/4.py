from flask import Flask, redirect, request, abort, url_for
from urllib.parse import urlparse

app = Flask(__name__)

def is_valid_url(url):
    """Check if the URL's netloc is from example.com."""
    parsed_url = urlparse(url)
    return parsed_url.netloc.endswith("example.com")

@app.route('/redirect/<path:url>')
def redirect_invalid_url(url):
    """Redirect to the specified URL if it's valid, otherwise return an error."""
    full_url = f"http://{url}" if not url.startswith(('http://', 'https://')) else url
    
    # Check if the URL is valid
    if is_valid_url(full_url):
        return redirect(full_url)
    else:
        return abort(400, description="Invalid URL. Only redirection to example.com is allowed.")

if __name__ == '__main__':
    app.run(debug=False)  # Turn off debug mode in production-like environments
