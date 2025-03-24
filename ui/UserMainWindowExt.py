from PyQt6.QtWidgets import QTableWidgetItem, QSpinBox, QMessageBox, QMainWindow, QSizePolicy
from controller.book_controller import BookController
from controller.order_controller import OrderController
from controller.user_controller import UserController
from models.Book import Book
from ui.UserMainWindow import Ui_MainWindow
from ui.UserOrderWindowExt import UserOrderWindowExt
from ui.OrderDetailWindowExt import OrderDetailWindowExt


from PyQt6.QtCore import QDate


class UserMainWindowExt(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.books = Book.get_all_books()
        self.user = UserController.current_user
        self.setupUi(self)



    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
        self.show_books_ui()


    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonSearchBook.clicked.connect(self.process_search_book_and_author)
        self.pushButtonLogOut_2.clicked.connect(self.logout)
        self.pushButtonOrder.clicked.connect(self.process_order)
    def show_books_ui(self):

        self.tableWidget.setRowCount(0)

        for book in self.books:
            #get number of rows (meaning: last row)
            row=self.tableWidget.rowCount()
            #insert new row (last row)
            self.tableWidget.insertRow(row)
            book_id = QTableWidgetItem(book.book_id)
            book_name = QTableWidgetItem(book.book_name)
            book_type = QTableWidgetItem(book.type)
            published_year = QTableWidgetItem(book.published_year)
            publisher = QTableWidgetItem(book.publisher)
            stock = QTableWidgetItem(str(book.quantity))
            author = QTableWidgetItem(book.author)

            #set cell for row
            self.tableWidget.setItem(row, 0, book_id)
            self.tableWidget.setItem(row, 1, book_name)
            self.tableWidget.setItem(row, 2, book_type)
            self.tableWidget.setItem(row, 3, published_year)
            self.tableWidget.setItem(row, 4, publisher)
            self.tableWidget.setItem(row, 5, stock)
            self.tableWidget.setItem(row, 6, author)
            borrowed_quantity = QSpinBox()
            borrowed_quantity.setMinimum(0)
            borrowed_quantity.setMaximum(int(book.quantity))
            borrowed_quantity.valueChanged.connect(self.display_order)
            self.tableWidget.setCellWidget(row, 7, borrowed_quantity)

        self.labelWelcome.setText(f"Welcome {self.user.name}")

    def process_search_book_and_author(self):
        query = self.lineEditSearch.text().strip().lower()
        self.books = BookController.search_books(query)
        self.show_books_ui()

    def logout(self):
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

    def display_order(self):
        display_text=""
        for row in range(self.tableWidget.rowCount()):
            quantity_spinbox = self.tableWidget.cellWidget(row, 7)
            book = self.tableWidget.item(row, 1).text()
            quantity = quantity_spinbox.value()
            if quantity>0:
                display_text += f"{book} : {quantity}\t\t"
        self.labelTotal.setText(f"{display_text}")

    def process_order(self):
        self.order_items = []

        for row in range(self.tableWidget.rowCount()):
            quantity = self.tableWidget.cellWidget(row, 7).value()
            if quantity > 0:
                book_name = self.tableWidget.item(row, 1).text()
                title = self.tableWidget.item(row, 2).text()
                author = self.tableWidget.item(row, 6).text()

                self.order_items.append({
                    "book_name": book_name,
                    "title": title,
                    "author": author,
                    "quantity": quantity
                })

        if not self.order_items:
            QMessageBox.warning(self.MainWindow, "Warning", "No books selected!")
            return

        self.mywindow = UserOrderWindowExt(self.order_items,self)
        self.mywindow.setupUi(QMainWindow())
        self.mywindow.showWindow()

    def refresh_books(self):
        self.books = BookController.get_all_books()
        self.show_books_ui()

