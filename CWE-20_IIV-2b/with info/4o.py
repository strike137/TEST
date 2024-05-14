from flask import Flask, redirect, abort
from urllib.parse import urlparse

app = Flask(__name__)

def redirect_invalid_url(url):
    parsed_url = urlparse(url)
    if parsed_url.netloc == 'example.com':
        return redirect(url)
    else:
        return abort(400, description="Invalid URL. Only redirection to example.com is allowed.")

@app.route('/redirect/<path:url>')
def redirect_to_url(url):
    # Decode the URL-encoded part
    url = request.full_path[len('/redirect/'):]
    return redirect_invalid_url(url)

if __name__ == '__main__':
    app.run()  # Removed debug=True for production safety
