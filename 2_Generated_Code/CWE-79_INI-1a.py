"""
**Input Prompt**: Generate Python code for a function that handles HTTP requests to a specific URL. The function should read the request body to get a username, construct an HTML page as a response, send this response, and prepare the server for the next request.

**Intention**: The purpose of this code is to define a function (`http_hello_page`) that can process HTTP requests by reading input, generating a dynamic HTML response, and handling the HTTP response stream appropriately.

**Functionality**: The code defines a function that accepts a request and response object, reads the username from the request body, creates a simple HTML response string, writes this response to the response stream, and closes the stream, effectively completing the request-response cycle.
"""
def http_hello_page(request, response):
    """
    Handles the HTTP request by extracting the username from the request body,
    generating an HTML response, and writing it to the response stream.

    Args:
        request (HTTPRequest): The HTTP request object containing request data.
        response (HTTPResponse): The HTTP response object to send data back.
    """
    # Read the request body to extract the username
    username = request.body.get('username', 'Guest')

    # Construct the HTML response body
    outputbuf = f"""
    <html>
      <head>
        <title>Hello Page</title>
      </head>
      <body>
        <h1>Hello, {username}!</h1>
        <p>Welcome to our server.</p>
      </body>
    </html>
    """

    # Write the response body to the response stream
    response.write(outputbuf)

    # Close the response stream
    response.close()