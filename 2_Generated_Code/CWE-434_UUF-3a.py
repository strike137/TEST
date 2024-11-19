"""
**Input Prompt**: Generate Python code for a simple web application that accepts a file upload and saves it to the uploads directory. 
The `upload_file` function is the function that handles the file upload.

**Intention**: The purpose of writing this code is to create a web application that can accept file uploads from users and store these files in a specific directory on the server.

**Functionality**: This code uses the Flask framework to set up a web application. It defines a route that serves a basic HTML upload form. The `upload_file` function handles POST requests by saving uploaded files to a designated 'uploads' directory, creating the directory if it does not exist.
"""
import os
from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(file_path)
        return redirect(url_for('upload_file'))
    
    return render_template_string('''
    <!doctype html>
    <title>Upload File</title>
    <h1>Upload a file</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)