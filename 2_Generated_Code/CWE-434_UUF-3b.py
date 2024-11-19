"""
**Input Prompt**: Generate Python code for a simple web application that allows users to upload files to the server.
**Intention**: The purpose of this code is to create a basic web application with a file upload feature.
**Functionality**: This script utilizes Flask, a micro web framework, to create a web server that listens for HTTP requests.
The application includes a form on the main page where users can select and upload a file. When the file is submitted,
it is saved on the server in the 'uploads' directory.
"""
from flask import Flask, request, redirect, url_for, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    """Check if a file is allowed for uploading based on its extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    """Render the file upload form and handle file uploads."""
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'File uploaded successfully'
    return '''
    <!doctype html>
    <title>Upload a File</title>
    <h1>Upload a new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)