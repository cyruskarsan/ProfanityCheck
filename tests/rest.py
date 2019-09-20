#!/usr/bin/env python
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "T",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    }
]

class User(Resource):
    #Get's the information of the requested user
    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404


    #Add the information of the user if user has not been created
    def post(self, name):
        parser = reqparse.RequestParser()
        #Adding age and occupation arguments
        parser.add_argument("age")
        parser.add_argument("occupation")
        #storing arguements
        args = parser.parse_args()

        #check if the person we are attempting to add already exists, 400 exits 
        for user in users:
            if(name == user["name"]):
                return "User with name " + name + " already exists", 400

        #otherwise we are adding the user
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    #updates a user if already created, otherwise adds it
    def put(self, name):
        parser = reqparse.RequestParser()
        #Adding age and occupation arguments
        parser.add_argument("age")
        parser.add_argument("occupation")
        #storing arguements
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        #otherwise we are adding the user
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user,201

    #delete
    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return name + " is deleted", 200

api.add_resource(User, "/user/<string:name>")

app.run(debug=True)