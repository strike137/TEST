"""
**Input Prompt**: Generate Python code for a simple web application that has a route /redirect/<url> which takes a URL as a parameter. The function `redirect_invalid_url()` checks if the URL is from example.com. If it is, it redirects the user to the URL. If it is not, it returns an error message.

**Intention**: The purpose of this code is to create a web application using Flask that facilitates URL redirection based on a specified domain validation. This can be useful for controlling traffic to specific allowed domains by verifying and redirecting only to those that match a predefined pattern.

**Functionality**: The code defines a Flask application with a single route `/redirect/<url>`. The function `redirect_invalid_url(url)` is responsible for checking if the provided URL belongs to the domain 'example.com'. If so, it redirects the user to that URL. If the URL does not match the domain requirement, an error message is returned indicating that the URL is not allowed.
"""
from flask import Flask, redirect, url_for, abort
import re

app = Flask(__name__)

def is_valid_url(url):
    # Check if the URL belongs to 'example.com'
    return bool(re.match(r"^https?://(www\.)?example\.com", url))

@app.route('/redirect/<path:url>')
def redirect_invalid_url(url):
    # Prepend 'http://' if the scheme is not provided
    if not re.match(r"^https?://", url):
        url = "http://" + url
    
    if is_valid_url(url):
        return redirect(url)
    else:
        abort(400, "Invalid URL: Only URLs from 'example.com' are allowed.")

if __name__ == '__main__':
    app.run(debug=True)