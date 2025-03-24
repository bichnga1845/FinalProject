from PyQt6.QtWidgets import QMessageBox

from controller.reader_controller import ReaderController
from libs.JsonFileFactory import JsonFileFactory
from models.Reader import Reader
from models.User import User
from ui.RegisterWindow import Ui_MainWindow


class RegisterWindowExt(Ui_MainWindow):
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonSignUp.clicked.connect(self.process_register)
    def process_register(self):
        users = User.get_all_users()
        is_admin=self.radioButtonAdmin.isChecked()

        username = self.lineEditUserName.text()
        password = self.lineEditPassword.text()
        name=self.lineEditFullName.text()
        gender=self.comboBoxGender.currentText()
        date=self.dateEditDate.date().toString("dd/MM/yyyy")
        phone=self.lineEditPhone.text()
        address=self.lineEditAddress.text()

        if not username or not password:
            QMessageBox.warning(self.MainWindow, "Error", "Username and password can't be blank !")
            return

        if not name or not gender or not date or not phone or not address:
            QMessageBox.warning(self.MainWindow, "Error", "You have to fill all")
            return

        for user in users:
            if user.username == username:
                QMessageBox.warning(self.MainWindow, "Error", "Username already exists!")
                return
        if is_admin:
            role="admin"
        else:
            role="user"
        new_user=User(username,password,name,gender,date,phone,address,role)
        users.append(new_user)
        JsonFileFactory.write_data(users, "../dataset/users.json")
        if not is_admin:
            reader_id=ReaderController.generate_reader_id()
            new_reader=Reader(reader_id,name,gender,date,phone,address)
            readers=ReaderController.get_all_readers()
            readers.append(new_reader)
            JsonFileFactory.write_data(readers,ReaderController.readers_file)

        QMessageBox.information(self.MainWindow, "Infor", "Sign up successful!")
        self.MainWindow.close()
