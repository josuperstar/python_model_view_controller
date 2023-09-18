from PySide2 import QtGui, QtCore, QtWidgets


class StatusView(QtWidgets.QListWidget):

    def __init__(self):
        super(StatusView, self).__init__()

    def update_view(self, shot):

        font = QtGui.QFont('arial')

        self.resize(400, 320)
        self.clear()

        item = QtWidgets.QListWidgetItem(shot.status)
        item.setData(QtCore.Qt.UserRole, shot)
        font.setPointSize(15)
        item.setFont(font)
        self.addItem(item)






