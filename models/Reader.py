from libs.JsonFileFactory import JsonFileFactory


class Reader:
    FILE_PATH = "../dataset/readers.json"
    def __init__(self,reader_id=None,name=None,gender=None,date=None,phone=None,address=None,books=[]):
        self.reader_id=reader_id
        self.name=name
        self.gender=gender
        self.date=date
        self.phone=phone
        self.address=address
        self.books=books

    @staticmethod
    def get_all_readers():
        return JsonFileFactory.read_data(Reader.FILE_PATH, Reader)