from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

def render_response_from_env(env):
    """
    Renders a template from the environment with a name parameter 
    obtained from the request and returns the rendered response.

    :param env: The environment which contains the request and template
    :type env: dict
    :return: Rendered template response
    :rtype: str
    """
    name = env['request'].args.get('name', 'World')
    template = env['template']
    rendered_template = render_template_string(template, name=name)
    return rendered_template

@app.route('/')
def home():
    """
    Calls `render_response_from_env` with the `env` dictionary and 
    returns the response.

    :return: Response from `render_response_from_env`
    :rtype: str
    """
    env = {
        'request': request,
        'template': '<h1>Hello, {{ name }}!</h1>'
    }
    response = render_response_from_env(env)
    return response

if __name__ == '__main__':
    # Set debug based on environment variable or default to False
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 't']
    app.run(debug=debug_mode)