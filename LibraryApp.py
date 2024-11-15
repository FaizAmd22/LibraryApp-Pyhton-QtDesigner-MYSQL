import sys
import mysql.connector
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QDate
from components.form_login import Ui_LoginWindow
from components.form_main import Ui_MainWindow
from components.form_anggota import Ui_FormAnggota
from components.form_buku import Ui_FormBuku
from components.form_transaksi import Ui_FormTransaksi

class LibraryApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(LibraryApp, self).__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.btnLogin.clicked.connect(self.check_login)

    def connect_db(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='perpustakaan_app'
            )
            return connection
        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(self, "Error", f"Error: {err}")
            return None

    def deleteText(self):
        self.ui.editUsername.setText('')
        self.ui.editPassword.setText('')

    def check_login(self):
        username = self.ui.editUsername.text()
        password = self.ui.editPassword.text()
        connection = self.connect_db()

        if username and password:
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM user WHERE username=%s AND password=md5(%s)", (username, password))
                result = cursor.fetchone()
                cursor.close()
                connection.close()

                if result:
                    QtWidgets.QMessageBox.information(self, "Success", "Login Berhasil!")
                    self.deleteText()
                    self.open_main_form()
                else:
                    QtWidgets.QMessageBox.warning(self, "Error", "Username atau Password salah!")
                    self.deleteText()
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Terjadi kesalahan saat login!")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Username atau Password tidak boleh kosong!")

    def open_main_form(self):
        self.mainForm = QtWidgets.QMainWindow()
        self.uiMain = Ui_MainWindow()
        self.uiMain.setupUi(self.mainForm)
        
        self.uiMain.btnAnggota.clicked.connect(self.open_form_anggota)
        self.uiMain.btnBuku.clicked.connect(self.open_form_buku)
        self.uiMain.btnTransaksi.clicked.connect(self.open_form_transaksi)
        self.uiMain.btnLogout.clicked.connect(self.logout)

        if widget.count() < 2:
            widget.addWidget(self.mainForm)
        
        widget.setCurrentIndex(1)

    def open_form_anggota(self):
        self.formAnggota = Ui_FormAnggota()
        self.formAnggota.show()
        self.formAnggota.member_data_table.cellClicked.connect(self.load_data_input_anggota) 
        self.formAnggota.btnBack.clicked.connect(self.close_form_anggota)

    def open_form_buku(self):
        self.formBuku = Ui_FormBuku()
        self.formBuku.show()
        self.formBuku.book_data_table.cellClicked.connect(self.load_data_input_buku)
        self.formBuku.btnBack.clicked.connect(self.close_form_buku)
    
    def open_form_transaksi(self):
        self.formTransaksi = Ui_FormTransaksi()
        self.formTransaksi.show()
        self.formTransaksi.btnBack.clicked.connect(self.close_form_transaksi)

    def close_form_anggota(self):
        self.formAnggota.close()

    def close_form_buku(self):
        self.formBuku.close()
    
    def close_form_transaksi(self):
        self.formTransaksi.close()

    def load_data_input_anggota(self, row, column):
        item = self.formAnggota.member_data_table.item(row, column)
        if item is not None:
            self.formAnggota.member_id_input.setText(self.formAnggota.member_data_table.item(row, 0).text())
            self.formAnggota.name_input.setText(self.formAnggota.member_data_table.item(row, 1).text())
            self.formAnggota.gender_combobox.setCurrentText(self.formAnggota.member_data_table.item(row, 2).text())
            self.formAnggota.address_input.setText(self.formAnggota.member_data_table.item(row, 3).text())
            self.formAnggota.phone_input.setText(self.formAnggota.member_data_table.item(row, 4).text())
            self.formAnggota.email_input.setText(self.formAnggota.member_data_table.item(row, 5).text())
    
    def load_data_input_buku(self, row):
        isbn = self.formBuku.book_data_table.item(row, 0).text()
        judul = self.formBuku.book_data_table.item(row, 3).text()
        penulis = self.formBuku.book_data_table.item(row, 2).text()
        genre = self.formBuku.book_data_table.item(row, 1).text()
        penerbit = self.formBuku.book_data_table.item(row, 4).text()
        tanggal_publikasi = self.formBuku.book_data_table.item(row, 5).text()
        stock = self.formBuku.book_data_table.item(row, 6).text()
        
        self.formBuku.book_id_input.setText(isbn)
        self.formBuku.title_input.setText(judul)
        self.formBuku.author_input.setCurrentText(penulis)
        self.formBuku.genre_input.setCurrentText(genre)
        self.formBuku.publisher_input.setText(penerbit)
        self.formBuku.stock_input.setText(stock)

        pub_date = QDate.fromString(tanggal_publikasi, "yyyy-MM-dd")
        self.formBuku.pub_date_input.setDate(pub_date)

    def return_to_main(self):
        widget.setCurrentIndex(1)

    def logout(self):
        reply = QtWidgets.QMessageBox.question(self, 'Konfirmasi Logout', 'Apakah Anda yakin ingin logout?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            widget.setCurrentIndex(0)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    QtGui.QFontDatabase.addApplicationFont("resources/fonts/Poppins-Regular.ttf")
    app.setStyleSheet("font-family: 'Poppins';")

    widget = QtWidgets.QStackedWidget()
    library_window = LibraryApp()
    widget.addWidget(library_window)
    widget.setMinimumWidth(850)
    widget.setMinimumHeight(600)
    widget.setWindowTitle('Aplikasi Perpustakaan')
    widget.show()

    sys.exit(app.exec_())
