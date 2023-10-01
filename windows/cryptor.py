import sys

from PyQt6 import QtWidgets, uic, QtCore
from PyQt6 import QtGui as qtg
from PyQt6.QtGui import QIcon
from utils.constants import CRYPTOR_TEMPLATE
from utils.helpers import get_file_icon
from .encrypt import EncryptWindow

class CryptorWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        uic.loadUi(CRYPTOR_TEMPLATE, self)
        self.show()
        self.file_path = None
        self.key = None
        self.add_label.mousePressEvent = self.__select_file
        self.file_path_line_edit.textChanged.connect(self.file_path_text_changed)
        self.encrypt_button.clicked.connect(self.__encrypt)

    def file_path_text_changed(self, text):
        if text:
            self.decrypt_button.setEnabled(True)
            self.encrypt_button.setEnabled(True)
        else:
            self.decrypt_button.setEnabled(False)
            self.encrypt_button.setEnabled(False)

    def __select_file(self, *args):
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select File")
        if file_path:
            self.file_path_line_edit.setText(file_path)
            self.__set_label_image(file_path)
            self.file_path = file_path

    def __set_label_image(self, file_path):
        file_icon_path = get_file_icon(file_path)
        self.pixmap = qtg.QPixmap(file_icon_path)
        add_label_size = self.add_label.size()
        self.pixmap = self.pixmap.scaled(
            add_label_size,  QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation
        )
        self.add_label.setPixmap(self.pixmap)

    def __encrypt(self):
        self.encrypt_window = EncryptWindow(context={
            "file_path": self.file_path
        })
        self.encrypt_window.show()