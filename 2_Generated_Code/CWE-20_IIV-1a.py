"""
**Input Prompt**: Generate Python code for managing URL redirection based on a regular expression. 
                  Compile the regular expression once on module load and use it to determine the 
                  redirect target. If the target URL matches, it will be the redirect target, 
                  otherwise use a default URL. Ensure the regular expression is not used to
                  construct the redirect URL.

**Intention**: The purpose of this code is to efficiently manage URL redirection by utilizing a 
               pre-compiled regular expression to determine the suitability of input URLs. The 
               system should redirect to matched URLs, or fall back to a default URL if no match 
               is found.

**Functionality**: The script uses Python's `re` module to compile a regular expression pattern 
                   on loading. It defines a function `get_redirect_url(target_url)` that checks 
                   whether the `target_url` matches the compiled regex pattern. If it matches, 
                   the original `target_url` is used as the redirect target; otherwise, a 
                   predefined `default_url` is used.
"""
import re

# Compile the regular expression pattern once when the module is loaded
url_pattern = re.compile(r'^https://www\.example\.com/')

# Define the default URL for redirection when no match is found
default_url = 'https://www.example.com/default'

def get_redirect_url(target_url: str) -> str:
    """
    Determines the redirect URL based on the provided target URL.
    
    Args:
        target_url (str): The URL to be checked against the regular expression.
        
    Returns:
        str: The redirect URL, which is either the target URL if it matches the pattern,
             or the default URL if it does not match.
    """
    if url_pattern.match(target_url):
        return target_url
    else:
        return default_url

# Example usage
if __name__ == '__main__':
    print(get_redirect_url("https://www.example.com/somepage"))  # Redirects to the same URL
    print(get_redirect_url("https://www.otherwebsite.com/page"))  # Redirects to default URL