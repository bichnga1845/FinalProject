from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox, QMainWindow

from controller.author_controller import AuthorController
from controller.book_controller import BookController
from controller.order_controller import OrderController
from controller.reader_controller import ReaderController
from controller.user_controller import UserController
from libs.ExportExcelTool import ExportImportExcelTool
from libs.JsonFileFactory import JsonFileFactory
from models.Author import Author
from models.Book import Book
from models.Order import Order
from models.Reader import Reader
from ui.AuthorDetailWindowExt import AuthorDetailWindowExt
from ui.ManagementWindow import Ui_MainWindow
from ui.OrderDetailWindowExt import OrderDetailWindowExt
from ui.ReaderDetailWindowExt import ReaderDetailWindowExt


class ManagementWindowExt(Ui_MainWindow):
    def __init__(self):
        self.all_authors = Author.get_all_authors()  # Danh sách gốc
        self.authors = self.all_authors[:]  # Tạo bản sao để thao tác

        self.all_books=Book.get_all_books()
        self.books=self.all_books[:]

        self.all_readers=Reader.get_all_readers()
        self.readers=self.all_readers[:]

        self.orders = OrderController.get_all_orders()

    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.show_authors_ui()
        self.show_books_ui()
        self.show_readers_ui()
        self.load_orders()

        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonSearchAuthor.clicked.connect(self.process_search_author)
        self.pushButtonShowAllAuthor.clicked.connect(self.process_show_all_author)
        self.pushButtonAddAuthor.clicked.connect(self.process_add_author)
        self.pushButtonDeleteAuthor.clicked.connect(self.process_delete_author)
        self.tableWidgetAuthor.cellClicked.connect(self.open_author_detail)
        self.pushButtonUpdateAuthor.clicked.connect(self.process_update_author)
        self.tableWidgetAuthor.itemSelectionChanged.connect(self.show_author_detail)

        self.pushButtonSearchBook.clicked.connect(self.process_search_book)
        self.pushButtonShowAllBook.clicked.connect(self.process_show_all_book)
        self.pushButtonAddBook.clicked.connect(self.process_add_book)
        self.pushButtonDeleteBook.clicked.connect(self.process_delete_book)
        self.pushButtonUpdateBook.clicked.connect(self.process_update_book)
        self.tableWidgetBook.itemSelectionChanged.connect(self.show_book_detail)

        self.pushButtonSearchReader.clicked.connect(self.process_search_reader)
        self.pushButtonShowAllReader.clicked.connect(self.process_show_all_reader)
        self.pushButtonAddReader.clicked.connect(self.process_add_reader)
        self.pushButtonDeleteReader.clicked.connect(self.process_delete_reader)
        self.pushButtonUpdateReader.clicked.connect(self.process_update_reader)
        self.tableWidgetReader.itemSelectionChanged.connect(self.show_reader_detail)
        self.tableWidgetReader.cellClicked.connect(self.open_reader_detail)

        self.pushButtonAddOrder.clicked.connect(self.process_add_order)
        self.tableWidgetBorrowAndReturn.cellClicked.connect(self.open_order_detail)
        self.tableWidgetBorrowAndReturn.itemSelectionChanged.connect(self.show_order_detail)
        self.pushButtonDeleteOrder.clicked.connect(self.process_delete_order)
        self.pushButtonUpdateOrder.clicked.connect(self.process_update_order)

        self.actionLog_Out.triggered.connect(self.process_log_out)
        self.actionExport_All.triggered.connect(self.export_all_data_excel)
        self.actionExport_Book_Data.triggered.connect(self.export_book_data_excel)
        self.actionExport_Reader_Data.triggered.connect(self.export_reader_data_excel)
        self.actionExport_Author_Data.triggered.connect(self.export_author_data_excel)
        self.actionExport_Order_Data.triggered.connect(self.export_order_data_excel)

    #Xu ly giao dien Author
    def show_authors_ui(self):
        #remove existing authors from QTableWidget
        self.tableWidgetAuthor.setRowCount(0)
        #add author into table by iterator
        for author in self.authors:
            #get number of rows (meaning: last row)
            row=self.tableWidgetAuthor.rowCount()
            #insert new row (last row)
            self.tableWidgetAuthor.insertRow(row)
            author_id = QTableWidgetItem(author.author_id)
            author_name = QTableWidgetItem(author.name)
            author_gender = QTableWidgetItem(author.gender)
            author_hometown = QTableWidgetItem(author.hometown)

            #set cell for row
            self.tableWidgetAuthor.setItem(row, 0, author_id)
            self.tableWidgetAuthor.setItem(row, 1, author_name)
            self.tableWidgetAuthor.setItem(row, 2, author_gender)
            self.tableWidgetAuthor.setItem(row, 3, author_hometown)
    def process_search_author(self):
        query=self.lineEditSearchAuthor.text().strip().lower()
        self.authors=AuthorController.search_authors(query)
        self.show_authors_ui()
    def process_show_all_author(self):
        self.authors = self.all_authors[:]
        self.show_authors_ui()
    def process_add_author(self):
        author_id=self.lineEditAuthorIDAuthor.text()
        name=self.lineEditAuthorNameAuthor.text()
        gender=self.lineEditGenderAuthor.text()
        hometown=self.lineEditHometownAuthor.text()

        if not author_id:
            QMessageBox.warning(self.MainWindow, "Error", "Author ID cannot be empty!")
            return
        if not name:
            QMessageBox.warning(self.MainWindow, "Error", "Author Name cannot be empty!")
            return

        author=Author(author_id,name,gender,hometown)

        #Chech exist
        existing_author = AuthorController.get_author_by_name(author.name)
        existing_author_id = AuthorController.get_author_by_id(author.author_id)
        if existing_author:
            QMessageBox.warning(self.MainWindow, "Error", "Author already exists!")
            return
        if existing_author_id:
            QMessageBox.warning(self.MainWindow, "Error", "Author ID already exists!")
            return

        self.all_authors.append(author)
        self.authors = self.all_authors[:]
        JsonFileFactory.write_data(self.authors, AuthorController.authors_file)
        self.show_authors_ui()
    def process_delete_author(self):
        row=self.tableWidgetAuthor.currentRow()
        if row==-1:
            return
        msg = QMessageBox(self.MainWindow)
        msg.setText("Do you want to delete?")
        msg.setWindowTitle("Delete confirmation")
        msg.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msg.setStandardButtons(buttons)
        result = msg.exec()
        if result == QMessageBox.StandardButton.No:
            return

        author_to_delete = self.authors[row]
        self.authors.pop(row)
        self.all_authors = [a for a in self.all_authors if a.name != author_to_delete.name]
        self.authors = self.all_authors[:]
        JsonFileFactory.write_data(self.authors, AuthorController.authors_file)
        self.show_authors_ui()
    def open_author_detail(self, row,column):
        if column == 1:
            author_name = self.tableWidgetAuthor.item(row, 1).text()
            self.author_detail_window = AuthorDetailWindowExt(author_name)
            self.author_detail_window.setupUi(QMainWindow())
            self.author_detail_window.showWindow()
    def show_author_detail(self):
        row = self.tableWidgetAuthor.currentRow()
        if row < 0:
            return
        author = self.authors[row]
        self.lineEditAuthorIDAuthor.setText(author.author_id)
        self.lineEditAuthorNameAuthor.setText(author.name)
        self.lineEditGenderAuthor.setText(author.gender)
        self.lineEditHometownAuthor.setText(author.hometown)
    def process_update_author(self):
        row = self.tableWidgetAuthor.currentRow()
        if row < 0:
            return
        author_id = self.lineEditAuthorIDAuthor.text()
        name = self.lineEditAuthorNameAuthor.text()
        gender = self.lineEditGenderAuthor.text()
        hometown = self.lineEditHometownAuthor.text()
        author=Author(author_id,name,gender,hometown)
        self.authors[row]=author
        #Cap nhat danh sach goc
        for i, a in enumerate(self.all_authors):
            if a.name == name:
                self.all_authors[i] = self.authors[row]
                break
        JsonFileFactory.write_data(self.all_authors, AuthorController.authors_file)
        self.show_authors_ui()


    #Xu ly giao dien Book
    def show_books_ui(self):

        self.tableWidgetBook.setRowCount(0)

        for book in self.books:
            #get number of rows (meaning: last row)
            row=self.tableWidgetBook.rowCount()
            #insert new row (last row)
            self.tableWidgetBook.insertRow(row)
            book_id = QTableWidgetItem(book.book_id)
            book_name = QTableWidgetItem(book.book_name)
            book_type = QTableWidgetItem(book.type)
            published_year = QTableWidgetItem(book.published_year)
            publisher = QTableWidgetItem(book.publisher)
            price = QTableWidgetItem(str(book.price))
            quantity = QTableWidgetItem(str(book.quantity))
            author = QTableWidgetItem(book.author)

            #set cell for row
            self.tableWidgetBook.setItem(row, 0, book_id)
            self.tableWidgetBook.setItem(row, 1, book_name)
            self.tableWidgetBook.setItem(row, 2, book_type)
            self.tableWidgetBook.setItem(row, 3, published_year)
            self.tableWidgetBook.setItem(row, 4, publisher)
            self.tableWidgetBook.setItem(row, 5, price)
            self.tableWidgetBook.setItem(row, 6, quantity)
            self.tableWidgetBook.setItem(row, 7, author)
    def process_search_book(self):
        query = self.lineEditSearchBook.text().strip().lower()
        self.books = BookController.search_books(query)
        self.show_books_ui()
    def process_show_all_book(self):
        self.books = self.all_books[:]
        self.show_books_ui()
    def process_add_book(self):
        self.books = self.all_books[:]

        book_id=self.lineEditBookIDBook.text().strip()
        book_name = self.lineEditBookNameBook.text().strip()
        book_type = self.lineEditTypeBook.text()
        published_year = self.dateEditPublishDateBook.date().toString("dd/MM/yyyy")
        publisher = self.lineEditPublisher.text()
        price = float(self.lineEditPriceBook.text())
        quantity = int(self.lineEditQuantityBook.text())
        author_name = self.lineEditAuthorBook.text().strip()

        if not book_id or not book_name or not author_name or not quantity or not price:
            QMessageBox.warning(self.MainWindow, "Error", "Please fill all fields!")
            return

        # Kiem tra xem book name hay book id co ton tai chua
        if any(book.book_name.strip().lower() == book_name.strip().lower() for book in self.books):
            QMessageBox.warning(self.MainWindow, "Error", "Book already exists in the system!")
            return
        if BookController.get_book_by_id(book_id) is not None:
            QMessageBox.warning(self.MainWindow, "Error", "Book ID already exists in the system!")
            return

        if author_name:
            author = AuthorController.get_author_by_name(author_name)

            #Neu author chua ton tai thi them moi
            if not author: #author tra ve none->ko co author do
                success = AuthorController.add_author_to_book(author_name)
                if success: #add thanh cong
                    author = AuthorController.get_author_by_name(author_name)

        book = Book(book_id, book_name, book_type, published_year, publisher, price, quantity, author.name)

        self.all_books.append(book)
        self.books = self.all_books[:]
        JsonFileFactory.write_data(self.books,BookController.books_file)
        self.show_books_ui()

        AuthorController.add_book_to_author(author.name, book_name)
        self.all_authors = Author.get_all_authors()
        self.authors = self.all_authors[:]
        JsonFileFactory.write_data(self.authors, AuthorController.authors_file)
        self.show_authors_ui()
    def process_delete_book(self):
        row = self.tableWidgetBook.currentRow()
        if row == -1:
            return
        msg = QMessageBox(self.MainWindow)
        msg.setText("Do you want to delete?")
        msg.setWindowTitle("Delete confirmation")
        msg.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msg.setStandardButtons(buttons)
        result = msg.exec()
        if result == QMessageBox.StandardButton.No:
            return

        book_to_delete = self.books[row]
        self.books.pop(row)
        self.all_books = [b for b in self.all_books if b.book_id != book_to_delete.book_id]
        self.books = self.all_books[:]
        JsonFileFactory.write_data(self.books, BookController.books_file)
        self.show_books_ui()

        AuthorController.remove_book_from_author(book_to_delete.author, book_to_delete.book_name)
        self.all_authors = Author.get_all_authors()
        self.authors = self.all_authors[:]
        self.show_books_ui()
        self.show_authors_ui()
    def show_book_detail(self):
        row = self.tableWidgetBook.currentRow()
        if row < 0:
            return
        book = self.books[row]
        self.lineEditBookIDBook.setText(book.book_id)
        self.lineEditBookNameBook.setText(book.book_name)
        self.lineEditTypeBook.setText(book.type)
        self.dateEditPublishDateBook.setDate(QDate.fromString(book.published_year, "dd/MM/yyyy"))
        self.lineEditPublisher.setText(book.publisher)
        self.lineEditPriceBook.setText(str(book.price))
        self.lineEditQuantityBook.setText(str(book.quantity))
        self.lineEditAuthorBook.setText(book.author)
    def process_update_book(self):
        row = self.tableWidgetBook.currentRow()
        if row < 0:
            return
        book_id = self.lineEditBookIDBook.text().strip()
        book_name = self.lineEditBookNameBook.text().strip()
        book_type = self.lineEditTypeBook.text()
        published_year = self.dateEditPublishDateBook.date().toString("dd/MM/yyyy")
        publisher = self.lineEditPublisher.text()
        price = float(self.lineEditPriceBook.text())
        quantity = int(self.lineEditQuantityBook.text())
        author_name = self.lineEditAuthorBook.text().strip()

        # Tạo đối tượng sách mới
        updated_book = Book(book_id, book_name, book_type, published_year, publisher, price, quantity, author_name)

        # Kiểm tra nếu tác giả có thay đổi
        old_book = self.books[row]
        if old_book.author != author_name:
            # Nếu tác giả thay đổi, cập nhật thông tin cho cả tác giả cũ và mới
            AuthorController.remove_book_from_author(old_book.author, old_book.book_name)  # Xóa sách khỏi tác giả cũ
            AuthorController.add_book_to_author(author_name, book_name)  # Thêm sách vào tác giả mới

        # Cập nhật sách trong danh sách
        self.books[row] = updated_book

        # Cap nhat danh sach goc
        for i, b in enumerate(self.all_books):
            if b.book_id == book_id:
                self.all_books[i] = self.books[row]
                break

        JsonFileFactory.write_data(self.all_books,BookController.books_file)
        self.show_books_ui()

        # Cập nhật thông tin tác giả
        self.all_authors = Author.get_all_authors()
        self.authors = self.all_authors[:]
        JsonFileFactory.write_data(self.authors, AuthorController.authors_file)
        self.show_authors_ui()  # Hiển thị lại danh sách tác giả


    #Xu ly giao dien Reader
    def show_readers_ui(self):

        self.tableWidgetReader.setRowCount(0)

        for reader in self.readers:
            #get number of rows (meaning: last row)
            row=self.tableWidgetReader.rowCount()
            #insert new row (last row)
            self.tableWidgetReader.insertRow(row)
            reader_id = QTableWidgetItem(str(reader.reader_id))
            reader_name = QTableWidgetItem(reader.name)
            reader_gender = QTableWidgetItem(reader.gender)
            reader_date = QTableWidgetItem(reader.date)
            reader_phone = QTableWidgetItem(reader.phone)
            reader_address = QTableWidgetItem(reader.address)

            #set cell for row
            self.tableWidgetReader.setItem(row, 0, reader_id)
            self.tableWidgetReader.setItem(row, 1, reader_name)
            self.tableWidgetReader.setItem(row, 2, reader_gender)
            self.tableWidgetReader.setItem(row, 3, reader_date)
            self.tableWidgetReader.setItem(row, 4, reader_phone)
            self.tableWidgetReader.setItem(row, 5, reader_address)
    def process_search_reader(self):
        query=self.lineEditSearchReader.text().strip().lower()
        self.readers=ReaderController.search_readers(query)
        self.show_readers_ui()
    def process_show_all_reader(self):
        self.readers = self.all_readers[:]
        self.show_readers_ui()
    def process_add_reader(self):
        reader_id=int(self.lineEditReaderIDReader.text())
        name=self.lineEditReaderNameReader.text()
        gender=self.lineEditGenderReader.text()
        phone=self.lineEditPhoneReader.text()
        address=self.lineEditAddressReader.text()
        date = self.dateEditDateReader.date().toString("dd/MM/yyyy")

        if not reader_id:
            QMessageBox.warning(self.MainWindow, "Error", "Reader ID cannot be empty!")
            return
        if not name:
            QMessageBox.warning(self.MainWindow, "Error", "Reader Name cannot be empty!")
            return

        reader=Reader(reader_id,name,gender,date,phone,address)

        #Chech exist
        existing_reader = ReaderController.get_reader_by_name(reader.name)
        existing_reader_id = ReaderController.get_reader_by_id(reader.reader_id)
        if existing_reader:
            QMessageBox.warning(self.MainWindow, "Error", "Reader already exists!")
            return
        if existing_reader_id:
            QMessageBox.warning(self.MainWindow, "Error", "Reader ID already exists!")
            return

        self.all_readers.append(reader)
        self.readers = self.all_readers[:]
        JsonFileFactory.write_data(self.readers, ReaderController.readers_file)
        self.show_readers_ui()
    def process_delete_reader(self):
        row=self.tableWidgetReader.currentRow()
        if row==-1:
            return
        msg = QMessageBox(self.MainWindow)
        msg.setText("Do you want to delete?")
        msg.setWindowTitle("Delete confirmation")
        msg.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msg.setStandardButtons(buttons)
        result = msg.exec()
        if result == QMessageBox.StandardButton.No:
            return
        reader_to_delete = self.readers[row]
        self.readers.pop(row)
        self.all_readers = [r for r in self.all_readers if r.name != reader_to_delete.name]
        self.readers = self.all_readers[:]
        JsonFileFactory.write_data(self.readers, ReaderController.readers_file)
        self.show_readers_ui()
    def show_reader_detail(self):
        row = self.tableWidgetReader.currentRow()
        if row < 0:
            return
        reader = self.readers[row]
        self.lineEditReaderIDReader.setText(str(reader.reader_id))
        self.lineEditReaderNameReader.setText(reader.name)
        self.lineEditGenderReader.setText(reader.gender)
        self.lineEditPhoneReader.setText(reader.phone)
        self.lineEditAddressReader.setText(reader.address)
        self.dateEditDateReader.setDate(QDate.fromString(reader.date, "dd/MM/yyyy"))
    def process_update_reader(self):
        row = self.tableWidgetReader.currentRow()
        if row < 0:
            return
        reader_id = int(self.lineEditReaderIDReader.text())
        name = self.lineEditReaderNameReader.text()
        gender = self.lineEditGenderReader.text()
        phone = self.lineEditPhoneReader.text()
        address = self.lineEditAddressReader.text()
        date = self.dateEditDateReader.date().toString("dd/MM/yyyy")
        reader=Reader(reader_id,name,gender,date,phone,address)
        self.readers[row]=reader
        #Cap nhat danh sach goc
        for i, r in enumerate(self.all_readers):
            if r.name == name:
                self.all_readers[i] = self.readers[row]
                break
        JsonFileFactory.write_data(self.readers, ReaderController.readers_file)
        self.show_readers_ui()
    def open_reader_detail(self,row,column):
        if column == 0 or column==1:
            reader_id = self.tableWidgetReader.item(row, 0).text()
            self.reader_detail_window = ReaderDetailWindowExt(reader_id)
            self.reader_detail_window.setupUi(QMainWindow())
            self.reader_detail_window.showWindow()


    #Xu ly giao dien Order (Borrowing/Returning)
    def load_orders(self):
        self.tableWidgetBorrowAndReturn.setRowCount(0)

        for order in self.orders:
            #get number of rows (meaning: last row)
            row=self.tableWidgetBorrowAndReturn.rowCount()
            #insert new row (last row)
            self.tableWidgetBorrowAndReturn.insertRow(row)
            order_id = QTableWidgetItem(str(order.order_id))
            reader_id = QTableWidgetItem(str(order.reader_id))
            book_id = QTableWidgetItem(order.book_id)
            quantity = QTableWidgetItem(str(order.quantity))
            borrow_date = QTableWidgetItem(order.borrow_date)
            return_date = QTableWidgetItem(order.return_date)
            status = QTableWidgetItem(order.status)

            #set cell for row
            self.tableWidgetBorrowAndReturn.setItem(row, 0, order_id)
            self.tableWidgetBorrowAndReturn.setItem(row, 1, reader_id)
            self.tableWidgetBorrowAndReturn.setItem(row, 2, book_id)
            self.tableWidgetBorrowAndReturn.setItem(row, 3, quantity)
            self.tableWidgetBorrowAndReturn.setItem(row, 4, status)
            self.tableWidgetBorrowAndReturn.setItem(row, 5, borrow_date)
            self.tableWidgetBorrowAndReturn.setItem(row, 6, return_date)
    def process_add_order(self):
        reader_id = int(self.lineEditReaderIDBR.text())
        book_id = self.lineEditBookIDBR.text()
        quantity = int(self.lineEditQuantityBR.text())
        status = self.comboBoxStatus.currentText()
        borrow_date = self.dateEditDateBorrowing.date().toString("dd/MM/yyyy")
        return_date = self.dateEditDateReturning.date().toString("dd/MM/yyyy")

        if not reader_id or not book_id or not quantity or not status:
            QMessageBox.warning(self.MainWindow, "Error", "All fields must be filled!")
            return

        if ReaderController.get_reader_by_id(reader_id) is None:
            QMessageBox.warning(self.MainWindow, "Error", "Reader is not in the system!")
            return

        # Tìm sách theo book_id
        book = next((b for b in self.all_books if b.book_id == book_id), None)

        if not book:
            QMessageBox.warning(self.MainWindow, "Error", "Book ID not found!")
            return

        if book.quantity < quantity:
            QMessageBox.warning(self.MainWindow, "Error", "Not enough books in stock!")
            return

        #Tạo Order và giảm số lượng sách
        order_id = OrderController.generate_order_id()
        order = Order(order_id, reader_id, book_id, quantity, borrow_date, return_date, status)

        self.orders.append(order)

        #Giảm số lượng sách
        book.quantity -= quantity

        #Cập nhật dữ liệu
        JsonFileFactory.write_data(self.orders, OrderController.orders_file)
        JsonFileFactory.write_data(self.all_books, BookController.books_file)  # Lưu danh sách sách mới

        #Cập nhật giao diện
        self.load_orders()
        self.show_books_ui()  # Cập nhật lại bảng sách

        ReaderController.add_order_book_to_reader(reader_id, book_id, quantity)
        self.all_readers = Reader.get_all_readers()
        self.readers = self.all_readers[:]
        JsonFileFactory.write_data(self.readers, ReaderController.readers_file)
    def open_order_detail(self,row,column):
        if column == 0:
            order_id = self.tableWidgetBorrowAndReturn.item(row, 0).text()
            self.order_detail_window = OrderDetailWindowExt(order_id)
            self.order_detail_window.setupUi(QMainWindow())
            self.order_detail_window.showWindow()
    def show_order_detail(self):
        row = self.tableWidgetBorrowAndReturn.currentRow()
        if row < 0:
            return
        order = self.orders[row]
        self.lineEditReaderIDBR.setText(str(order.reader_id))
        self.lineEditBookIDBR.setText(order.book_id)
        self.lineEditQuantityBR.setText(str(order.quantity))

        # Lấy ngày mượn và ngày trả từ bảng
        borrow_date_str = self.tableWidgetBorrowAndReturn.item(row, 5).text()
        return_date_str = self.tableWidgetBorrowAndReturn.item(row, 6).text()

        # Chuyển đổi chuỗi ngày thành QDate
        borrow_date = QDate.fromString(borrow_date_str, "dd/MM/yyyy")
        return_date = QDate.fromString(return_date_str, "dd/MM/yyyy")

        # Cập nhật vào QDateEdit
        self.dateEditDateBorrowing.setDate(borrow_date)
        self.dateEditDateReturning.setDate(return_date)

        current_status = self.tableWidgetBorrowAndReturn.item(row, 4).text()
        index = self.comboBoxStatus.findText(current_status)
        if index != -1:
            self.comboBoxStatus.setCurrentIndex(index)
    def process_delete_order(self):
        selected_row = self.tableWidgetBorrowAndReturn.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self.MainWindow, "Error", "Select order to delete!")
            return

        order_id = int(self.tableWidgetBorrowAndReturn.item(selected_row, 0).text())

        msg = QMessageBox(self.MainWindow)
        msg.setText(f"Do you want to delete {order_id}?")
        msg.setWindowTitle("Delete confirmation")
        msg.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msg.setStandardButtons(buttons)
        result = msg.exec()
        if result == QMessageBox.StandardButton.No:
            return

        # Lấy thông tin Order để hoàn lại sách trước khi xóa
        order = next((o for o in self.orders if o.order_id == order_id), None)
        if not order:
            QMessageBox.warning(self.MainWindow, "Error", "Order not found!")
            return
        book_id = order.book_id
        quantity_return = order.quantity
        reader_id = order.reader_id  # Lấy Reader ID từ đơn hàng

        success, message = OrderController.delete_order(order_id)
        if success:
            # Hoàn lại số lượng sách
            book = next((b for b in self.all_books if b.book_id == book_id), None)
            if book:
                book.quantity += quantity_return  # Cộng lại số sách
                JsonFileFactory.write_data(self.all_books, BookController.books_file)  # Lưu vào file

            # Xóa sách khỏi danh sách mượn của Reader
            ReaderController.remove_order_book_from_reader(reader_id, book_id, quantity_return)

            QMessageBox.information(self.MainWindow, "Announcement", message)

            # Cập nhật danh sách và giao diện
            self.orders = OrderController.get_all_orders()
            self.load_orders()
            self.show_books_ui()  # Cập nhật lại bảng sách
    def process_update_order(self):
        selected_row = self.tableWidgetBorrowAndReturn.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self.MainWindow, "Error", "Select order to update information!")
            return

        order_id = int(self.tableWidgetBorrowAndReturn.item(selected_row, 0).text())
        reader_id = int(self.lineEditReaderIDBR.text())
        book_id = self.lineEditBookIDBR.text()
        new_quantity = int(self.lineEditQuantityBR.text())
        status = self.comboBoxStatus.currentText()
        borrow_date = self.dateEditDateBorrowing.date().toString("dd/MM/yyyy")
        return_date = self.dateEditDateReturning.date().toString("dd/MM/yyyy")

        # Lấy thông tin order cũ trước khi cập nhật
        old_order = self.orders[selected_row]
        old_reader_id = old_order.reader_id
        old_book_id = old_order.book_id
        old_quantity = old_order.quantity

        # Tìm sách trong danh sách
        old_book = next((b for b in self.all_books if b.book_id == old_book_id), None)
        new_book = next((b for b in self.all_books if b.book_id == book_id), None)

        if not new_book:
            QMessageBox.warning(self.MainWindow, "Error", "Book ID not found!")
            return

        # Nếu đổi sách, hoàn trả số sách cũ về kho
        if old_book and old_book_id != book_id:
            old_book.quantity += old_quantity

        # Kiểm tra số lượng sách mới có đủ không
        available_quantity = new_book.quantity + (old_quantity if old_book_id == book_id else 0)
        if available_quantity < new_quantity:
            QMessageBox.warning(self.MainWindow, "Error", "Not enough books in stock!")
            return

        # Cập nhật số lượng sách trong kho
        if old_book_id == book_id:
            new_book.quantity += old_quantity - new_quantity
        else:
            new_book.quantity -= new_quantity

        # Cập nhật danh sách sách của người đọc
        if old_reader_id != reader_id:
            # Nếu đổi người mượn => Giảm sách khỏi người cũ, tăng cho người mới
            ReaderController.update_order_book_to_reader(old_reader_id, old_book_id, 0, old_quantity)
            ReaderController.update_order_book_to_reader(reader_id, book_id, new_quantity, 0)
        elif old_book_id != book_id:
            # Nếu đổi sách nhưng vẫn là cùng người mượn
            ReaderController.update_order_book_to_reader(old_reader_id, old_book_id, 0, old_quantity)
            ReaderController.update_order_book_to_reader(reader_id, book_id, new_quantity, 0)
        else:
            # Nếu chỉ thay đổi số lượng
            ReaderController.update_order_book_to_reader(reader_id, book_id, new_quantity, old_quantity)

        # Cập nhật lại đơn hàng
        order = Order(order_id, reader_id, book_id, new_quantity, borrow_date, return_date, status)
        self.orders[selected_row] = order

        # Lưu thay đổi vào file
        JsonFileFactory.write_data(self.orders, OrderController.orders_file)
        JsonFileFactory.write_data(self.all_books, BookController.books_file)

        # Cập nhật giao diện
        self.show_readers_ui()
        self.load_orders()
        self.show_books_ui()

    #Xu ly action
    def process_log_out(self):
        confirmation = QMessageBox.question(
            self.MainWindow, "Logout", "Are you sure you want to logout?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if confirmation == QMessageBox.StandardButton.Yes:
            UserController.logout()
            self.MainWindow.close()
            from ui.LoginWindowExt import LoginWindowExt
            self.mywindow = LoginWindowExt()
            self.mywindow.setupUi(QMainWindow())
            self.mywindow.showWindow()
    def export_order_data_excel(self):
        eit = ExportImportExcelTool()
        filename = "../excel_dataset/orders.xlsx"
        eit.export_order_excel(self.orders, filename)

        msg = QMessageBox(self.MainWindow)
        msg.setText("Đã export data ra Excel thành công")
        msg.setWindowTitle("Thông báo")
        msg.setIcon(QMessageBox.Icon.Information)
        buttons = QMessageBox.StandardButton.Yes
        msg.setStandardButtons(buttons)
        msg.exec()
    def export_reader_data_excel(self):
        eit = ExportImportExcelTool()
        filename = "../excel_dataset/readers.xlsx"
        eit.export_reader_excel(self.all_readers, filename)

        msg = QMessageBox(self.MainWindow)
        msg.setText("Đã export data ra Excel thành công")
        msg.setWindowTitle("Thông báo")
        msg.setIcon(QMessageBox.Icon.Information)
        buttons = QMessageBox.StandardButton.Yes
        msg.setStandardButtons(buttons)
        msg.exec()
    def export_author_data_excel(self):
        eit = ExportImportExcelTool()
        filename = "../excel_dataset/authors.xlsx"
        eit.export_author_excel(self.all_authors, filename)

        msg = QMessageBox(self.MainWindow)
        msg.setText("Đã export data ra Excel thành công")
        msg.setWindowTitle("Thông báo")
        msg.setIcon(QMessageBox.Icon.Information)
        buttons = QMessageBox.StandardButton.Yes
        msg.setStandardButtons(buttons)
        msg.exec()
    def export_book_data_excel(self):
        eit = ExportImportExcelTool()
        filename = "../excel_dataset/books.xlsx"
        eit.export_book_excel(self.all_books, filename)

        msg = QMessageBox(self.MainWindow)
        msg.setText("Đã export data ra Excel thành công")
        msg.setWindowTitle("Thông báo")
        msg.setIcon(QMessageBox.Icon.Information)
        buttons = QMessageBox.StandardButton.Yes
        msg.setStandardButtons(buttons)
        msg.exec()
    def export_all_data_excel(self):
        eit = ExportImportExcelTool()

        filename = "../excel_dataset/authors.xlsx"
        eit.export_author_excel(self.all_authors, filename)

        filename = "../excel_dataset/books.xlsx"
        eit.export_book_excel(self.all_books, filename)

        filename = "../excel_dataset/orders.xlsx"
        eit.export_order_excel(self.orders, filename)

        filename = "../excel_dataset/readers.xlsx"
        eit.export_reader_excel(self.all_readers, filename)

        msg = QMessageBox(self.MainWindow)
        msg.setText("Đã export data ra Excel thành công")
        msg.setWindowTitle("Thông báo")
        msg.setIcon(QMessageBox.Icon.Information)
        buttons = QMessageBox.StandardButton.Yes
        msg.setStandardButtons(buttons)
        msg.exec()