from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'my store 1',
        'items': [
            {
                'name': 'store 1 item 1',
                'price': 230
            },
            {
                'name': 'store 1 item 2',
                'price': 250
            }
        ]
    },
    {
        'name': 'my store 2',
        'items': [
            {
                'name': 'store 2 item 1',
                'price': 270
            },
            {
                'name': 'store 2 item 2',
                'price': 290
            }
        ]
    }
]
@app.route('/')
def home():
    return 'Hello Customer!'

# GET - gets all the stores
@app.route('/stores')
def list_all_stores():
    return jsonify(stores)

# GET - gets all the items in a particular store
@app.route('/stores/<string:name>')
def store(name):
    for store in stores:
        if store['name'] == name:
            return store
    return 'this store is not present'

# GET - gets a particular item in a particular store
@app.route('/stores/<string:store_name>/<string:item_name>')
def item(store_name, item_name):
    for store in stores:
        if store['name'] == store_name:
            for item in store['items']:
                if item['name'] == item_name:
                    return item
    return 'this item is not present in this store'

# POST - create a store in our list of stores
@app.route('/stores', methods = ['POST'])
def add_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(stores)

# POST - add item in a particular store
@app.route('/stores/<string:store_name>', methods = ['POST'])
def add_item(store_name):
    request_data = request.get_json()
    new_item = {
        'name': request_data['name'],
        'price': request_data['price']
    }
    for store in stores:
        if store['name'] == store_name:
            store['items'].append(new_item)
    return jsonify(stores)



app.run(port = 5000)
