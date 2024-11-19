from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/<username>')
def hello(username):
    """
    Render a template with the provided username.

    :param username: String captured from the URL segment.
    :return: Rendered HTML content with the username displayed.
    """
    return render_template('hello.html', username=username)

if __name__ == '__main__':
    # Do not use debug=True in production
    app.run()