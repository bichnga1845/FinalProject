from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.LoginWindowExt import LoginWindowExt

app=QApplication([])
mywindow= LoginWindowExt()
mywindow.setupUi(QMainWindow())
mywindow.showWindow()
app.exec()