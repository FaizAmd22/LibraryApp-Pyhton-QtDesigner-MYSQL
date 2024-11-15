from PyQt5.QtWidgets import (QWidget, QLabel, QComboBox, QPushButton, QDateEdit, QGridLayout, QVBoxLayout, QMessageBox, QLineEdit, QTableWidget, QTableWidgetItem)
from PyQt5.QtCore import QDate
import mysql.connector
import random
from components.form_anggota import Ui_FormAnggota
from components.form_buku import Ui_FormBuku

class Ui_FormTransaksi(QWidget):
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
        self.setWindowTitle("Data Transaksi Peminjaman Buku")
        self.resize(850, 600)
        self.verticalLayout = QVBoxLayout(self)

        self.label = QLabel("Data Transaksi Peminjaman Buku")
        self.label.setStyleSheet("font-size:20px; font-weight: bold; text-align: center; margin: 10px 0;")
        self.verticalLayout.addWidget(self.label)

        self.id_peminjaman_label = QLabel("ID Peminjaman")
        self.id_peminjaman_input = QLineEdit()
        self.id_peminjaman_input.setDisabled(True)

        self.nama_anggota_label = QLabel("Nama Anggota")
        self.nama_anggota_input = QComboBox()

        self.judul_buku_label = QLabel("Judul Buku")
        self.judul_buku_input = QComboBox()

        self.tgl_peminjaman_label = QLabel("Tanggal Peminjaman")
        self.tgl_peminjaman_input = QDateEdit()
        self.tgl_peminjaman_input.setCalendarPopup(True)
        self.tgl_peminjaman_input.setDisplayFormat("yyyy-MM-dd")
        self.tgl_peminjaman_input.setDate(QDate.currentDate())

        self.tgl_pengembalian_label = QLabel("Tanggal Pengembalian")
        self.tgl_pengembalian_input = QDateEdit()
        self.tgl_pengembalian_input.setCalendarPopup(True)
        self.tgl_pengembalian_input.setDisplayFormat("yyyy-MM-dd")
        self.tgl_pengembalian_input.setDate(QDate.currentDate().addDays(7))

        # self.tgl_dikembalikan_label = QLabel("Tanggal Dikembalikan")
        # self.tgl_dikembalikan_input = QDateEdit()
        # self.tgl_dikembalikan_input.setCalendarPopup(True)
        # self.tgl_dikembalikan_input.setDisplayFormat("yyyy-MM-dd")
        # self.tgl_dikembalikan_input.setDate(QDate.currentDate())

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
        self.reset_button = QPushButton("Reset")
        self.members_table_button = QPushButton("Tabel Anggota")
        self.members_table_button.setStyleSheet("QPushButton {\n"
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
        self.books_table_button = QPushButton("Tabel Buku")
        self.books_table_button.setStyleSheet("QPushButton {\n"
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

        self.form_layout = QGridLayout()
        self.form_layout.addWidget(self.id_peminjaman_label, 0, 0)
        self.form_layout.addWidget(self.id_peminjaman_input, 0, 1)
        self.form_layout.addWidget(self.nama_anggota_label, 1, 0)
        self.form_layout.addWidget(self.nama_anggota_input, 1, 1)
        self.form_layout.addWidget(self.judul_buku_label, 2, 0)
        self.form_layout.addWidget(self.judul_buku_input, 2, 1)
        self.form_layout.addWidget(self.tgl_peminjaman_label, 3, 0)
        self.form_layout.addWidget(self.tgl_peminjaman_input, 3, 1)
        self.form_layout.addWidget(self.tgl_pengembalian_label, 4, 0)
        self.form_layout.addWidget(self.tgl_pengembalian_input, 4, 1)
        # self.form_layout.addWidget(self.tgl_dikembalikan_label, 5, 0)
        # self.form_layout.addWidget(self.tgl_dikembalikan_input, 5, 1)
        self.form_layout.addWidget(self.add_button, 0, 2)
        # self.form_layout.addWidget(self.reset_button, 1, 2)
        self.form_layout.addWidget(self.members_table_button, 1, 2)
        self.form_layout.addWidget(self.books_table_button, 2, 2)
        self.verticalLayout.addLayout(self.form_layout)

        self.search_label = QLabel("Cari Nama Anggota / Judul Buku")
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

        self.verticalLayout.addWidget(self.search_label)
        self.verticalLayout.addWidget(self.search_input)
        self.verticalLayout.addWidget(self.search_button)


        self.transaction_data_table = QTableWidget()
        self.transaction_data_table.setColumnCount(6)
        self.transaction_data_table.setHorizontalHeaderLabels(["ID Peminjaman", "Nama Anggota", "Judul Buku", "Tanggal Peminjaman", "Tanggal Pengembalian", "Tanggal Dikembalikan"])
        self.transaction_data_table.horizontalHeader().setStretchLastSection(True)
        self.transaction_data_table.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.transaction_data_table)

        self.btnBack = QPushButton("Kembali")
        self.btnBack.setStyleSheet("QPushButton { background-color: rgb(255, 255, 255); border: none; "
                      "border-radius: 10px; color: rgb(73, 84, 100); padding: 10px; font-size: 12px; font-weight: bold; "
                      "margin-top: 30px; }"
                      "QPushButton:hover { background-color: rgb(73, 84, 100); color: white; }")
        self.verticalLayout.addWidget(self.btnBack)

        self.load_data_to_comboboxes()
        self.load_datas()

        self.add_button.clicked.connect(self.add_transaction)
        self.reset_button.clicked.connect(self.clear_input)
        self.members_table_button.clicked.connect(self.open_form_anggota)
        self.books_table_button.clicked.connect(self.open_form_buku)
        self.search_button.clicked.connect(self.search_transaction)

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

    def close_form_anggota(self):
        self.formAnggota.close()
        self.load_data_to_comboboxes()

    def close_form_buku(self):
        self.formBuku.close()
        self.load_data_to_comboboxes()

    def load_data_input_anggota(self, row, column):
        item = self.formAnggota.member_data_table.item(row, column)
        if item is not None:
            self.formAnggota.member_id_input.setText(self.formAnggota.member_data_table.item(row, 0).text())
            self.formAnggota.name_input.setText(self.formAnggota.member_data_table.item(row, 1).text())
            self.formAnggota.gender_combobox.setCurrentText(self.formAnggota.member_data_table.item(row, 2).text())
            self.formAnggota.address_input.setText(self.formAnggota.member_data_table.item(row, 3).text())
            self.formAnggota.phone_input.setText(self.formAnggota.member_data_table.item(row, 4).text())
            self.formAnggota.email_input.setText(self.formAnggota.member_data_table.item(row, 5).text())
    
    def load_data_input_buku(self, row, column):
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

    def load_data_to_comboboxes(self):
        connection = self.connect_db()
        if connection:
            cursor = connection.cursor()

            self.nama_anggota_input.clear()
            self.judul_buku_input.clear()

            cursor.execute("SELECT id_anggota, nama_anggota FROM anggota WHERE is_delete = 0")
            anggota_data = cursor.fetchall()
            self.nama_anggota_input.addItem("")
            for id, nama in anggota_data:
                self.nama_anggota_input.addItem(nama, id)
            

            cursor.execute("SELECT isbn, judul FROM buku WHERE is_delete = 0 AND jumlah_stok > 0")
            buku_data = cursor.fetchall()
            self.judul_buku_input.addItem("")
            for id, judul in buku_data:
                self.judul_buku_input.addItem(judul, id)


            cursor.close()
            connection.close()

    def load_datas(self):
        connection = self.connect_db()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM peminjaman_buku WHERE is_delete = false ORDER BY created_at DESC")
            results = cursor.fetchall()
            self.transaction_data_table.setRowCount(0)
            existing_ids = set()
            
            for row in results:
                row_position = self.transaction_data_table.rowCount()
                self.transaction_data_table.insertRow(row_position)
                for column, data in enumerate(row):
                    self.transaction_data_table.setItem(row_position, column, QTableWidgetItem(str(data)))
                    
                    if column == 5 and data is None:
                        btn = QPushButton("Belum Dikembalikan")
                        btn.clicked.connect(lambda state, row=row: self.update_return_date(row))
                        self.transaction_data_table.setCellWidget(row_position, column, btn)
                    if column == 0:
                        existing_ids.add(data)

            cursor.close()
            connection.close()
            self.generate_unique_member_id(existing_ids)


    def generate_unique_member_id(self, existing_ids):
        """Generate a unique Member ID that does not exist in the database."""
        while True:
            random_number = random.randint(0, 99999999)
            unique_id = f"{random_number:08d}"
            if unique_id not in existing_ids:
                self.id_peminjaman_input.setText(unique_id)
                return unique_id
            
    def update_return_date(self, row_data):
        id_peminjaman = row_data[0]
        nama = row_data[1]
        judul_buku = row_data[2]
        current_date = QDate.currentDate().toString("yyyy-MM-dd")

        reply = QMessageBox.question(self, "Delete Confirmation", f"Apakah Buku ini sudah dikembalikan ?\n ID : {id_peminjaman} \n Judul Buku : {judul_buku} \n Nama Anggota : {nama}", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            connection = self.connect_db()
            if connection:
                cursor = connection.cursor()
                try:
                    query = """
                    UPDATE peminjaman_buku
                    SET tanggal_pengembalian = %s
                    WHERE id_peminjaman = %s
                    """
                    cursor.execute(query, (current_date, id_peminjaman))

                    query_update_stok = """
                    UPDATE buku
                    SET jumlah_stok = jumlah_stok + 1
                    WHERE judul = %s
                    """
                    cursor.execute(query_update_stok, (judul_buku,))
                    connection.commit()
                    QMessageBox.information(self, "Success", f"Buku telah dikembalikan!.")
                except Exception as e:
                    QMessageBox.warning(self, "Error", f"Terjadi kesalahan: {str(e)}")
                finally:
                    cursor.close()
                    connection.close()

            self.load_datas()

            
    def clear_input(self):
        self.id_peminjaman_input.clear()
        self.nama_anggota_input.setCurrentIndex(0)
        self.judul_buku_input.setCurrentIndex(0)
        self.tgl_peminjaman_input.setDate(QDate.currentDate())
        self.tgl_pengembalian_input.setDate(QDate.currentDate().addDays(7))

        self.load_datas()



    def add_transaction(self):
        id_pinjam = self.id_peminjaman_input.text().strip()
        nama_anggota = self.nama_anggota_input.currentText().strip()
        judul_buku = self.judul_buku_input.currentText().strip()
        tgl_peminjaman = self.tgl_peminjaman_input.date().toString("yyyy-MM-dd")
        tgl_pengembalian = self.tgl_pengembalian_input.date().toString("yyyy-MM-dd")

        if not nama_anggota or not judul_buku:
            QMessageBox.warning(self, "Warning", "Nama Anggota dan Judul Buku harus diisi")
            return

        connection = self.connect_db()
        if connection:
            cursor = connection.cursor()
            
            try:
                query_peminjaman = """
                INSERT INTO peminjaman_buku (id_peminjaman, nama_anggota, judul_buku, tanggal_peminjaman, tanggal_untuk_pengembalian)
                VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(query_peminjaman, (id_pinjam, nama_anggota, judul_buku, tgl_peminjaman, tgl_pengembalian))
                
                query_update_stok = """
                UPDATE buku
                SET jumlah_stok = jumlah_stok - 1
                WHERE judul = %s AND jumlah_stok > 0
                """
                cursor.execute(query_update_stok, (judul_buku,))
                
                connection.commit()
                QMessageBox.information(self, "Success", "Transaksi Peminjaman Buku Berhasil!")
            except Exception as e:
                connection.rollback()
                QMessageBox.warning(self, "Error", f"Terjadi kesalahan: {str(e)}")
            finally:
                cursor.close()
                connection.close()

            self.clear_input()
            self.load_datas()
            self.load_data_to_comboboxes()



    def update_transaction(self):
        QMessageBox.information(self, "Info", "Function update_transaction dipanggil")

    def delete_transaction(self):
        QMessageBox.information(self, "Info", "Function delete_transaction dipanggil")

    def search_transaction(self):
        connection = self.connect_db()
        if connection:
            cursor = connection.cursor()
            search_term = self.search_input.text().strip()
            query = "SELECT * FROM peminjaman_buku WHERE judul_buku LIKE %s OR nama_anggota LIKE %s"
            try:
                cursor.execute(query, ('%' + search_term + '%', '%' + search_term + '%'))
                results = cursor.fetchall()
                self.transaction_data_table.setRowCount(0)
                for row_data in results:
                    row_position = self.transaction_data_table.rowCount()
                    self.transaction_data_table.insertRow(row_position)
                    for col, data in enumerate(row_data):
                        self.transaction_data_table.setItem(row_position, col, QTableWidgetItem(str(data)))
            except Exception as e:
                QMessageBox.critical(self, "Unexpected Error", f"Error: {e}")
            finally:
                cursor.close()
                connection.close()
