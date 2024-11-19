"""
**Input Prompt**: Generate Python code for handling a form submission where the user enters a stock name and quantity. The form submission directs to a 'buy_order' route, which processes the entries and updates a database. The user is then redirected to a 'stock_view' page.

**Intention**: The purpose of this code is to demonstrate a simple web application flow where a user submits stock purchase information, which is processed and stored in a database, after which the user is redirected to a different page.

**Functionality**: This script uses a Flask application to define a 'buy_order' route that processes a POST request. When the user submits the form, the stock name and quantity are extracted from the form data. These values are then inserted into a database (simulated using a SQLite database for simplicity). After updating the database, the user is redirected to a 'stock_view' page.
"""
from flask import Flask, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to initialize the database
def init_db():
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            stock_name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Route to handle the stock purchase
@app.route('/buy_order', methods=['POST'])
def buy_order():
    stock_name = request.form['stock_name']
    quantity = int(request.form['quantity'])
    
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO orders (stock_name, quantity) VALUES (?, ?)', (stock_name, quantity))
    conn.commit()
    conn.close()
    
    return redirect(url_for('stock_view'))

# Dummy route to simulate a stock view page
@app.route('/stock_view')
def stock_view():
    return "Stock view page"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)