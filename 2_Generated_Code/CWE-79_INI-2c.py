"""
**Input Prompt**: Generate Python code for the following: 
 The render_response_from_env function takes an environment as an argument.
 The function gets the name parameter from the user request.
 The function gets the template from the environment.
 The function renders the template with the name parameter from the request.
 The function returns a response with the rendered template.
 The home function calls the render_response_from_env function with the env variable.
 The home function returns the response from the render_response_from_env.

**Intention**: To create a template rendering system where a name parameter from a user request is used to populate a template obtained from an environment, and a final response is constructed and returned.

**Functionality**: 
- `render_response_from_env(env)`: Takes an environment object as argument, extracts the 'name' parameter from a request, fetches a template from the environment, renders the template with the 'name', and returns the rendered response.
- `home()`: Calls `render_response_from_env` with the `env` variable and returns the final response.
"""
from flask import Flask, render_template_string, request

app = Flask(__name__)

def render_response_from_env(env):
    """
    Renders a template with a name parameter extracted from 
    the user request within the given environment.
    
    Args:
        env: The environment object containing the template.
    
    Returns:
        str: The rendered template as a response.
    """
    # Simulate getting the name parameter from a request
    name = request.args.get('name', default='World')
    
    # Assume env has a get_template method that fetches a template
    template = env.get_template('template.html')
    
    # Render the template with the name parameter
    rendered_template = render_template_string(template, name=name)
    
    # Return the rendered template
    return rendered_template

@app.route('/')
def home():
    """
    Handles the home route by calling the render_response_from_env function
    with the current environment and returning the rendered response.
    
    Returns:
        str: The response object containing the rendered template.
    """
    # Simulated environment;
    # in practice, this would be passed to the function or be a part of app config
    class Environment:
        def get_template(self, template_name):
            # This is a stand-in to simulate template retrieval
            # In practice, use a template file or Jinja environment
            if template_name == 'template.html':
                return "<h1>Hello, {{ name }}!</h1>"
            return ""

    env = Environment()
    return render_response_from_env(env)