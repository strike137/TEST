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
    app_env = os.getenv('FLASK_ENV', 'production')
    is_debug = app_env != 'production'
    app.run(debug=is_debug)