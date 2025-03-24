from libs.JsonFileFactory import JsonFileFactory


class Author:
    FILE_PATH = "../dataset/authors.json"

    def __init__(self, author_id=None, name=None, gender=None,hometown=None,book_count=0, books=[]):
        self.author_id = author_id
        self.name = name
        self.gender = gender
        self.hometown = hometown
        self.book_count = book_count
        self.books = books


    @staticmethod
    def get_all_authors():
        return JsonFileFactory.read_data(Author.FILE_PATH,Author)