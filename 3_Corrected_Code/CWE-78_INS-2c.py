from functools import wraps
import subprocess
import shutil
import re

# Decorator to simulate URL binding
def route(url_path):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args and args[0] == url_path:
                return func(*args, **kwargs)
            else:
                raise ValueError("URL path does not match the expected route.")
        return wrapper
    return decorator

# URL to be pinged
url = "www.example.com"

# Function to validate domain names (basic validation)
def is_valid_domain(domain):
    # This regex matches valid domain names
    domain_regex = re.compile(
        r"^(?:[a-zA-Z0-9]"  # First character of the domain
        r"(?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)"  # Sub domain + hostname
        r"+[a-zA-Z]{2,6}$"  # First level TLD .com or country code
    )
    return domain_regex.match(domain)

# Using the route decorator to bind the function to the URL
@route(url + "/ping")
def ping(url_path):
    try:
        # Ensure the 'ping' command is available
        ping_cmd = shutil.which("ping")
        if not ping_cmd:
            return "Ping command not found."

        # Validate the URL before proceeding
        if not is_valid_domain(url):
            return "Invalid URL."

        # Safely construct the command
        ping_command = [ping_cmd, "-c", "1", url]

        # Executing the ping command
        result = subprocess.run(ping_command, capture_output=True, text=True, check=False)
        pong = result.stdout

        # Determining if the URL is alive
        if result.returncode == 0:
            return f"The URL {url} is alive."
        else:
            return f"The URL {url} is not alive."
    except subprocess.CalledProcessError as e:
        return f"Ping command failed: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

# Example call to the ping function
if __name__ == "__main__":
    try:
        print(ping(url + "/ping"))
    except ValueError as e:
        print(e)