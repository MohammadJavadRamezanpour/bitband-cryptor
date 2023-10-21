import os

from PyQt6 import QtWidgets

class Window(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def where_to_save(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "where to save")
        return file_path
    
    def show_message_box(self, title, text):
        message_box = QtWidgets.QMessageBox(self)

        message_box.setWindowTitle(title)
        message_box.setText(text)
        message_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)

        message_box.exec()

    def open_file_directory(self, directory:str) -> None:
        file_path = os.path.dirname(directory)
        os.startfile(file_path)