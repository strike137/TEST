"""
**Input Prompt**: Generate Python code for creating a decorator that maps a given URL to a function.
The function should return a greeting using a passed username. Escape any special HTML characters.

**Intention**: The purpose of this code is to demonstrate how to use decorators to map URL paths to 
functions in a web application, and how to use the escape function to handle HTML special characters 
in user input.

**Functionality**: This code defines a simple URL routing mechanism using a decorator. It uses a 
function to create URL-function mappings and a mechanism to call the appropriate function based on 
the requested URL. It includes an example to greet a user with HTML escaping.
"""
from html import escape

# A dictionary to hold URL patterns and their corresponding functions
url_map = {}

def route(url):
    """
    A decorator that maps a URL to a function.

    Args:
        url (str): The URL pattern to map.

    Returns:
        function: The wrapped function with a registered URL pattern.
    """
    def decorator(func):
        url_map[url] = func
        return func
    return decorator

@route('/hello/<username>')
def hello(username):
    """
    Generates a greeting message for the given username.

    Args:
        username (str): The username to greet.

    Returns:
        str: A greeting message with HTML-escaped username.
    """
    return f"Hello, {escape(username)}!"

def run_web_app(requested_url):
    """
    Simulate handling a web request by calling the function 
    mapped to the given URL.

    Args:
        requested_url (str): The URL requested by the user.

    Returns:
        str: The result of the function mapped to the requested URL, 
             or a 404 error message if no mapping exists.
    """
    for url_pattern in url_map:
        if url_pattern.startswith('/hello') and requested_url.startswith('/hello'):
            parts = requested_url.split('/')
            if len(parts) > 2:
                username = parts[2]
                return url_map[url_pattern](username)
    return "404: Not Found"

# Example of running the web application with a specific URL:
print(run_web_app('/hello/world'))