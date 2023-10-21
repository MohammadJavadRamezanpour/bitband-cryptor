import sys

from PyQt6 import QtWidgets, uic, QtCore, QtGui as qtg
from PyQt6.QtWidgets import QWidget

from utils.constants import CRYPTOR_TEMPLATE_ADDRESS
from utils.helpers import get_file_icon_path
from windows.encrypt import EncryptWindow
from windows.decrypt import DecryptWindow


class CryptorWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi(CRYPTOR_TEMPLATE_ADDRESS, self)
        self.show()

        self.file_path = None

        self.select_label.mousePressEvent = self.__select_file
        self.path_line_edit.textChanged.connect(self.__path_changed)
        self.encrypt_button.clicked.connect(self.__encrypt)
        self.decrypt_button.clicked.connect(self.__decrypt)

    def __select_file(self, *args):
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select any File")

        if file_path:
            self.path_line_edit.setText(file_path)
            self.__set_label_icon(file_path)
            self.file_path = file_path

    def __path_changed(self, text):
        self.encrypt_button.setEnabled(bool(text))
        self.decrypt_button.setEnabled(bool(text))

    def __set_label_icon(self, file_path):
        file_icon_path = get_file_icon_path(file_path)
        self.pixmap = qtg.QPixmap(file_icon_path)
        select_label_size = self.select_label.size()
        self.pixmap = self.pixmap.scaled(
            select_label_size,
            QtCore.Qt.AspectRatioMode.KeepAspectRatio,
            QtCore.Qt.TransformationMode.SmoothTransformation,
        )
        self.select_label.setPixmap(self.pixmap)

    def __encrypt(self):
        if self.file_path is None:
            return
        
        self.encrypt_window = EncryptWindow(context={"file_path": self.file_path})
        self.encrypt_window.show()

    def __decrypt(self):
        if self.file_path is None:
            return
        
        self.decrypt_window = DecryptWindow(context={"file_path": self.file_path})
        self.decrypt_window.show()
        

