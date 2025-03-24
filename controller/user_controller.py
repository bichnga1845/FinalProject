from libs.JsonFileFactory import JsonFileFactory
from models.User import User


class UserController:
    current_user=None

    @staticmethod
    def login(username, password):
        users = JsonFileFactory.read_data("../dataset/users.json",User)

        for user in users:
            if user.username == username and user.password == password:
                UserController.current_user = user
                return True, user.role
        return False, None

    @staticmethod
    def change_password(username, new_password):
        users = JsonFileFactory.read_data("../dataset/users.json",User)

        found = False
        for user in users:
            if user.username == username:
                user.password = new_password
                found = True
                break

        if not found:
            return False, "Can't find user!"

        JsonFileFactory.write_data(users, "../dataset/users.json")
        return True, "Password change success!"

    @staticmethod
    def logout():
        UserController.current_user = None
