from controller.author_controller import AuthorController
from libs.JsonFileFactory import JsonFileFactory
from models.Book import Book


class BookController:
    books_file = "../dataset/books.json"
    authors_file = "../dataset/authors.json"

    @staticmethod
    def get_all_books():
        books = JsonFileFactory.read_data(BookController.books_file,Book)
        return books

    @staticmethod
    def get_book_by_id(book_id):
        books = BookController.get_all_books()
        return next((book for book in books if book.book_id == book_id), None) #Tra ve phan tu dau tien thoa man
        #books = BookController.get_all_books()
        #for book in books:
            #if book.book_id == book_id:
                #return book
        #return None

    @staticmethod
    def get_book_by_name(book_name):
        books = BookController.get_all_books()
        for book in books:
            if book.book_name == book_name:
                return book
        return None

    @staticmethod
    def search_books(query):
        books = BookController.get_all_books()
        query = query.lower()

        if not query:
            return books

        return [
            book for book in books
            if query in book.book_name.lower() or
               query in book.author.lower()
        ]

