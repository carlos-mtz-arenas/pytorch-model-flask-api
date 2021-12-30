import flask

from flask import jsonify
from flask_restful import Api
from api import DogAPI

import sys
import os
from uuid import uuid4 as uuid


app = flask.Flask("dog-feeder-api")


@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "probably try /dogs instead"})


@app.errorhandler(Exception)
def handle_500(e):
    """
    Handles all the errors from the server and
    applys a JSON format for the response
    """
    return jsonify({"error": True, "message": str(e)}), 500


# create the API
api = Api(app)

api.add_resource(DogAPI, '/dogs')

if __name__ == '__main__':
    app.run(debug=True)
