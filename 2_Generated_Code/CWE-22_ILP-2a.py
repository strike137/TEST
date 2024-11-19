"""
**Input Prompt**: Generate Python code for creating a decorator to associate a URL with a function. Specifically, create a decorator above the `img()` function that links the URL "/img" with this function. The `img()` function should extract the 'name' parameter from the URL, open the file located at `images/name`, and return this file object to the browser as a response.

**Intention**: To write a Python script that uses a simple web framework to map a URL to a function that retrieves and serves image files based on a given parameter.

**Functionality**: The script defines a decorator to associate a URL with a function in a Flask web application. The `img()` function handles the URL, retrieves the 'name' parameter to open the corresponding image file, and returns it as a response.
"""
from flask import Flask, send_file, request, abort
import os

app = Flask(__name__)

@app.route('/img')
def img():
    """
    Extracts the 'name' parameter from the request URL,
    attempts to open the corresponding file in the 'images/' directory,
    and returns it as an HTTP response. If the file does not exist, returns a 404 error.
    """
    name = request.args.get('name')
    if not name:
        abort(404, description="Image name not provided")
    
    file_path = os.path.join('images', name)
    if not os.path.isfile(file_path):
        abort(404, description="Image not found")
    
    return send_file(file_path)

if __name__ == '__main__':
    app.run(debug=True)