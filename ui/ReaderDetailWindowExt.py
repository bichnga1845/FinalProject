from PyQt6.QtWidgets import QMessageBox

from controller.reader_controller import ReaderController
from ui.ReaderDetailWindow import Ui_MainWindow


class ReaderDetailWindowExt(Ui_MainWindow):
    def __init__(self, reader_id):
        super().__init__()
        self.reader_id = reader_id

    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.load_reader_details()

    def showWindow(self):
        self.MainWindow.show()

    def load_reader_details(self):
        reader = ReaderController.get_reader_by_id(self.reader_id)

        if not reader:
            QMessageBox.warning(self.MainWindow, "Error", "Reader not found!")
            self.MainWindow.close()
            return

        self.lineEditReaderID.setText(str(reader.reader_id))
        self.lineEditReaderName.setText(reader.name)
        self.lineEditReaderBooks.setText(", ".join(f"{book_id} (x{quantity})" for book_id, quantity in reader.books))