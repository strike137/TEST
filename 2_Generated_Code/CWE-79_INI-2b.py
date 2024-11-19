"""
**Input Prompt**: Generate Python code for the following: 
The render_response_from_env function takes an environment as an argument and gets the name parameter from the request. 
The function also gets the template from the environment. 
The function renders the template with the name parameter. 
The function returns a response with the rendered template. 
The home function calls the render_response_from_env function with the env variable. 
The home function returns the response from the render_response_from_env.

**Intention**: The purpose of this code is to create a mechanism where a template is rendered with a name parameter derived 
from a request, which is part of a web application's environment configuration. The rendered response is returned to the client.

**Functionality**: The code defines two functions:
1. `render_response_from_env` which extracts the name from a request, gets a template, renders it with the name, and constructs 
   a response.
2. `home` function that utilizes `render_response_from_env`, passing an environmental configuration, to get and return the response.
"""
from flask import Flask, request, render_template_string

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
    app.run(debug=True)