from libs.JsonFileFactory import JsonFileFactory
from models.Reader import Reader


class ReaderController:
    readers_file = "../dataset/readers.json"

    @staticmethod
    def get_all_readers():
        return JsonFileFactory.read_data(ReaderController.readers_file,Reader)

    @staticmethod
    def generate_reader_id():
        readers = ReaderController.get_all_readers()
        reader_ids = [int(reader.reader_id) for reader in readers if isinstance(reader, Reader)]
        return max(reader_ids) + 1 if reader_ids else 1

    @staticmethod
    def get_reader_by_id(reader_id):
        readers = ReaderController.get_all_readers()
        for reader in readers:
            if reader.reader_id == int(reader_id):
                return reader
        return None

    @staticmethod
    def get_reader_by_name(name):
        if not isinstance(name, str) or not name.strip():
            return None

        readers = ReaderController.get_all_readers()
        for reader in readers:
            if reader.name.strip().lower() == name.strip().lower():
                return reader
        return None

    @staticmethod
    def search_readers(query):
        readers = ReaderController.get_all_readers()
        query = query.lower()
        return [reader for reader in readers if query in reader.name.lower()]

    @staticmethod
    def add_order_book_to_reader(reader_id, book_id, quantity):
        readers = ReaderController.get_all_readers()

        for reader in readers:
            if reader.reader_id == reader_id:
                # Kiểm tra xem sách đã có trong danh sách chưa
                for i, (b_id, qty) in enumerate(reader.books):
                    if b_id == book_id:
                        reader.books[i] = (b_id, qty + quantity)  # Cập nhật số lượng
                        break
                else:
                    reader.books.append((book_id, quantity))  # Thêm mới nếu chưa có

                break

        JsonFileFactory.write_data(readers, ReaderController.readers_file)

    @staticmethod
    def remove_order_book_from_reader(reader_id, book_id, quantity_to_remove):
        readers = ReaderController.get_all_readers()

        for reader in readers[:]:
            if reader.reader_id == reader_id:
                # Tạo danh sách mới
                new_books = []
                for book_tuple in reader.books:
                    if book_tuple[0] == book_id:  # Nếu đúng sách bị xóa
                        new_quantity = book_tuple[1] - quantity_to_remove
                        if new_quantity > 0:  # Vẫn còn sách, giữ lại
                            new_books.append((book_id, new_quantity))
                    else:
                        new_books.append(book_tuple)  # Giữ nguyên các sách khác

                reader.books = new_books
                JsonFileFactory.write_data(readers, ReaderController.readers_file)  # Lưu thay đổi vào file
                return

    @staticmethod
    def update_order_book_to_reader(reader_id, book_id, new_quantity, old_quantity):
        readers = ReaderController.get_all_readers()

        for reader in readers:
            if reader.reader_id == reader_id:
                for i, (b_id, qty) in enumerate(reader.books):
                    if b_id == book_id:
                        quantity=qty+new_quantity-old_quantity
                        if quantity > 0:
                            reader.books[i] = (b_id, quantity)
                        else:
                            reader.books.pop(i)  # Xóa nếu không còn sách
                        break
                else:
                    if new_quantity > 0:
                        reader.books.append((book_id, new_quantity))  # Thêm sách mới nếu chưa có

                # Lưu lại dữ liệu vào file
                JsonFileFactory.write_data(readers, ReaderController.readers_file)
                return