from PySide2 import QtGui, QtCore, QtWidgets
from model_view_controller.adapters.abstract_view import AbstractView


class StatusView(AbstractView):

    def __init__(self, controller):
        super(StatusView, self).__init__(controller)
        self._widget = QtWidgets.QListWidget()

    def update_view(self, shot):

        font = QtGui.QFont('arial')

        self._widget.resize(400, 320)
        self._widget.clear()

        item = QtWidgets.QListWidgetItem(shot.status)
        item.setData(QtCore.Qt.UserRole, shot)
        font.setPointSize(15)
        item.setFont(font)
        self._widget.addItem(item)

    def get_widget(self):
        return self._widget





