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
    # Only enable debug mode if an environment variable `FLASK_DEBUG` is set to 'true'
    debug_mode = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(debug=debug_mode)