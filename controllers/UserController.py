from flask import request, Blueprint, jsonify
from service.UserService import UserService
from service.UserService import user_schema, users_schema
from models.User import User

user = Blueprint('user', __name__)
user_serv = UserService()

@user.route('/new', methods=['POST'])
def create_user()-> User: 
    username = request.json['username']
    email = request.json['email']
    new_user = User(username, email)
    return user_schema.jsonify(user_serv.create_user(username,email))

@user.route('/list/all', methods=['GET'])
def list_users():
    result = users_schema.dump(user_serv.list_users())
    return jsonify(result)

@user.route('/user', methods=['GET'])
def find_by_id():
    id = request.args.get('id')
    return user_schema.jsonify(user_serv.find_by_id(id))

@user.route('/update', methods=['PUT'])
def update():
    id = request.json['id']
    username = request.json['username']
    email = request.json['email']
    update_user = User(username, email,id)
    return user_schema.jsonify(user_serv.update(update_user))

@user.route('/delete', methods=['DELETE'])
def delete():
    id = request.args.get('id')
    return user_schema.jsonify(user_serv.delete(id))