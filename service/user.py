from dao.model.user import UserSchema
from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_by_email(self, email):
        usr = self.dao.get_by_email(email)
        return UserSchema().dump(usr)

    def create(self, user_data):
        user_password = user_data['password']
        if user_password:
            user_data['password'] = self.dao.get_hash(user_password)
        usr = self.dao.create(user_data)
        return UserSchema().dump(usr)

    def compare_passwords(self, password, other_password):
        password_hash = self.dao.get_hash(other_password)
        return self.dao.compare_passwords(password, password_hash)

