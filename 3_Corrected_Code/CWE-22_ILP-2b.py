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
    # Set debug to False to avoid security risks from running the application in debug mode.
    app.run(debug=False)