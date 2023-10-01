import os
import sys
import base64
import webbrowser

from cryptography.fernet import Fernet

from PyQt6 import QtWidgets, uic, QtCore
from PyQt6 import QtGui as qtg
from PyQt6.QtGui import QIcon

from utils.constants import ENCRYPT_TEMPLATE, SIGNATURE
from utils.helpers import get_file_icon, fit_key

class EncryptWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, context, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        uic.loadUi(ENCRYPT_TEMPLATE, self)
        self.show()
        self.encrypt_button.clicked.connect(self.__encrypt)
        self.file_path = context["file_path"]

    def __encrypt(self):
        password = self.encrypt_password_line_edit.text()
        reapeat_password = self.encrypt_repeat_password_line_edit.text()
        
        if password == reapeat_password:
            key = fit_key(password.encode())

            with open(self.file_path, 'rb') as f:
                data = f.read()

            fernet = Fernet(key)
            encrypted_data = fernet.encrypt(data)

            save_at = self.__where_to_save()

            if save_at:
                with open(save_at, "wb") as f:
                    f.write(encrypted_data + SIGNATURE.encode())
            
            # open the file
            directory_path = os.path.dirname(save_at)
            os.startfile(directory_path) 

            # close the window 
            self.close()
        else:
            self.__show_message_box("password error", "passwords do not match")

    def __where_to_save(self):
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, 
            "Save File", "", "All Files(*)")
        return file_name
    
    def __show_message_box(self, title, message):
        # Create a QMessageBox object.
        message_box = QtWidgets.QMessageBox(self)

        # Set the text of the message box.
        message_box.setText(message)
        message_box.setWindowTitle(title)

        # Set the icon of the message box.
        message_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)

        # Show the message box.
        message_box.exec()