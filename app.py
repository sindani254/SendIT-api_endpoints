from flask import Flask, jsonify, abort, make_response, request

NOT_FOUND = 'data NOT found'
BAD_REQUEST = 'Bad request'

app = Flask(__name__)

parcels = [
    {
        'id': 1,
        'owner_id': 1,
        'item_name': 'Geforce GTX 1060 iGame',
        'origin': 'nairobi cbd',
        'pickup_location': 'zimmerman base',
        'price': 45000,
        'status': 'delivered'
    },
    {
        'id': 2,
        'owner_id': 2,
        'item_name': 'Geforce GTX 1080 ti',
        'origin': 'nairobi cbd',
        'pickup_location': 'zimmerman base',
        'price': 105000,
        'status': 'in transit'
    },
    {
        'id': 3,
        'owner_id': 1,
        'item_name': 'Geforce GTX 1050 ti',
        'origin': 'nairobi cbd',
        'pickup_location': 'base',
        'price': 85000,
        'status': 'cancelled'
    }
]


def _get_order(id):
    return [parcel for parcel in parcels if parcel['id'] == id]


def _entry_exists_for_delivery_order(item_name):
    return [parcel for parcel in parcels if parcel["item_name"] == item_name]


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': NOT_FOUND}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': BAD_REQUEST}), 400)


@app.route('/api/v1')
def index():
    return jsonify({"welcome": "crackers ni wale wase"})


@app.route('/api/v1/parcels', methods=['GET'])
def get_all_parcel_orders():
    return jsonify({'all orders': parcels})


if __name__ == '__main__':
    app.run(debug=True)
