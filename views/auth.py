from flask import request
from flask_restx import abort, Namespace, Resource

from implemented import user_service, auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/register')
class AuthRegisterView(Resource):
    def post(self):
        data = request.json
        return user_service.create(data)


@auth_ns.route('/login')
class AuthLoginView(Resource):
    def post(self):
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            abort(400)

        tokens = auth_service.generate_tokens(email=email, password=password)

        return tokens, 201


