from PyQt6.QtWidgets import QMessageBox, QMainWindow, QInputDialog

from controller.user_controller import UserController
from ui.LoginWindow import Ui_MainWindow
from ui.RegisterWindowExt import RegisterWindowExt



class LoginWindowExt(Ui_MainWindow):
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.process_login)
        self.pushButtonRegister.clicked.connect(self.process_register)
        self.pushButtonChangePassword.clicked.connect(self.process_change_password)

    def process_login(self):
        uid = self.lineEditUserName.text()
        pwd = self.lineEditPassword.text()

        user,role = UserController.login(uid, pwd)
        if not user:
            self.msg = QMessageBox(self.MainWindow)
            self.msg.setText("Login Failed!")
            self.msg.exec()
        else:
            self.MainWindow.close()  # close man hinh login

            if role == "admin":
                from ui.ManagementWindowExt import ManagementWindowExt
                self.mywindow = ManagementWindowExt()
            elif role == "user":
                from ui.UserMainWindowExt import UserMainWindowExt
                self.mywindow = UserMainWindowExt()
            else:
                QMessageBox.warning(self.MainWindow, "Error", "Invalid role!")
                return  # Dừng lại nếu role không hợp lệ

            self.mywindow.setupUi(QMainWindow())
            self.mywindow.showWindow()

    def process_register(self):
        self.mywindow = RegisterWindowExt()
        self.mywindow.setupUi(QMainWindow())
        self.mywindow.showWindow()
    def process_change_password(self):
        uid = self.lineEditUserName.text()
        # Hiển thị hộp thoại nhập liệu
        new_pass, ok = QInputDialog.getText(self.MainWindow, "Change password:", "Enter your new password:")

        # Kiểm tra nếu người dùng nhấn OK
        if ok and new_pass:
            success,message=UserController.change_password(uid,new_pass)
            # Hiển thị kết quả
            if success:
                QMessageBox.information(self.MainWindow, "Success", message)
            else:
                QMessageBox.warning(self.MainWindow, "Error", message)

