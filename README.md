# Web Stock Maintenance System

This project is a Stock Maintenance System designed to manage product details, purchases, sales, and stock levels. It provides a user-friendly interface for data entry and real-time updates on stock movements.

## Aim
The aim of this web application is to create a Stock Maintenance System that facilitates the management of product details, purchases, sales, and stock levels. The primary objectives include providing a user-friendly interface for data entry, real-time updates on stock movements using HTML and DHTML, and incorporating various web technologies.

## Required Web Tools and Methodology
- **Web Development Framework:** Flask (Python)
- **Database:** MongoDB
- **Frontend:** HTML, CSS, Jinja2 (template engine for Flask)
- **Charting Library:** Chart.js
- **Version Control:** Git

## Implementation Procedure
1. **Database Design:** Defined MongoDB collections for products, purchases, sales, and stock. Established relationships between these collections.
2. **Backend Development:** Used Flask to create routes for adding and retrieving data. Implemented functions to update stock levels based on purchases and sales.
3. **Frontend Development:** Created HTML templates for product, purchase, sales, and stock pages. Used CSS for styling and layout. Integrated Chart.js for dynamic statistics.
4. **User Interface:** Implemented internal hyperlinking for seamless navigation between different sections of the web application. Designed forms for inputting product details, purchase information, and sales data. Implemented tables to display structured data, such as product details and stock information. Incorporated dynamic charts for statistics.

## Code Snippets
```python
# Sample Python code using Flask for web routes
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/stock_db'
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')
```

## Conclusion
The Stock Maintenance System successfully fulfills its objectives, offering an efficient and organized solution for businesses to manage their stock data. The use of Flask, MongoDB, and other web technologies ensures scalability and adaptability for future enhancements.
