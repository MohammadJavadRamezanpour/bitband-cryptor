from PyQt6 import QtWidgets

def show_message_box(title, message):
    # Create a QMessageBox object.
    message_box = QtWidgets.QMessageBox(None)

    # Set the text of the message box.
    message_box.setText(message)
    message_box.setWindowTitle(title)

    # Set the icon of the message box.
    message_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)

    # Show the message box.
    message_box.exec()