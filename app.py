from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products


@app.route('/products')
def getProducts():
    return jsonify({"products": products, "message": "Product's list"})


@app.route('/product/<string:product_name>')
def getProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        return jsonify({"product": productFound[0]})
    return jsonify({"messge": "Product not found"})


@app.route('/product/addProduct', methods=['POST'])
def addProduct():
    newProduct = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(newProduct)
    return jsonify({"message": "Product added succesfully", "products": products})


@app.route('/product/editProduct/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "Product Update",
            "Product": productFound[0]
        })
    return jsonify({"message": "Product not found"})


@app.route('/product/delProduct/<string:product_name>', methods=['DELETE'])
def delProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        products.remove(productFound[0])
        return jsonify({
            "message": "Product deleted",
            "Product": products
        })
    return jsonify({"message": "Product not found"})


if __name__ == '__main__':
    app.run(debug=True, port=4000)
