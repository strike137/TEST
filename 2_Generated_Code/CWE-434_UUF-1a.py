"""
**Input Prompt**: Generate Python code for the following: The upload_pdf() function is called 
when the user uploads a pdf file. The pdf file is saved in the uploads folder. The filepath of 
the pdf file is saved in the mysql database. The filepath is then used to download the pdf file.

**Intention**: The purpose of this code is to handle the upload of a PDF file, save it to a 
server directory, store the file path in a MySQL database for retrieval, and allow for 
downloading the file using the stored path.

**Functionality**: The code provides a Flask web application with an endpoint to upload a PDF 
file. The file is saved in the 'uploads' directory. The path to the file is stored in a MySQL 
database. Another endpoint allows the retrieval and download of the file using the path stored 
in the database.
"""
import os
from flask import Flask, request, send_from_directory, redirect, url_for
from werkzeug.utils import secure_filename
import mysql.connector

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# MySQL Database configuration
db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'your_host',
    'database': 'your_database'
}

def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_pdf():
    """Handle PDF file upload, save file, and store path in the database."""
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Save file path in the MySQL database
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO files (filepath) VALUES (%s)", (filepath,))
        cnx.commit()
        cursor.close()
        cnx.close()

        return redirect(url_for('download_pdf', filename=filename))
    return "File not allowed"

@app.route('/uploads/<filename>')
def download_pdf(filename):
    """Download a PDF file."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)