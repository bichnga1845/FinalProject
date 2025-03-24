from libs.JsonFileFactory import JsonFileFactory


class User:
    FILE_PATH = "../dataset/users.json"
    def __init__(self, username, password, name=None,gender=None,date=None,phone=None,address=None,role="user"):
        self.username = username
        self.password = password
        self.name = name
        self.phone = phone
        self.gender = gender
        self.date=date
        self.address = address
        self.role=role
    def __str__(self):
        return f"{self.username}\t{self.password}\t{self.name}\t{self.phone}\t{self.email}\t{self.address}"

    @staticmethod
    def get_all_users():
        return JsonFileFactory.read_data(User.FILE_PATH,User)