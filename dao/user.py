import hashlib
import base64
import hmac
from config import Config
from .model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def create(self, user_data):
        usr = User(**user_data)
        self.session.add(usr)
        self.session.commit()
        return usr

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).one_or_none()

    def generate_password_digest(self, password):
        return hashlib.pbkdf2_hmac(
            hash_name='sha256',
            password=password.encode('utf-8'),
            salt=Config.PWD_SALT,
            iterations=Config.PWD_ITERATIONS,
        )

    def get_hash(self, password):
        return base64.b64encode(self.generate_password_digest(password)).decode('utf-8')

    # def get_hash(self, password):
    #     return hashlib.pbkdf2_hmac(
    #         'sha256',
    #         password.encode('utf-8'),
    #         Config.PWD_SALT,
    #         Config.PWD_ITERATIONS,
    #     ).decode('utf-8', 'ignore')

    def compare_passwords(self, password_hash, other_password):
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac(
                'sha256',
                other_password.encode('utf-8'),
                Config.PWD_SALT,
                Config.PWD_ITERATIONS,
            )
        )
