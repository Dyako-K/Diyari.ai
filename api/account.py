# Description: This file contains the account blueprint for the API.
# The blueprint is registered in the app.py file.
from flask import jsonify, Blueprint, make_response

# Create a blueprint for the account API
account = Blueprint('account', __name__)

# Define a route for the account API
@account.route('/account', methods=['GET'])
def get_account():
    return '', 200