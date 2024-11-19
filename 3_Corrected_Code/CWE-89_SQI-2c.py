from flask import Flask, request, redirect, url_for
import sqlite3
import os

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
    # Set debug mode based on an environment variable
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 't']
    app.run(debug=debug_mode)