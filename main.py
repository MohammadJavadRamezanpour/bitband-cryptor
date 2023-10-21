import sys

from PyQt6 import QtWidgets

from windows import CryptorWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = CryptorWindow()
    app.exec()