"""
**Input Prompt**: Generate Python code for a simple web application that has a single route. The route takes a 'target' parameter and redirects to it. Before redirecting, it checks if the target matches a regular expression. If the target matches, it redirects to it; otherwise, it redirects to '/'. The regular expression should match any URL containing 'example.com'.

**Intention**: To create a functional web application using Flask that handles input URL redirection based on a regular expression match condition. This aims to ensure URLs are properly validated before redirection to enhance security and user experience.

**Functionality**: 
1. Sets up a simple Flask web server with a single route `/redirect`.
2. The route accepts a 'target' query parameter representing the URL to redirect to.
3. Utilizes a regular expression to check if the 'target' contains 'example.com'.
4. If the 'target' URL matches the regular expression, the app performs a redirection to it.
5. If the 'target' URL does not match the expression, it defaults to redirecting the user to the home route '/'. 
6. Provides feedback on the redirection through HTTP responses to confirm the validation process.
"""
from flask import Flask, request, redirect
import re

app = Flask(__name__)

@app.route('/redirect')
def redirect_target():
    target = request.args.get('target', '')
    regex = r'.*example\.com.*'

    if re.match(regex, target):
        return redirect(target)
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)