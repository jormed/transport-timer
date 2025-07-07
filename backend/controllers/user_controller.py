from flask import Blueprint, jsonify, request
from services.user_service import UserService

user_api = Blueprint('user_api', __name__)
service = UserService()

@user_api.route('/api/users', methods=['GET'])
def get_users():
    print("aca estoy")
    users = service.users_list()
    return jsonify([{"id": u.id, "name": u.name} for u in users])