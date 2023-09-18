from PySide2 import QtGui, QtCore, QtWidgets
from model_view_controller.adapters.presenters.shot import Shot


class PropertyView(QtWidgets.QListWidget):

    def __init__(self):
        super(PropertyView, self).__init__()

    def update_view(self, shot):

        font = QtGui.QFont('arial')

        self.resize(400, 320)
        self.clear()

        item = QtWidgets.QListWidgetItem(shot.title)
        item.setForeground(QtGui.QColor(shot.title_color))
        item.setData(QtCore.Qt.UserRole, shot)
        font.setPointSize(15)
        item.setFont(font)
        self.addItem(item)

        item = QtWidgets.QListWidgetItem(shot.description)
        item.setForeground(QtGui.QColor(shot.title_color))
        item.setData(QtCore.Qt.UserRole, shot)
        font.setPointSize(15)
        item.setFont(font)
        self.addItem(item)




