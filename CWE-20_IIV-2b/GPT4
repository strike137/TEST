from flask import Flask, redirect, request, abort

app = Flask(__name__)

def is_valid_url(url):
    """Check if the URL is from example.com."""
    return url.startswith("http://example.com") or url.startswith("https://example.com")

@app.route('/redirect/<path:url>')
def redirect_invalid_url(url):
    """Redirect to the specified URL if it's valid, otherwise return an error."""
    # Prepend 'http://' to the URL if it doesn't start with 'http://' or 'https://'
    if not (url.startswith('http://') or url.startswith('https://')):
        url = 'http://' + url
    
    # Check if the URL is valid
    if is_valid_url(url):
        return redirect(url)
    else:
        return abort(400, description="Invalid URL. Only redirection to example.com is allowed.")

if __name__ == '__main__':
    app.run(debug=True)
