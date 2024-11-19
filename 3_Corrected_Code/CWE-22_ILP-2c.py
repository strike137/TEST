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
    # Run the app without debug mode enabled for production
    app.run(debug=False)