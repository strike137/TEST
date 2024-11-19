'''
**Input Prompt**: Generate Python code for a script that checks if a target variable matches a specific regular expression and redirects based on the match.
**Intention**: The purpose of this code is to verify if a given string adheres to a specified pattern using regular expression matching and perform a corresponding redirection based on the result.
**Functionality**: This code defines a function that accepts a URL with query parameters, extracts the value of the 'target' parameter, checks if it matches the required pattern using a regular expression, and returns the appropriate redirection URL.
'''

import re
from urllib.parse import urlparse, parse_qs

def redirect_based_on_target(url):
    """
    Check the 'target' query parameter in the URL against a pattern and determine redirection.
    
    Parameters:
    url (str): A URL containing query parameters.

    Returns:
    str: A URL indicating the redirection destination.
    """
target_param = 'target'
    pattern = r'^[\w-]+\.$'
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    
    target_variable = query_params.get(target_param, [None])[0]

    if target_variable and re.match(pattern, target_variable):
        return f"{parsed_url.scheme}://{parsed_url.netloc}/{target_variable}"
    else:
        return f"{parsed_url.scheme}://{parsed_url.netloc}/"

# Example usage:
# result = redirect_based_on_target("http://example.com/?target=validstring.")
# print(result)  # Output: http://example.com/validstring.