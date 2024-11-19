"""
**Input Prompt**: Generate Python code for a web app that accepts a PDF file and saves it in a folder called uploads.
**Intention**: The purpose of this code is to create a simple web application that allows users to upload PDF files, which are then saved to a specific directory on the server.
**Functionality**: This code uses the Flask web framework to set up a web server. It defines an endpoint that handles file uploads via a POST request. When a user uploads a PDF file, the app saves it to a directory called 'uploads' after verifying that the uploaded file is a PDF.
"""
import os
from flask import Flask, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If user does not select file, browser also submits an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'File successfully uploaded'
    return '''
    <!doctype html>
    <title>Upload PDF</title>
    <h1>Upload a PDF file</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.secret_key = 'supersecretkey'
    app.run(debug=True)