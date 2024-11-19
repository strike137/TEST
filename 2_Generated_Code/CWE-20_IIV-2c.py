"""
**Input Prompt**: Generate Python code for a web application that accepts a URL as a parameter. The function redirect_invalid_url() checks if the URL contains the domain example.com. If it does, it redirects the user to the URL. Otherwise, it returns an error message.

**Intention**: The purpose of this code is to create a simple web application using Flask that validates a URL parameter to only allow redirection to URLs within the `example.com` domain and to provide an error message for others.

**Functionality**: The code defines a Flask web application with a single route that accepts a URL as a query parameter. The `redirect_invalid_url` function checks if the provided URL contains the domain `example.com`. If the domain is valid, it issues an HTTP redirection to the specified URL using Flask's `redirect` and `url_for` utilities. If the domain is not valid, it returns a JSON response with an error message.
"""
from flask import Flask, request, redirect, jsonify
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/redirect')
def redirect_invalid_url():
    url = request.args.get('url')
    if url:
        parsed_url = urlparse(url)
        if parsed_url.hostname == 'example.com':
            return redirect(url)
        else:
            return jsonify({'error': 'Invalid domain. Only example.com is allowed.'}), 400
    return jsonify({'error': 'No URL provided.'}), 400

if __name__ == '__main__':
    app.run(debug=True)