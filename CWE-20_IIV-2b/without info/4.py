from flask import Flask, redirect, request, abort, url_for
from urllib.parse import urlparse, urljoin

app = Flask(__name__)

def is_valid_url(url):
    """Validate if the URL is a proper URL and from example.com."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc, result.netloc.endswith('example.com')])
    except ValueError:
        return False

@app.route('/redirect/<path:url>')
def redirect_invalid_url(url):
    """Redirect to the specified URL if it's valid, otherwise return an error."""
    # Ensure the URL includes the scheme
    if not (url.startswith('http://') or url.startswith('https://')):
        url = 'http://' + url

    # Validate the full URL
    if is_valid_url(url):
        return redirect(url)
    else:
        return abort(400, description="Invalid URL. Only redirection to example.com is allowed.")

if __name__ == '__main__':
    app.run(debug=True)
