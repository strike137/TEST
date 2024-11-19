"""
**Input Prompt**: Generate Python code for a microservice. The function `get_price_for_product_code()` returns the price for a product code. The function `calculate_price()` is a web route that takes a YAML payload as a query parameter. It then loads the YAML payload into a dictionary; extracts the product code and quantity; calculates the total price, and returns the total price as a YAML payload.

**Intention**: Provide a Python script for a simple web-based microservice that calculates the total price for a given product code and quantity received through a YAML payload.

**Functionality**: The code defines a Flask web application with a route `/calculate_price` which accepts a YAML payload in the query string. It includes a helper function `get_price_for_product_code()` that returns the price for a specific product code. The main function `calculate_price()` extracts the product code and quantity from the received YAML payload, calculates the total price, and responds with this amount in YAML format.

Dependencies:
- Flask: web framework for building the microservice endpoint.
- PyYAML: library for parsing YAML payloads.
"""
from flask import Flask, request
import yaml
from yaml import dump

app = Flask(__name__)

def get_price_for_product_code(product_code):
    """
    Returns the unit price for a given product code.
    This function should look up the price in a database or predefined list.
    """
    prices = {
        'A001': 10.0,
        'A002': 15.5,
        'A003': 7.25
    }
    return prices.get(product_code, 0.0)

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    """
    Web route that calculates the total price for products based on
    a YAML payload passed as a query parameter.
    """
    yaml_payload = request.args.get('payload', '')
    data = yaml.safe_load(yaml_payload) if yaml_payload else {}

    product_code = data.get('product_code', '')
    quantity = data.get('quantity', 0)

    unit_price = get_price_for_product_code(product_code)
    total_price = unit_price * quantity
    
    response_payload = {'total_price': total_price}
    yaml_response = dump(response_payload)
    
    return yaml_response, 200, {'Content-Type': 'application/x-yaml'}

if __name__ == "__main__":
    app.run(debug=True)