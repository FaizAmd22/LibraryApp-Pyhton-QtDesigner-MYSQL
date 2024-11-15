from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, 
                             QComboBox, QGridLayout, QVBoxLayout, QTableWidget, 
                             QTableWidgetItem, QMessageBox)
import mysql.connector
import re
import random

class Ui_FormAnggota(QWidget):
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
        self.setWindowTitle("Data Anggota")
        self.resize(850, 600)
        self.verticalLayout = QVBoxLayout(self)

        self.label = QLabel("Data Anggota")
        self.label.setStyleSheet("font-size:20px; font-weight: bold; text-align: center; margin: 10px 0;")
        self.verticalLayout.addWidget(self.label)

        self.member_id_label = QLabel("Anggota ID")
        self.member_id_input = QLineEdit()
        self.member_id_input.setDisabled(True)
        self.name_label = QLabel("Nama")
        self.name_input = QLineEdit()
        self.gender_label = QLabel("Jenis Kelamin")
        self.gender_combobox = QComboBox()
        self.gender_combobox.addItems(["Laki-laki", "Perempuan"])
        self.address_label = QLabel("Alamat")
        self.address_input = QLineEdit()
        self.phone_label = QLabel("No Telepon")
        self.phone_input = QLineEdit()
        self.email_label = QLabel("Email")
        self.email_input = QLineEdit()

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
        self.form_layout.addWidget(self.member_id_label, 0, 0)
        self.form_layout.addWidget(self.member_id_input, 0, 1)
        self.form_layout.addWidget(self.name_label, 1, 0)
        self.form_layout.addWidget(self.name_input, 1, 1)
        self.form_layout.addWidget(self.gender_label, 2, 0)
        self.form_layout.addWidget(self.gender_combobox, 2, 1)
        self.form_layout.addWidget(self.address_label, 3, 0)
        self.form_layout.addWidget(self.address_input, 3, 1)
        self.form_layout.addWidget(self.phone_label, 4, 0)
        self.form_layout.addWidget(self.phone_input, 4, 1)
        self.form_layout.addWidget(self.email_label, 5, 0)
        self.form_layout.addWidget(self.email_input, 5, 1)
        self.form_layout.addWidget(self.add_button, 0, 2)
        self.form_layout.addWidget(self.update_button, 1, 2)
        self.form_layout.addWidget(self.delete_button, 2, 2)
        self.form_layout.addWidget(self.reset_button, 3, 2)

        self.verticalLayout.addLayout(self.form_layout)

        self.search_label = QLabel("Anggota ID / Nama")
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
        self.search_input.setPlaceholderText("Masukkan Anggota ID / Nama anggota")
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
        self.member_data_table = QTableWidget()
        self.member_data_table.setColumnCount(6)
        self.member_data_table.setHorizontalHeaderLabels(["Anggota ID", "Nama", "Jenis Kelamin", "Alamat", "No Telepon", "Email"])
        self.member_data_table.horizontalHeader().setStretchLastSection(True)
        self.member_data_table.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.search_label)
        self.verticalLayout.addWidget(self.search_input)
        self.verticalLayout.addWidget(self.search_button)
        self.verticalLayout.addWidget(self.member_data_table)

        self.btnBack = QPushButton("Kembali")
        self.btnBack.setStyleSheet("QPushButton { background-color: rgb(255, 255, 255); border: none; "
                      "border-radius: 10px; color: rgb(73, 84, 100); padding: 10px; font-size: 12px; font-weight: bold; "
                      "margin-top: 30px; }"
                      "QPushButton:hover { background-color: rgb(73, 84, 100); color: white; }")
        self.verticalLayout.addWidget(self.btnBack)

        self.add_button.clicked.connect(self.add_member)
        self.update_button.clicked.connect(self.update_member)
        self.delete_button.clicked.connect(self.delete_member)
        self.search_button.clicked.connect(self.search_member)
        self.reset_button.clicked.connect(self.clear_input_fields)

        self.load_members()

    def load_members(self):
        connection = self.connect_db()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM anggota WHERE is_delete = false ORDER BY created_at DESC")
            results = cursor.fetchall()
            self.member_data_table.setRowCount(0)
            existing_ids = set()
            
            for row in results:
                row_position = self.member_data_table.rowCount()
                self.member_data_table.insertRow(row_position)
                for column, data in enumerate(row):
                    self.member_data_table.setItem(row_position, column, QTableWidgetItem(str(data)))
                    if column == 0:
                        existing_ids.add(data)
            
            cursor.close()
            connection.close()
            self.generate_unique_member_id(existing_ids)

    def generate_unique_member_id(self, existing_ids):
        """Generate a unique Member ID that does not exist in the database."""
        while True:
            random_number = random.randint(00000, 99999)
            unique_id = f"MBR{random_number}"
            if unique_id not in existing_ids:
                self.member_id_input.setText(unique_id)
                return unique_id
    
    def clear_input_fields(self):
        """Mengosongkan semua field input pada form anggota."""
        self.member_id_input.clear()
        self.name_input.clear()
        self.gender_combobox.setCurrentIndex(0)
        self.phone_input.clear()
        self.address_input.clear()
        self.email_input.clear()

        self.load_members()

    def add_member(self):
        connection = self.connect_db()
        if connection:
            cursor = connection.cursor()
            anggota_id = self.member_id_input.text().strip()
            nama = self.name_input.text().strip()
            gender = self.gender_combobox.currentText().strip()
            phone = self.phone_input.text().strip()
            address = self.address_input.text().strip()
            email = self.email_input.text().strip()

            if not anggota_id or not nama or not gender or not phone or not address or not email:
                QMessageBox.warning(self, "Input Error", "Semua field harus diisi.")
                return

            email_regex = r"[^@]+@[^@]+\.[^@]+"
            if not re.match(email_regex, email):
                QMessageBox.warning(self, "Invalid Email", "Format email tidak valid.")
                return

            if not phone.isdigit() or len(phone) < 10:
                QMessageBox.warning(self, "Invalid Phone Number", "Nomor telepon harus hanya berisi angka dan minimal 10 digit.")
                return

            try:
                cursor.execute("SELECT COUNT(*) FROM anggota WHERE is_delete = false AND id_anggota = %s", (anggota_id,))
                if cursor.fetchone()[0] > 0:
                    QMessageBox.warning(self, "Duplicate ID", "ID Anggota sudah ada. Gunakan ID yang berbeda.")
                    return

                cursor.execute("INSERT INTO anggota (id_anggota, nama_anggota, jenis_kelamin, alamat, no_hp, email) VALUES (%s, %s, %s, %s, %s, %s)", 
                               (anggota_id, nama, gender, address, phone, email))
                connection.commit()
                QMessageBox.information(self, "Success", "Anggota berhasil ditambahkan.")
                self.clear_input_fields()
            except Exception as e:
                QMessageBox.critical(self, "Unexpected Error", f"Error: {e}")
            finally:
                cursor.close()
                connection.close()

    def update_member(self):
        connection = self.connect_db()
        if connection:
            cursor = connection.cursor()
            anggota_id = self.member_id_input.text().strip()
            nama = self.name_input.text().strip()
            gender = self.gender_combobox.currentText().strip()
            phone = self.phone_input.text().strip()
            address = self.address_input.text().strip()
            email = self.email_input.text().strip()

            if not anggota_id:
                QMessageBox.warning(self, "Input Error", "ID Anggota harus diisi untuk update.")
                return

            try:
                cursor.execute("UPDATE anggota SET nama_anggota=%s, jenis_kelamin=%s, alamat=%s, no_hp=%s, email=%s WHERE id_anggota=%s", 
                               (nama, gender, address, phone, email, anggota_id))
                connection.commit()
                QMessageBox.information(self, "Success", "Anggota berhasil diupdate.")
                self.clear_input_fields()
            except Exception as e:
                QMessageBox.critical(self, "Unexpected Error", f"Error: {e}")
            finally:
                cursor.close()
                connection.close()

    def delete_member(self):
        reply = QMessageBox.question(self, "Delete Confirmation", "Apakah Anda yakin ingin menghapus anggota?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            connection = self.connect_db()
            if connection:
                cursor = connection.cursor()
                anggota_id = self.member_id_input.text().strip()

                if not anggota_id:
                    QMessageBox.warning(self, "Input Error", "ID Anggota harus diisi untuk delete.")
                    return

                try:
                    cursor.execute("UPDATE anggota SET is_delete=true WHERE id_anggota = %s", (anggota_id,))
                    connection.commit()
                    QMessageBox.information(self, "Success", "Anggota berhasil dihapus.")
                    self.clear_input_fields()
                except Exception as e:
                    QMessageBox.critical(self, "Unexpected Error", f"Error: {e}")
                finally:
                    cursor.close()
                    connection.close()
        else :
            self.clear_input_fields()

    def search_member(self):
        connection = self.connect_db()
        if connection:
            cursor = connection.cursor()
            search_term = self.search_input.text().strip()
            query = "SELECT * FROM anggota WHERE id_anggota LIKE %s OR nama_anggota LIKE %s"
            try:
                cursor.execute(query, ('%' + search_term + '%', '%' + search_term + '%'))
                results = cursor.fetchall()
                self.member_data_table.setRowCount(0)
                for row_data in results:
                    row_position = self.member_data_table.rowCount()
                    self.member_data_table.insertRow(row_position)
                    for col, data in enumerate(row_data):
                        self.member_data_table.setItem(row_position, col, QTableWidgetItem(str(data)))
            except Exception as e:
                QMessageBox.critical(self, "Unexpected Error", f"Error: {e}")
            finally:
                cursor.close()
                connection.close()
