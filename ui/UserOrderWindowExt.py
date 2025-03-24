from datetime import datetime, timedelta

from PyQt6.QtWidgets import QLabel, QMessageBox

from controller.book_controller import BookController
from controller.order_controller import OrderController
from controller.reader_controller import ReaderController
from controller.user_controller import UserController
from libs.JsonFileFactory import JsonFileFactory
from models.Order import Order
from ui.UserOrderWindow import Ui_MainWindow


class UserOrderWindowExt(Ui_MainWindow):
    def __init__(self,order_items,user_window):
        super().__init__()
        self.order_items=order_items
        self.orders=OrderController.get_all_orders()
        self.user=UserController.current_user
        self.books = BookController.get_all_books()
        self.user_window=user_window

    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.show_order_items()
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonConfirm.clicked.connect(self.process_confirm)
    def show_order_items(self):
        for item in self.order_items:
            book_info = QLabel(
                f" {item['book_name']} - {item['title']} |  Author: {item['author']} |  Quantity: {item['quantity']}")
            self.verticalLayoutOrder.addWidget(book_info)

    def process_confirm(self):
        for item in self.order_items:
            order_id=OrderController.generate_order_id()

            reader=ReaderController.get_reader_by_name(self.user.name)
            reader_id=reader.reader_id

            book=BookController.get_book_by_name(item['book_name'])
            book_id=book.book_id

            quantity=item['quantity']

            borrow_date = datetime.today()
            return_date = borrow_date + timedelta(days=14)
            borrow_date =borrow_date.strftime("%d/%m/%Y")
            return_date=return_date.strftime("%d/%m/%Y")

            order = Order(order_id, reader_id, book_id, quantity, borrow_date, return_date)
            self.orders.append(order)
            JsonFileFactory.write_data(self.orders, OrderController.orders_file)

            book.quantity -= quantity
            for b in self.books:
                if b.book_id==book_id:
                    b.quantity=book.quantity
                    break
            JsonFileFactory.write_data(self.books, BookController.books_file)

            ReaderController.add_order_book_to_reader(reader_id, book_id, quantity)
            self.readers = ReaderController.get_all_readers()
            JsonFileFactory.write_data(self.readers, ReaderController.readers_file)

        QMessageBox.information(self.MainWindow, "Success", "Order successfully!")

        # Cập nhật danh sách sách trong cửa sổ chính
        self.user_window.refresh_books()

        self.MainWindow.close()  # Đóng cửa sổ đặt hàng

