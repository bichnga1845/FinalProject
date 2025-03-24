from libs.JsonFileFactory import JsonFileFactory
from models.Author import Author


class AuthorController:
    authors_file = "../dataset/authors.json"

    @staticmethod
    def get_next_author_id():
        authors = AuthorController.get_all_authors()  # Lấy danh sách tác giả (dạng list[Author])
        author_ids = [int(author.author_id) for author in authors if isinstance(author, Author)]
        return max(author_ids) + 1 if author_ids else 100

    @staticmethod
    def get_all_authors():
        return JsonFileFactory.read_data(AuthorController.authors_file,Author)

    @staticmethod
    def get_author_by_id(author_id):
        authors = AuthorController.get_all_authors()
        for author in authors:
            if author.author_id == author_id:
                return author
        return None

    @staticmethod
    def get_author_by_name(name):
        if not isinstance(name, str) or not name.strip():
            return None

        authors = AuthorController.get_all_authors()
        for author in authors:
            if author.name.strip().lower() == name.strip().lower():
                return author
        return None

    @staticmethod
    def search_authors(query):
        authors = AuthorController.get_all_authors()
        query = query.lower()
        return [author for author in authors if query in author.name.lower()]

    @staticmethod
    def add_author_to_book(name):
        authors = AuthorController.get_all_authors()
        """existing_author = AuthorController.get_author_by_name(name)

        if existing_author:
            return False"""

        new_author = Author(author_id=None,name=name)
        authors.append(new_author)

        JsonFileFactory.write_data(authors, AuthorController.authors_file)

        return True

    @staticmethod
    def add_book_to_author(author_name, book_name):
        authors = AuthorController.get_all_authors()

        for author in authors:
            if author.name == author_name:
                if book_name not in author.books:
                    author.books.append(book_name)
                    author.book_count = len(author.books)
                    break

        JsonFileFactory.write_data(authors, AuthorController.authors_file)

    @staticmethod
    def remove_book_from_author(author_name, book_name):
        authors = AuthorController.get_all_authors()

        for author in authors[:]:
            if author.name == author_name:
                author.books = [book for book in author.books if book != book_name] #Tao list moi
                                                                            #ko chua book_id can xoa
                author.book_count = len(author.books)

                if author.book_count < 0:
                    authors.remove(author)

                JsonFileFactory.write_data(authors, AuthorController.authors_file)
                return
