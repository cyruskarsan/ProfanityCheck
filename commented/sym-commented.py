#!/usr/bin/env python
from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
import json
from censor import check

app = Flask(__name__)
api = Api(app)

class Word(Resource):
    def get(self):
    	explicts = []
    	explicts.append(text)
    	dictExplict = dict.fromkeys(explicts, 'explicts')
    	return dictExplict, 200

api.add_resource(Word, "/word")

class Send(Resource):
	def get(self):
		return request.json,201

	def post(self):
		if not request.json:
			abort(400)
		data = request.get_json()
		response = check(data)
		#run through the check function
		#result of the check function as a new object
		return response, 201

api.add_resource(Send, "/send")

app.run(debug=True)