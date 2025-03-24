from libs.JsonFileFactory import JsonFileFactory


class Book:
    FILE_PATH = "../dataset/books.json"

    def __init__(self, book_id, book_name, type, published_year, publisher, price, quantity, author=""):
        self.book_id = book_id
        self.book_name = book_name
        self.type = type
        self.published_year = published_year
        self.publisher = publisher
        self.price = price
        self.quantity = quantity
        self.author = author
    def __str__(self):
        return f"{self.book_id}\t{self.quantity}"

    @staticmethod
    def get_all_books():
        return JsonFileFactory.read_data(Book.FILE_PATH,Book)