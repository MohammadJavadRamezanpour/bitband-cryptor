from cryptography.fernet import Fernet, InvalidToken

from PyQt6 import uic

from utils.constants import DECRYPT_TEMPLATE_ADDRESS, SIGNATURE
from utils.helpers import fit_key
from windows.window import Window


class DecryptWindow(Window):
    def __init__(self, *args, context=None, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi(DECRYPT_TEMPLATE_ADDRESS, self)
        self.show()

        self.decrypt_button.clicked.connect(self.__decrypt)
        self.file_path = context["file_path"]

    def __get_key(self):
        password = self.password_line_edit.text()
        return fit_key(password.encode())
    
    def __get_cleared_data(self, encrypted_data):
        key = self.__get_key()
        fernet = Fernet(key)
        return fernet.decrypt(encrypted_data.replace(SIGNATURE.encode(), b''))
    
    def __decrypt(self):
        if self.file_path is None:
            self.show_message_box("error", "no file is selected")
            return
        
        with open(self.file_path, "rb") as file:
            encrypted_data = file.read()

        try:
            cleared_data = self.__get_cleared_data(encrypted_data)
        except InvalidToken:
            self.show_message_box("error", "password is wrong please try again")
            return

        save_to = self.where_to_save()

        if save_to is None:
            return
        
        with open(save_to, "wb") as file:
            file.write(cleared_data)

        # open the file directory
        self.open_file_directory(save_to)

        # close the window
        self.close()