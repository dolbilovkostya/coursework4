from service.user import UserService
import datetime
import calendar
import jwt
from flask import abort
from config import Config


class AuthService:
    def __init__(self, user_service):
        self.user_service = user_service

    def generate_tokens(self, email, password):
        user = self.user_service.get_by_email(email)

        if user is None:
            abort(404)

        if not self.user_service.compare_passwords(user.password, password):
            abort(400)

        data = {
            'email': email,
            'password': password,
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, Config.SECRET_HERE, algorithm=Config.JWT_ALGO)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, Config.SECRET_HERE, algorithm=Config.JWT_ALGO)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
        }

