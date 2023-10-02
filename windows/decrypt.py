import os
import sys
import base64
import webbrowser

from cryptography.fernet import Fernet, InvalidToken

from PyQt6 import QtWidgets, uic, QtCore
from PyQt6 import QtGui as qtg
from PyQt6.QtGui import QIcon

from utils.constants import DECRYPT_TEMPLATE, SIGNATURE
from utils.helpers import show_message_box, fit_key

class DecryptWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, context, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        uic.loadUi(DECRYPT_TEMPLATE, self)
        self.show()
        self.decrypt_button.clicked.connect(self.__decrypt)
        self.file_path = context["file_path"]

    def __decrypt(self):
        password = self.decrypt_password_line_edit.text()

        if not password:
            self.__show_message_box("password error", "passwords do not match")
            return
        
        key = fit_key(password.encode())

        with open(self.file_path, 'rb') as f:
            data = f.read().replace(SIGNATURE.encode(), b"")

        fernet = Fernet(key)

        try:
            decrypted_data = fernet.decrypt(data)
        except InvalidToken:
            show_message_box("error", "wrong password")
            return


        save_at = self.__where_to_save()

        if save_at:
            with open(save_at, "wb") as f:
                f.write(decrypted_data)
        
        # open the file
        directory_path = os.path.dirname(save_at)
        os.startfile(directory_path) 

        # close the window 
        self.close()

    def __where_to_save(self):
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, 
            "Save File", "", "All Files(*)")
        return file_name