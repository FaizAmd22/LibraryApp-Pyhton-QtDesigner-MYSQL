from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 600)
        
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(244, 244, 242);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(50, 20, 50, 20)
        self.verticalLayout.setSpacing(20)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setFixedSize(140, 140)
        self.label_2.setPixmap(QtGui.QPixmap("resources/icons/login.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_2, alignment=QtCore.Qt.AlignCenter)

        # Username input
        self.editUsername = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        self.editUsername.setFont(font)
        self.editUsername.setStyleSheet("QLineEdit {\n"
                                        "    border: none;\n"
                                        "    color: rgb(0, 0, 0);\n"
                                        "    background-color: rgba(232, 232, 232, 255);\n"
                                        "    border-radius: 10px;\n"
                                        "    margin-right: 100px;\n"
                                        "    margin-left: 100px;\n"
                                        "    padding-left: 15px;\n"
                                        "    height: 35px;\n"
                                        "}")
        self.editUsername.setPlaceholderText("Username")
        self.verticalLayout.addWidget(self.editUsername)

        # Password input
        self.editPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.editPassword.setFont(font)
        self.editPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editPassword.setStyleSheet("QLineEdit {\n"
                                        "    border: none;\n"
                                        "    color: rgb(0, 0, 0);\n"
                                        "    background-color: rgba(232, 232, 232, 255);\n"
                                        "    border-radius: 10px;\n"
                                        "    padding-left: 15px;\n"
                                        "    margin-bottom: 30px;\n"
                                        "    margin-right: 100px;\n"
                                        "    margin-left: 100px;\n"
                                        "    height: 35px;\n"
                                        "}")
        self.editPassword.setPlaceholderText("Password")
        self.verticalLayout.addWidget(self.editPassword)

        # Login button
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setFont(font)
        self.btnLogin.setStyleSheet("QPushButton {\n"
                                    "    background-color: rgb(73, 84, 100);\n"
                                    "    border: none;\n"
                                    "    border-radius: 10px;\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "    margin-bottom: 50px;\n"
                                    "    margin-right: 150px;\n"
                                    "    margin-left: 150px;\n"
                                    "    height: 35px;\n"
                                    "    width: 70%;\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: rgb(91, 105, 125);\n"
                                    "}")
        self.btnLogin.setText("Login")
        self.verticalLayout.addWidget(self.btnLogin)

        # Set the central widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Set window title
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
