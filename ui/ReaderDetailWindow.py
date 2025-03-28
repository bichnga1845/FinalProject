# Form implementation generated from reading ui file 'E:\PYTHON\KĨ THUẬT LẬP TRÌNH - HK2\FinalProject\ui\ReaderDetailWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 655)
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: #E8F5E9; /* Xanh lá pastel nhẹ */\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 321, 51))
        self.label.setStyleSheet("QLabel {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #1B5E20; /* Xanh lá đậm */\n"
"    background-color: white;\n"
"    padding: 10px;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 91, 21))
        self.label_2.setStyleSheet("QLabel {\n"
"    font-size: 10px;\n"
"    font-weight: bold;\n"
"    color: #2E7D32; /* Xanh lá đậm */\n"
"}")
        self.label_2.setObjectName("label_2")
        self.lineEditReaderID = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditReaderID.setGeometry(QtCore.QRect(160, 130, 291, 31))
        self.lineEditReaderID.setStyleSheet("QLineEdit {\n"
"    background-color: #FFFFFF; /* Nền trắng */\n"
"    color: #1B5E20; /* Chữ xanh lá đậm */\n"
"    border-radius: 5px; /* Bo góc */\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    border: 2px solid #66BB6A; /* Viền xanh lá nhạt */\n"
"}\n"
"\n"
"/* Khi hover vào ô nhập */\n"
"QLineEdit:hover {\n"
"    background-color: #C8E6C9; /* Xanh lá nhạt */\n"
"    border: 2px solid #388E3C; /* Viền xanh lá đậm hơn */\n"
"}\n"
"\n"
"/* Khi ô nhập có focus */\n"
"QLineEdit:focus {\n"
"    background-color: #A5D6A7; /* Màu xanh lá sáng khi nhập */\n"
"    border: 2px solid #2E7D32; /* Viền xanh lá đậm hơn */\n"
"}\n"
"")
        self.lineEditReaderID.setObjectName("lineEditReaderID")
        self.lineEditReaderName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditReaderName.setGeometry(QtCore.QRect(160, 180, 291, 31))
        self.lineEditReaderName.setStyleSheet("QLineEdit {\n"
"    background-color: #FFFFFF; /* Nền trắng */\n"
"    color: #1B5E20; /* Chữ xanh lá đậm */\n"
"    border-radius: 5px; /* Bo góc */\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    border: 2px solid #66BB6A; /* Viền xanh lá nhạt */\n"
"}\n"
"\n"
"/* Khi hover vào ô nhập */\n"
"QLineEdit:hover {\n"
"    background-color: #C8E6C9; /* Xanh lá nhạt */\n"
"    border: 2px solid #388E3C; /* Viền xanh lá đậm hơn */\n"
"}\n"
"\n"
"/* Khi ô nhập có focus */\n"
"QLineEdit:focus {\n"
"    background-color: #A5D6A7; /* Màu xanh lá sáng khi nhập */\n"
"    border: 2px solid #2E7D32; /* Viền xanh lá đậm hơn */\n"
"}\n"
"")
        self.lineEditReaderName.setObjectName("lineEditReaderName")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 91, 21))
        self.label_3.setStyleSheet("QLabel {\n"
"    font-size: 10px;\n"
"    font-weight: bold;\n"
"    color: #2E7D32; /* Xanh lá đậm */\n"
"}")
        self.label_3.setObjectName("label_3")
        self.lineEditReaderBooks = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditReaderBooks.setGeometry(QtCore.QRect(160, 230, 291, 31))
        self.lineEditReaderBooks.setStyleSheet("QLineEdit {\n"
"    background-color: #FFFFFF; /* Nền trắng */\n"
"    color: #1B5E20; /* Chữ xanh lá đậm */\n"
"    border-radius: 5px; /* Bo góc */\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    border: 2px solid #66BB6A; /* Viền xanh lá nhạt */\n"
"}\n"
"\n"
"/* Khi hover vào ô nhập */\n"
"QLineEdit:hover {\n"
"    background-color: #C8E6C9; /* Xanh lá nhạt */\n"
"    border: 2px solid #388E3C; /* Viền xanh lá đậm hơn */\n"
"}\n"
"\n"
"/* Khi ô nhập có focus */\n"
"QLineEdit:focus {\n"
"    background-color: #A5D6A7; /* Màu xanh lá sáng khi nhập */\n"
"    border: 2px solid #2E7D32; /* Viền xanh lá đậm hơn */\n"
"}\n"
"")
        self.lineEditReaderBooks.setObjectName("lineEditReaderBooks")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 230, 91, 21))
        self.label_7.setStyleSheet("QLabel {\n"
"    font-size: 10px;\n"
"    font-weight: bold;\n"
"    color: #2E7D32; /* Xanh lá đậm */\n"
"}")
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-10, -30, 651, 641))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("E:\\PYTHON\\KĨ THUẬT LẬP TRÌNH - HK2\\FinalProject\\ui\\../images/pic_readdetail.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEditReaderID.raise_()
        self.lineEditReaderName.raise_()
        self.label_3.raise_()
        self.lineEditReaderBooks.raise_()
        self.label_7.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "READER DETAIL"))
        self.label_2.setText(_translate("MainWindow", "Reader ID:"))
        self.label_3.setText(_translate("MainWindow", "Reader Name:"))
        self.label_7.setText(_translate("MainWindow", "Books:"))
