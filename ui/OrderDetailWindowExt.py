from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QMessageBox

from controller.order_controller import OrderController
from ui.OrderDetailWindow import Ui_MainWindow


class OrderDetailWindowExt(Ui_MainWindow):
    def __init__(self, order_id):
        super().__init__()
        self.order_id = order_id

    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.load_order_details()

    def showWindow(self):
        self.MainWindow.show()

    def load_order_details(self):
        order=OrderController.get_order_by_id(self.order_id)

        if not order:
            QMessageBox.warning(self.MainWindow, "Error", "Order not found!")
            self.MainWindow.close()
            return
        self.lineEditOrderID.setText(str(order.order_id))
        self.lineEditReaderID.setText(str(order.reader_id))
        self.lineEditBookID.setText(order.book_id)
        self.lineEditQuantity.setText(str(order.quantity))
        self.lineEditStatus.setText(order.status)
        self.dateEditBorrow.setDate(QDate.fromString(order.borrow_date, "dd/MM/yyyy"))
        self.dateEditReturn.setDate(QDate.fromString(order.return_date, "dd/MM/yyyy"))