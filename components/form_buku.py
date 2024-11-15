from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, 
                             QComboBox, QDateEdit, QGridLayout, QVBoxLayout, QTableWidget, 
                             QTableWidgetItem, QMessageBox)
from PyQt5.QtCore import QDate
import mysql.connector

class Ui_FormBuku(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def connect_db(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='perpustakaan_app'
            )
            print("Koneksi ke database berhasil")
            return connection
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Error: {err}")
            return None

    def setupUi(self):
        self.setWindowTitle("Data Buku")
        self.resize(850, 600)
        self.verticalLayout = QVBoxLayout(self)

        self.label = QLabel("Data Buku")
        self.label.setStyleSheet("font-size:20px; font-weight: bold; text-align: center; margin: 10px 0;")
        self.verticalLayout.addWidget(self.label)

        self.book_id_label = QLabel("ISBN")
        self.book_id_input = QLineEdit()

        self.title_label = QLabel("Judul Buku")
        self.title_input = QLineEdit()
        
        self.author_label = QLabel("Penulis")
        self.author_input = QComboBox()
        self.author_input.setEditable(True)
        self.author_input.setInsertPolicy(QComboBox.NoInsert)
        self.author_input.completer().setCompletionMode(2)
        self.load_authors()

        self.genre_label = QLabel("Genre")
        self.genre_input = QComboBox()
        self.genre_input.setEditable(True)
        self.genre_input.setInsertPolicy(QComboBox.NoInsert)
        self.genre_input.completer().setCompletionMode(2)
        self.load_genres()

        self.publisher_label = QLabel("Penerbit")
        self.publisher_input = QLineEdit()
        self.stock_label = QLabel("Jumlah Buku")
        self.stock_input = QLineEdit()

        self.pub_date_label = QLabel("Tanggal Publikasi")
        self.pub_date_input = QDateEdit()
        self.pub_date_input.setCalendarPopup(True)
        self.pub_date_input.setDisplayFormat("yyyy-MM-dd")

        self.add_button = QPushButton("Tambah")
        self.add_button.setStyleSheet("QPushButton {\n"
                                    "    background-color: rgb(73, 84, 100);\n"
                                    "    border: none;\n"
                                    "    border-radius: 10px;\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "    font-size: 11px;\n"
                                    "    font-weight: bold;\n"
                                    "    padding: 5px 50px 5px 50px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: rgb(91, 105, 125);\n"
                                    "}\n"
                                    "")
        self.update_button = QPushButton("Edit")
        self.update_button.setStyleSheet("QPushButton {\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "    border: none;\n"
                                    "    border-radius: 10px;\n"
                                    "    color: rgb(73, 84, 100);\n"
                                    "    font-size: 11px;\n"
                                    "    font-weight: bold;\n"
                                    "    padding: 5px 50px 5px 50px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: rgb(73, 84, 100);\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "}\n"
                                    "")
        self.delete_button = QPushButton("Hapus")
        self.delete_button.setStyleSheet("QPushButton {\n"
                                    "    background-color: rgb(247, 10, 10);\n"
                                    "    border: none;\n"
                                    "    border-radius: 10px;\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "    font-size: 11px;\n"
                                    "    font-weight: bold;\n"
                                    "    padding: 5px 50px 5px 50px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: #FF4C4C;\n"
                                    "}\n"
                                    "")
        self.reset_button = QPushButton("Reset")
        self.reset_button.setStyleSheet("QPushButton {\n"
                                    "    background-color: rgb(73, 84, 100);\n"
                                    "    border: none;\n"
                                    "    border-radius: 10px;\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "    font-weight: bold;\n"
                                    "    padding: 5px 50px 5px 50px;\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: rgb(91, 105, 125);\n"
                                    "}")

        self.form_layout = QGridLayout()
        self.form_layout.addWidget(self.book_id_label, 0, 0)
        self.form_layout.addWidget(self.book_id_input, 0, 1)
        self.form_layout.addWidget(self.title_label, 1, 0)
        self.form_layout.addWidget(self.title_input, 1, 1)
        self.form_layout.addWidget(self.author_label, 2, 0)
        self.form_layout.addWidget(self.author_input, 2, 1)
        self.form_layout.addWidget(self.genre_label, 3, 0)
        self.form_layout.addWidget(self.genre_input, 3, 1)
        self.form_layout.addWidget(self.publisher_label, 4, 0)
        self.form_layout.addWidget(self.publisher_input, 4, 1)
        self.form_layout.addWidget(self.pub_date_label, 5, 0)
        self.form_layout.addWidget(self.pub_date_input, 5, 1)
        self.form_layout.addWidget(self.stock_label, 6, 0)
        self.form_layout.addWidget(self.stock_input, 6, 1)
        self.form_layout.addWidget(self.add_button, 0, 2)
        self.form_layout.addWidget(self.update_button, 1, 2)
        self.form_layout.addWidget(self.delete_button, 2, 2)
        self.form_layout.addWidget(self.reset_button, 3, 2)

        self.verticalLayout.addLayout(self.form_layout)

        self.search_label = QLabel("Cari ISBN / Judul Buku")
        self.search_label.setStyleSheet("margin-top: 40px;")
        self.search_input = QLineEdit()
        self.search_input.setStyleSheet("QLineEdit {\n"
                                        "    border: none;\n"
                                        "    color: rgb(0, 0, 0);\n"
                                        "    background-color: #fff;\n"
                                        "    border: 2px solid rgb(73, 84, 100);\n"
                                        "    border-radius: 10px;\n"
                                        "    padding-left: 15px;\n"
                                        "    height: 35px;\n"
                                        "}\n"
                                        "QLineEdit:hover {\n"
                                        "    border: 2px solid #efefef;\n"
                                        "}")
        self.search_input.setPlaceholderText("Masukkan ISBN / Judul Buku")
        self.search_button = QPushButton("Cari")
        self.search_button.setStyleSheet("QPushButton {\n"
                                    "    background-color: rgb(73, 84, 100);\n"
                                    "    border: none;\n"
                                    "    border-radius: 10px;\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "    padding: 10px 50px 10px 50px;\n"
                                    "    font-weight: bold;\n"
                                    "    font-size: 12px;\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    background-color: rgb(91, 105, 125);\n"
                                    "}")

        self.book_data_table = QTableWidget()
        self.book_data_table.setColumnCount(7)
        self.book_data_table.setHorizontalHeaderLabels(["ISBN", "Judul Buku", "Penulis", "Genre", "Penerbit", "Tanggal Publikasi", "Jumlah Buku"])
        self.book_data_table.horizontalHeader().setStretchLastSection(True)
        self.book_data_table.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.search_label)
        self.verticalLayout.addWidget(self.search_input)
        self.verticalLayout.addWidget(self.search_button)
        self.verticalLayout.addWidget(self.book_data_table)

        self.btnBack = QPushButton("Kembali")
        self.btnBack.setStyleSheet("QPushButton { background-color: rgb(255, 255, 255); border: none; "
                      "border-radius: 10px; color: rgb(73, 84, 100); padding: 10px; font-size: 12px; font-weight: bold; "
                      "margin-top: 30px; }"
                      "QPushButton:hover { background-color: rgb(73, 84, 100); color: white; }")
        self.verticalLayout.addWidget(self.btnBack)

        self.add_button.clicked.connect(self.add_book)
        self.update_button.clicked.connect(self.update_book)
        self.delete_button.clicked.connect(self.delete_book)
        self.search_button.clicked.connect(self.search_book)
        self.reset_button.clicked.connect(self.clear_inputs)

        self.load_books()

    def load_authors(self):
        connection = self.connect_db()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT DISTINCT id_penulis, nama_penulis FROM penulis WHERE is_delete = false")
            authors = cursor.fetchall()
            self.author_input.addItem("")
            self.author_input.addItems([author[1] for author in authors])
            cursor.close()
            connection.close()

    def load_genres(self):
        connection = self.connect_db()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT DISTINCT id_genre, nama_genre FROM genre WHERE is_delete = false")
            genres = cursor.fetchall()
            self.genre_input.addItem("")
            self.genre_input.addItems([genre[1] for genre in genres])
            cursor.close()
            connection.close()

    def load_books(self):
        connection = self.connect_db()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM buku WHERE is_delete = false ORDER BY created_at DESC")
            results = cursor.fetchall()
            self.book_data_table.setRowCount(0)
            existing_ids = set()
            
            for row in results:
                row_position = self.book_data_table.rowCount()
                self.book_data_table.insertRow(row_position)
                for column, data in enumerate(row):
                    self.book_data_table.setItem(row_position, column, QTableWidgetItem(str(data)))
                    if column == 0:
                        existing_ids.add(data)
            
            cursor.close()
            connection.close()

    def clear_inputs(self):
        self.book_id_input.clear()
        self.title_input.clear()
        self.author_input.setCurrentIndex(0)
        self.genre_input.setCurrentIndex(0)
        self.publisher_input.clear()
        self.stock_input.clear()
        
        pub_date = QDate.fromString("2000-01-01", "yyyy-MM-dd")
        self.pub_date_input.setDate(pub_date)

    def add_genre_if_not_exists(self, genre_name):
        connection = self.connect_db()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("SELECT COUNT(*) FROM genre WHERE is_delete = false AND nama_genre = %s", (genre_name,))
                result = cursor.fetchone()
                
                if result[0] == 0:
                    cursor.execute("INSERT INTO genre (nama_genre) VALUES (%s)", (genre_name,))
                    connection.commit()
                    print(f"Genre '{genre_name}' berhasil ditambahkan ke database.")
                else:
                    print(f"Genre '{genre_name}' sudah ada di database.")
            except mysql.connector.Error as err:
                print("Database Error", f"Terjadi kesalahan saat menambahkan genre: {err}")
            finally:
                cursor.close()
                connection.close()
    
    def add_author_if_not_exists(self, author_name):
        connection = self.connect_db()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("SELECT COUNT(*) FROM penulis WHERE is_delete = false AND nama_penulis = %s", (author_name,))
                result = cursor.fetchone()
                
                if result[0] == 0:
                    cursor.execute("INSERT INTO penulis (nama_penulis) VALUES (%s)", (author_name,))
                    connection.commit()
                    print(f"Penulis '{author_name}' berhasil ditambahkan ke database.")
                else:
                    print(f"Penulis '{author_name}' sudah ada di database.")
            except mysql.connector.Error as err:
                print("Database Error", f"Terjadi kesalahan saat menambahkan penulis: {err}")
            finally:
                cursor.close()
                connection.close()

    def add_book(self):
        isbn = self.book_id_input.text().strip()
        judul = self.title_input.text().strip()
        penulis = self.author_input.currentText().strip()
        genre = self.genre_input.currentText().strip()
        penerbit = self.publisher_input.text().strip()
        tanggal_publikasi = self.pub_date_input.date().toString("yyyy-MM-dd")
        stock = self.stock_input.text().strip()
        
        if not judul or not penerbit or not stock :
            QMessageBox.warning(self, "Input Error", "Data tidak boleh kosong.")
            return

        if not penulis:
            QMessageBox.warning(self, "Input Error", "Silakan pilih penulis.")
            return

        if not genre:
            QMessageBox.warning(self, "Input Error", "Silakan pilih genre.")
            return

        self.add_genre_if_not_exists(genre)
        self.add_author_if_not_exists(penulis)
        connection = self.connect_db()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("SELECT COUNT(*) FROM buku WHERE isbn = %s AND is_delete = false", (isbn,))
                result = cursor.fetchone()

                if result[0] > 0:
                    QMessageBox.warning(self, "Input Error", "Tidak boleh input no ISBN yang sama")
                    return
                
                cursor.execute("INSERT INTO buku (isbn, judul, nama_penulis, nama_genre, penerbit, tanggal_publikasi, jumlah_stok) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                                (isbn, judul, penulis, genre, penerbit, tanggal_publikasi, stock))
                connection.commit()
                QMessageBox.information(self, "Success", "Buku berhasil ditambahkan.")
                self.load_books()
                self.load_genres()
                self.load_authors()
                self.clear_inputs()
            except mysql.connector.Error as err:
                QMessageBox.critical(self, "Database Error", f"Terjadi kesalahan saat menambahkan buku: {err}")
            finally:
                cursor.close()
                connection.close()


    def update_book(self):
        isbn = self.book_id_input.text().strip()
        judul = self.title_input.text().strip()
        penulis = self.author_input.currentText().strip()
        genre = self.genre_input.currentText().strip()
        penerbit = self.publisher_input.text().strip()
        tanggal_publikasi = self.pub_date_input.date().toString("yyyy-MM-dd")
        stock = self.stock_input.text().strip()
        
        if not isbn:
            QMessageBox.warning(self, "Input Error", "Silakan masukkan ISBN buku yang ingin diperbarui.")
            return
        
        self.add_genre_if_not_exists(genre)
        self.add_author_if_not_exists(penulis)

        connection = self.connect_db()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute(
                    "UPDATE buku SET judul=%s, nama_penulis=%s, nama_genre=%s, penerbit=%s, tanggal_publikasi=%s, jumlah_stok=%s WHERE isbn=%s",
                    (judul, penulis, genre, penerbit, tanggal_publikasi, stock, isbn)
                )
                connection.commit()
                QMessageBox.information(self, "Success", "Data buku berhasil diperbarui.")
                self.load_books()
                self.load_genres()
                self.load_authors()
                self.clear_inputs()
            except mysql.connector.Error as err:
                print(f"Terjadi kesalahan saat memperbarui buku: {err}")
                QMessageBox.critical(self, "Database Error", f"Terjadi kesalahan saat memperbarui buku: {err}")
            finally:
                cursor.close()
                connection.close()

    def delete_book(self):
        isbn = self.book_id_input.text().strip()
        if not isbn:
            QMessageBox.warning(self, "Input Error", "Silakan masukkan ISBN buku yang ingin dihapus.")
            return

        reply = QMessageBox.question(self, "Delete Confirmation", "Apakah Anda yakin ingin menghapus buku ini?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            connection = self.connect_db()
            if connection:
                cursor = connection.cursor()
                try:
                    cursor.execute("UPDATE buku SET is_delete = true WHERE isbn = %s", (isbn,))
                    connection.commit()
                    QMessageBox.information(self, "Success", "Buku berhasil dihapus.")
                    self.load_books()
                    self.clear_inputs()
                except mysql.connector.Error as err:
                    QMessageBox.critical(self, "Database Error", f"Terjadi kesalahan saat menghapus buku: {err}")
                finally:
                    cursor.close()
                    connection.close()

    def search_book(self):
        search_text = self.search_input.text().strip()
        connection = self.connect_db()
        if connection:
            cursor = connection.cursor()
            try:
                query = "SELECT * FROM buku WHERE is_delete = false AND (isbn LIKE %s OR judul LIKE %s)"
                cursor.execute(query, (f"%{search_text}%", f"%{search_text}%"))
                results = cursor.fetchall()
                self.book_data_table.setRowCount(0)
                
                for row_data in results:
                    row_position = self.book_data_table.rowCount()
                    self.book_data_table.insertRow(row_position)
                    for column, data in enumerate(row_data):
                        self.book_data_table.setItem(row_position, column, QTableWidgetItem(str(data)))
                
                if not results:
                    QMessageBox.information(self, "No Results", "Data buku tidak ditemukan.")
            except mysql.connector.Error as err:
                QMessageBox.critical(self, "Database Error", f"Terjadi kesalahan saat mencari buku: {err}")
            finally:
                cursor.close()
                connection.close()

