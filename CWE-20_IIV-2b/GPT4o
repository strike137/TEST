from flask import Flask, redirect, request, abort

app = Flask(__name__)

def redirect_invalid_url(url):
    if 'example.com' in url:
        return redirect(url)
    else:
        return abort(400, description="Invalid URL. Only URLs from example.com are allowed.")

@app.route('/redirect/<path:url>')
def redirect_to_url(url):
    return redirect_invalid_url(url)

if __name__ == '__main__':
    app.run(debug=True)
