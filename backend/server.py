import mysql.connector
import json
from flask import Flask, request, jsonify
from sql_connection import get_sql_connection

import productsDao
import ordersDao
import uomDao

app = Flask(__name__)
connection = get_sql_connection()

@app.route('/getAllOrders', methods=['GET'])
def getAllOrders():
    response = ordersDao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getProducts', methods=['GET'])
def getProducts():
    response = productsDao.get_all_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insertProduct():
    request_payload = json.loads(request.form['data'])
    product_id = productsDao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getUOM', methods=['GET'])
def getUom():
    response = uomDao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insertOrder():
    request_payload = json.loads(request.form['data'])
    order_id = ordersDao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods=['POST'])
def deleteProduct():
    return_id = productsDao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Initializing Server.")
    app.run(port=5000)

