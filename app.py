from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://selcia2110605:uUXoiQVyFTSZI0qc@stockmaintenance.ztbi9gj.mongodb.net/users_database'
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/product')
def product():
    products = mongo.db.products.find()
    return render_template('product.html', products=products)

@app.route('/add_product', methods=['POST'])
def add_product():
    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        opening_stock = int(request.form['opening_stock'])
        prices = request.form['prices']
    
        # Insert the product into MongoDB
        mongo.db.products.insert_one({
            'code': code,
            'name': name,
            'opening_stock': opening_stock,
            'prices': prices
        })
        products.append({"code": code, "name": name, "opening_stock": opening_stock, "prices": prices})

        # Initialize stock details for the new product
        initialize_stock(code, opening_stock)
        return redirect(url_for('product'))

@app.route('/purchase')
def purchase():
    purchases = mongo.db.purchases.find()
    return render_template('purchase.html', purchases=purchases)

@app.route('/add_purchase', methods=['POST'])
def add_purchase():
    if request.method == 'POST':
        product_code = request.form['product_code']
        quantity = int(request.form['quantity'])
        price = request.form['price']
        date = datetime.now()
        # Insert the purchase into MongoDB
        mongo.db.purchases.insert_one({
            'product_code': product_code,
            'quantity': quantity,
            'price': price,
            'date': date
        })

        update_stock(product_code, quantity, 0)
        return redirect(url_for('purchase'))

def update_stock(product_code, purchase_quantity, sales_quantity):
    # Get the current stock details for the product
    stock_details = mongo.db.stocks.find_one({'product_code': product_code})

    # Update the stock details
    new_purchase_stock = stock_details.get('purchase_stock', 0) + purchase_quantity
    new_sales_stock = stock_details.get('sales_stock', 0) + sales_quantity
    new_current_stock = stock_details.get('opening_stock', 0) + new_purchase_stock - new_sales_stock

    # Update the stock details in the stocks collection
    mongo.db.stocks.update_one(
        {'product_code': product_code},
        {'$set': {
            'purchase_stock': new_purchase_stock,
            'sales_stock': new_sales_stock,
            'current_stock': new_current_stock,
        }}
    )

@app.route('/sales')
def sales():
    sales = mongo.db.sales.find()
    return render_template('sales.html', sales=sales)

@app.route('/add_sales', methods=['POST'])
def add_sales():
    if request.method == 'POST':
        date = datetime.now()
        customer_name = request.form['customer_name']
        product_code = request.form['product_code']
        quantity = int(request.form['quantity'])
        price = request.form['price']

        mongo.db.sales.insert_one({
            'customer_name': customer_name,
            'product_code': product_code,
            'quantity': quantity,
            'price': price,
            'date': date
        })

        update_stock(product_code, 0, quantity)

        return redirect(url_for('sales'))

def initialize_stock(product_code, opening_stock):
    # Check if stock details already exist for the product
    existing_stock = mongo.db.stocks.find_one({'product_code': product_code})

    if not existing_stock:
        # If no stock details exist, insert a new document with the initial stock values
        mongo.db.stocks.insert_one({
            'product_code': product_code,
            'opening_stock': opening_stock,
            'purchase_stock': 0,
            'sales_stock': 0,
            'current_stock': opening_stock,
        })

@app.route('/stock')
def stock():
    stock_details = mongo.db.stocks.find()
    return render_template('stock.html', stock_details=stock_details)

if __name__ == '__main__':
    app.run(debug=True)