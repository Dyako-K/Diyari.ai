# Description: This file contains the account blueprint for the API.
# The blueprint is registered in the app.py file.
from flask import jsonify, Blueprint, make_response

# Create a blueprint for the account API
account = Blueprint('account', __name__)

# This is a test route to check if the blueprint is working.
@account.route('/account', methods=['POST'])
def test():
    data = {'message': 'Hello, World!'}
    response = make_response(jsonify(data), 200)
    response.mimetype = 'application/json'
    return response