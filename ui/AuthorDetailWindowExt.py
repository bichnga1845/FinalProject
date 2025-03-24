from PyQt6.QtWidgets import QMessageBox

from controller.author_controller import AuthorController
from ui.AuthorDetailWindow import Ui_MainWindow


class AuthorDetailWindowExt(Ui_MainWindow):
    def __init__(self, author_name):
        super().__init__()
        self.author_name = author_name

    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.load_author_details()

    def showWindow(self):
        self.MainWindow.show()

    def load_author_details(self):
        author = AuthorController.get_author_by_name(self.author_name)

        if not author:
            QMessageBox.warning(self.MainWindow, "Error", "Author not found!")
            self.MainWindow.close()
            return

        self.lineEditAuthorID.setText(str(author.author_id))
        self.lineEditName.setText(author.name)
        self.lineEditGender.setText(author.gender)
        self.lineEditHometown.setText(author.hometown)
        self.lineEditBookCount.setText(str(len(author.books)))
        self.lineEditBooks.setText(", ".join(book for book in author.books))