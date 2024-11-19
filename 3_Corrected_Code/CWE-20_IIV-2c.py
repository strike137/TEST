from flask import Flask, request, redirect, jsonify
from urllib.parse import urlparse
import os

app = Flask(__name__)

@app.route('/redirect')
def redirect_invalid_url():
    url = request.args.get('url')
    if url:
        parsed_url = urlparse(url)
        if parsed_url.hostname == 'example.com':
            # Corrected condition to check for http and https schemes
            if parsed_url.scheme in ['http', 'https']:
                return redirect(url)
            else:
                return jsonify({'error': 'Invalid URL scheme. Only HTTP and HTTPS are allowed.'}), 400
        else:
            return jsonify({'error': 'Invalid domain. Only example.com is allowed.'}), 400
    return jsonify({'error': 'No URL provided.'}), 400

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')
    app.run(debug=debug_mode)
```