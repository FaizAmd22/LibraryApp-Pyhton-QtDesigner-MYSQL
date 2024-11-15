from PyQt5 import QtWidgets, QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 600)
        MainWindow.setStyleSheet("background-color: rgb(244, 244, 242);")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.anggotaLayout = QtWidgets.QVBoxLayout()
        self.labelAnggota = QtWidgets.QLabel(self.centralwidget)
        self.labelAnggota.setPixmap(QtGui.QPixmap("resources/icons/anggota.png"))
        self.labelAnggota.setScaledContents(True)
        self.labelAnggota.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAnggota.setStyleSheet("margin: 100px 50px 0 50px;")
        self.anggotaLayout.addWidget(self.labelAnggota)
        
        self.btnAnggota = QtWidgets.QPushButton("Data Anggota", self.centralwidget)
        self.btnAnggota.setStyleSheet(self.buttonStyle())
        self.anggotaLayout.addWidget(self.btnAnggota)
        self.horizontalLayout.addLayout(self.anggotaLayout)

        self.bukuLayout = QtWidgets.QVBoxLayout()
        self.labelBuku = QtWidgets.QLabel(self.centralwidget)
        self.labelBuku.setPixmap(QtGui.QPixmap("resources/icons/buku.png"))
        self.labelBuku.setScaledContents(True)
        self.labelBuku.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBuku.setStyleSheet("margin: 100px 50px 0 50px;")
        self.bukuLayout.addWidget(self.labelBuku)
        
        self.btnBuku = QtWidgets.QPushButton("Data Buku", self.centralwidget)
        self.btnBuku.setStyleSheet(self.buttonStyle())
        self.bukuLayout.addWidget(self.btnBuku)
        self.horizontalLayout.addLayout(self.bukuLayout)

        self.transaksiLayout = QtWidgets.QVBoxLayout()
        self.labelTransaksi = QtWidgets.QLabel(self.centralwidget)
        self.labelTransaksi.setPixmap(QtGui.QPixmap("resources/icons/transaksi.png"))
        self.labelTransaksi.setScaledContents(True)
        self.labelTransaksi.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTransaksi.setStyleSheet("margin: 100px 50px 0 50px;")
        self.transaksiLayout.addWidget(self.labelTransaksi)
        
        self.btnTransaksi = QtWidgets.QPushButton("Data Transaksi", self.centralwidget)
        self.btnTransaksi.setStyleSheet(self.buttonStyle())
        self.transaksiLayout.addWidget(self.btnTransaksi)
        self.horizontalLayout.addLayout(self.transaksiLayout)

        self.verticalLayout.addLayout(self.horizontalLayout)

        spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacer)

        self.btnLogout = QtWidgets.QPushButton("Logout", self.centralwidget)
        self.btnLogout.setStyleSheet("QPushButton {\n"
                                    "    background-color: rgb(247, 10, 10);\n"
                                    "    border: none;\n"
                                    "    border-radius: 10px;\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "    font-size: 11px;\n"
                                    "    font-weight: bold;\n"
                                    "    padding: 15px 75px 15px 75px;\n"
                                    "    margin-bottom: 50px;\n"
                                    "    margin-top: 80px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: #FF4C4C;\n"
                                    "}\n"
                                    "")
        self.verticalLayout.addWidget(self.btnLogout, alignment=QtCore.Qt.AlignCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("Main Form")

    def buttonStyle(self):
        return ("QPushButton { background-color: rgb(255, 255, 255); border: none; "
                      "border-radius: 10px; color: rgb(73, 84, 100); padding: 10px; font-size: 12px; font-weight: bold; "
                      "margin-left: 50px; margin-right: 50px; }"
                      "QPushButton:hover { background-color: rgb(73, 84, 100); color: white; }")
