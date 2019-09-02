#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restplus import Api, Resource, fields, reqparse

from . import TwitterProfiling

app = Flask(__name__, static_url_path='')
CORS(app)

api = Api(app=app, version="0.1.0", title="TwitterProfiling", description="Service for the TwitterProfiling API")
api_namespace = api.namespace("api", description="Api points")

input_model = api.model('Input model', {
    'consumer-key': fields.String(description="Consumer key",
                                  example="aaaaaaaaaaaaaaaaaaaaaaaaa"),
    'consumer-secret': fields.String(description="Consumer secret",
                                     example="bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"),
    'access-token': fields.String(description="Access token",
                                  example="cccccccccccccccccccccccccccccccccccccccccccccccccc"),
    'access-token-secret': fields.String(description="Access token secret",
                                         example="ddddddddddddddddddddddddddddddddddddddddddddd"),
    'user-name': fields.String(description="Twitter user name",
                               example="sciencemagazine"),
    'number-of-tweets': fields.Integer(description="Maximum number of tweets to recover",
                                       example=1200
                                       )
})

output_model = api.model('Output model', {
    'description': fields.String(description="Description in the Twitter account of the user",
                                 example="45th President of the United States of America🇺🇸"),
    'classification': fields.Raw(description="Mapping of categories to a score",
                                 example={
                                     "News and Politics": 21.437,
                                     "Financial and Business": 10.596,
                                     "Sports": 8.489,
                                 }),
})


@api_namespace.route('')
class NewPrediction(Resource):
    @api.expect(input_model)
    @api.marshal_with(output_model, code=200, description='OK')
    def post(self):
        """Fetch tweets from a user and find the relevant categories
        """
        args = [request.json['user-name'], request.json['consumer-key'], request.json['consumer-secret'],
                request.json['access-token'], request.json['access-token-secret']]
        kwargs = {"number_of_tweets": request.json['number-of-tweets']} if 'number-of-tweets' in request.json else {}
        cat = TwitterProfiling(*args, **kwargs)

        return {"description": cat.get_user_description(), "classification": cat.get_user_classification()}


def main():
    app.run(debug=False, host='0.0.0.0')


if __name__ == '__main__':
    main()
