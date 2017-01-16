from flask import request, jsonify
from ..blueprint import api
from middleware import token_verification

@api.route('/user/me')
@token_verification
def me():
    current_user = request.current_user['user']
    return jsonify(current_user)
