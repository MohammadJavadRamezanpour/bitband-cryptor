import sys

from PyQt6 import QtWidgets, uic
from PyQt6 import QtGui as qtg
from PyQt6.QtGui import QIcon
from utils.constants import CRYPTOR_TEMPLATE

class CryptorWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        uic.loadUi(CRYPTOR_TEMPLATE, self)
        self.show()