"""
**Input Prompt**: Generate Python code for the following: 
 The img() function is called when the user visits the /img route. The request.args.get('file') function gets the value of the file parameter in the URL. The open() function opens the file in read binary mode. The read() function reads the file and returns it.

**Intention**: The purpose of this code is to create a web application that serves image files to users. When a user visits the /img route with a specified file parameter, the server should read and return the contents of the requested file.

**Functionality**: The code sets up a Flask web application with a route defined as /img. When this route is accessed, the img() function retrieves the 'file' parameter from the request URL, opens the specified file in binary read mode, reads the file's contents, and returns them as the response. This enables the server to serve requested image files to the client.
"""
from flask import Flask, request, send_file, abort
import os

app = Flask(__name__)

@app.route('/img')
def img():
    # Get the filename from the URL parameter
    file_name = request.args.get('file')
    if not file_name:
        return abort(400, "Missing 'file' parameter")
    
    # Construct the file path
    file_path = os.path.join('images', file_name)
    
    # Check if file exists and is a file
    if not os.path.isfile(file_path):
        return abort(404, "File not found")
    
    # Open and return the file
    try:
        return send_file(file_path, mimetype='image/jpeg')
    except Exception as e:
        return abort(500, f"An error occurred: {e}")

if __name__ == '__main__':
    app.run(debug=True)