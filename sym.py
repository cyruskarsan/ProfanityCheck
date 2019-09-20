#!/usr/bin/env python
from flask import Flask, jsonify, request, abort
from flask_restful import Api, Resource, reqparse
import json
from censor import check
import sqlite3

app = Flask(__name__)
api = Api(app)

#Used to interact and modify the SQL database
class Explict(Resource):
	#displays all the id's and words for the 'explicts' table in the database
	def get(self):
		#connect to db
		con = sqlite3.connect('symbaloo.db')
		cursorObj = con.cursor()

		#retreieving all values from database
		sql = 'SELECT * FROM explicts'
		cursorObj.execute(sql)
		result = (cursorObj.fetchall())

		#commiting changes and closing connection
		con.commit()
		con.close()
		return result

	#inserting an explict word into the database
	def post(self):
		#connect to db
		con = sqlite3.connect('symbaloo.db')
		cursorObj = con.cursor()

		#setting up the HTTP request parameters
		parser = reqparse.RequestParser(bundle_errors=True)
		parser.add_argument("id", type=str, required = True)
		parser.add_argument("word",type=str, required = True)
		args = parser.parse_args()

		#adding to the database with data specified in request
		cursorObj.execute("CREATE TABLE IF NOT EXISTS explicts(id integer, word text)")
		data = (args["id"], args["word"])
		cursorObj.execute('INSERT INTO explicts(id,word) VALUES(?,?)', data)

		#close the connection and return the message
		con.commit()
		con.close()
		insert = {
		"insert status" : "success",
		"id" : args["id"],
		"word": args["word"]
		}
		return insert

	#updating a forbidden word in the database using its key
	def put(self):
		#connect to db
		con = sqlite3.connect('symbaloo.db')
		cursorObj = con.cursor()

		#setting up the HTTP request parameters
		parser = reqparse.RequestParser(bundle_errors=True)
		parser.add_argument("id", type=str, required = True)
		parser.add_argument("word",type=str, required = True)
		args = parser.parse_args()

		#updating the database with the data specified in the HTTP request
		key = args["word"]
		word= args["id"]
		sql = "UPDATE explicts SET word = ? WHERE id = ?"
		data = (args["word"], args["id"])
		cursorObj.execute(sql,data)
		con.commit()
		con.close()

		#message to be returned
		update = {
		"update status" : "success",
		"id" : args["id"],
		"word": args["word"]
		}
		return update

	#deleting a forbidden word in the database using its key
	def delete(self):
		#connecting to the db
		con = sqlite3.connect('symbaloo.db')
		cursorObj = con.cursor()

		#setting up arguments for HTTP request
		parser = reqparse.RequestParser(bundle_errors=True)
		parser.add_argument("id", type=str, required = True)
		args = parser.parse_args()

		#deleting the item in the db based on id
		sql = 'DELETE FROM explicts WHERE id = ?'
		data = args["id"]
		cursorObj.execute(sql,data)

		#selecting the remaining entries in database
		sql = 'SELECT * FROM explicts'
		cursorObj.execute(sql)
		result = (cursorObj.fetchall())

		#commiting changes and closing db
		con.commit()
		con.close()
		return result
		
#Used to run the profanity check
class Send(Resource):
	def post(self):
		#ensuring we get the correct input
		if not request.json or not 'webmixes' in request.json:
			abort(400)
		data = request.get_json()

		#connecting to the database with explict words
		con = sqlite3.connect('symbaloo.db')
		cursorObj = con.cursor()
		cursorObj.execute('SELECT word FROM explicts')
		badWords = []
		rows = cursorObj.fetchall()

		#since row is a tuple, add only the first element which is the value
		for row in rows:
			badWords.append(row[0])

		#run through the check function and store returned object as result
		response = check(data, badWords)
		
		#commit and close the database
		con.commit()
		con.close()
		return response, 201
		
api.add_resource(Send, "/send")
api.add_resource(Explict, "/explict", endpoint='database')

app.run()