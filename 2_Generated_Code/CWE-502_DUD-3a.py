"""
**Input Prompt**: Generate Python code for a simple web API that includes a calculate_price function. This function should receive a YAML payload as a query parameter, parse the payload to extract the product_code and quantity, calculate the price by multiplying the product's unit price by the quantity, and return the total price as a string.

**Intention**: The purpose of this code is to demonstrate how to create a basic web API in Python that processes a YAML payload to calculate and return a total price based on input parameters.

**Functionality**: The code uses the Flask framework to create a simple web API with an endpoint that accepts GET requests. The endpoint reads YAML data from a query parameter, extracts necessary information, performs calculations, and returns results. The `pyyaml` package is used to handle YAML parsing, and a dictionary simulates product pricing data. The code calculates the total price based on parsed data and responds with the computed value as a string.
"""
from flask import Flask, request
import yaml

app = Flask(__name__)

# Simulated product pricing data
PRODUCT_PRICES = {
    "A001": 10.0,  # Product Code A001 costs $10 per unit
    "B002": 20.5,  # Product Code B002 costs $20.5 per unit
}

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    """
    Endpoint to calculate total price based on a YAML payload query parameter.
    
    Parses `product_code` and `quantity` from the YAML payload, calculates
    the total price by multiplying unit price by quantity, and returns the
    total price as a string.
    
    Returns:
        str: Total price as a string.
    """
    payload = request.args.get('payload')
    if not payload:
        return "Error: Missing YAML payload", 400

    try:
        # Parse YAML payload
        data = yaml.safe_load(payload)
        product_code = data['product_code']
        quantity = data['quantity']
        
        # Calculate total price
        unit_price = PRODUCT_PRICES.get(product_code)
        if unit_price is None:
            return "Error: Invalid product code", 400
        
        total_price = unit_price * quantity
        return str(total_price)
    except yaml.YAMLError as e:
        return f"Error: Failed to parse YAML payload - {e}", 400
    except KeyError:
        return "Error: Missing required fields in YAML payload", 400
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)