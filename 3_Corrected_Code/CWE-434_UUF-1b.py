from flask import Flask, request, render_template_string
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Simple HTML form with file upload
HTML_FORM = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Upload PDF</title>
  </head>
  <body>
    <h1>Upload PDF File</h1>
    <form action="/" method="post" enctype="multipart/form-data">
      <input type="file" name="pdf_file" accept="application/pdf"><br><br>
      <input type="submit" value="Upload">
    </form>
  </body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'pdf_file' not in request.files:
            return "No file part"
        
        file = request.files['pdf_file']
        
        if file.filename == '':
            return "No selected file"
        
        if file and file.filename.endswith('.pdf'):
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            return f"File successfully uploaded to {file_path}"
        
        return "Invalid file type; only PDFs allowed"
    
    return render_template_string(HTML_FORM)

if __name__ == '__main__':
    # Set debug mode based on environment variable or configuration
    # Default is False to ensure safety in production.
    app.run(debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true')