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
    # In production, do not use debug=True for security reasons
    app.run()