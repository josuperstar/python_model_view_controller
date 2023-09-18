# dialog.py

"""Dialog-style application."""

import sys

from PySide2 import QtGui, QtCore, QtWidgets

class Window(QtWidgets.QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("QDialog")
        dialogLayout = QtWidgets.QVBoxLayout()
        formLayout = QtWidgets.QFormLayout()
        formLayout.addRow("Name:", QtWidgets.QLineEdit())
        formLayout.addRow("Age:", QtWidgets.QLineEdit())
        formLayout.addRow("Job:", QtWidgets.QLineEdit())
        formLayout.addRow("Hobbies:", QtWidgets.QLineEdit())
        dialogLayout.addLayout(formLayout)
        buttons = QtWidgets.QDialogButtonBox()
        buttons.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel
            | QtWidgets.QDialogButtonBox.StandardButton.Ok
        )
        dialogLayout.addWidget(buttons)
        self.setLayout(dialogLayout)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec_())