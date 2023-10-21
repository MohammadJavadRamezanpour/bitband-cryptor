from cryptography.fernet import Fernet, InvalidToken

from PyQt6 import QtWidgets, uic

from utils.constants import ENCRYPT_TEMPLATE_ADDRESS, SIGNATURE
from utils.helpers import fit_key
from windows.window import Window


class EncryptWindow(Window):
    def __init__(self, *args, context=None, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi(ENCRYPT_TEMPLATE_ADDRESS, self)
        self.show()

        self.encrypt_button.clicked.connect(self.__encrypt)
        self.file_path = context["file_path"]

    def __are_passwords_equal(self) -> bool:
        return self.password_line_edit.text() == self.password_repeat_line_edit.text()

    def __get_key(self):
        password = self.password_line_edit.text()
        return fit_key(password.encode())
    
    def __get_encrypted_data(self, clear_data):
        key = self.__get_key()
        fernet = Fernet(key)
        return fernet.encrypt(clear_data) + SIGNATURE.encode()

    def __encrypt(self):
        if self.file_path is None:
            self.show_message_box("error", "no file is selected")
            return

        if not self.__are_passwords_equal():
            self.show_message_box("error", "passwords do not match")
            return
        
        with open(self.file_path, "rb") as file:
            clear_data = file.read()

        encrypted_data = self.__get_encrypted_data(clear_data)

        save_to = self.where_to_save()

        if save_to is None:
            return
        
        with open(save_to, "wb") as file:
            file.write(encrypted_data)

        # open the file directory
        self.open_file_directory(save_to)

        # close the window
        self.close()