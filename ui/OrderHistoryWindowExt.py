from PyQt6.QtWidgets import QTableWidgetItem

from ui.OrderHistoryWindow import Ui_MainWindow


class OrderHistoryWindowExt(Ui_MainWindow):
    def __init__(self, orders, parent=None):
        super().__init__()
        self.orders = orders  # Lưu danh sách đơn hàng
        self.parent = parent  # Lưu tham chiếu đến cửa sổ cha (nếu có)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow  # Cửa sổ chính được truyền vào

        # Hiển thị các đơn hàng trong QTableWidget
        self.tableWidget.setRowCount(len(self.orders))  # Đặt số hàng cho bảng

        for row, order in enumerate(self.orders):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(order.order_id)))  # Order ID
            self.tableWidget.setItem(row, 1, QTableWidgetItem(order.book_id))  # Book ID
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(order.quantity)))  # Quantity
            self.tableWidget.setItem(row, 3, QTableWidgetItem(order.status))  # Status
            self.tableWidget.setItem(row, 4, QTableWidgetItem(order.borrow_date))  # Borrowing Date
            self.tableWidget.setItem(row, 5, QTableWidgetItem(order.return_date))  # Returning Date

    def showWindow(self):
        self.MainWindow.show()
