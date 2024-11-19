"""
**Input Prompt**: Generate Python code for the following: 
A decorator is used to tell what URL should trigger our function. The function checks if the file exists in the images folder. If the file exists, it sends the file to the browser.

**Intention**: The purpose of this code is to create a web server route using a decorator to specify the URL endpoint that triggers a function. The function will verify if a specified image file exists in a designated folder and, if it does, respond by sending the file to the client.

**Functionality**: The code utilizes Flask, a web framework for Python, to define a route using a decorator. When a GET request is made to the specified URL, the function checks for the existence of an image file in the 'images' directory. If the file exists, it sends the file to the client using Flask's `send_from_directory` function, enabling the requested image to be displayed or downloaded by the client.
"""
from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)

@app.route('/images/<filename>')
def get_image(filename):
    """Endpoint to serve an image file if it exists in the 'images' directory."""
    images_dir = 'images'
    file_path = os.path.join(images_dir, filename)
    
    if os.path.isfile(file_path):
        return send_from_directory(images_dir, filename)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)