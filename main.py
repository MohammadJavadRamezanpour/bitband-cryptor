import sys

from PyQt6 import QtWidgets
from windows.cryptor import CryptorWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = CryptorWindow()
    app.exec()