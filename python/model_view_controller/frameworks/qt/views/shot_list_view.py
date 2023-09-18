from PySide2 import QtGui, QtCore, QtWidgets

from model_view_controller.adapters.abstract_view import AbstractView


class ShotListView(AbstractView):

    def __init__(self, controller, name):
        super(ShotListView, self).__init__(controller, name)
        self._widget = QtWidgets.QListWidget()

        list_of_presenters = controller.get_list_of_shot()

        font = QtGui.QFont('arial')

        self._widget.resize(400, 320)
        for shot in list_of_presenters:
            item = QtWidgets.QListWidgetItem(shot.title)
            item.setForeground(QtGui.QColor(shot.title_color))
            item.setData(QtCore.Qt.UserRole, shot)
            font.setPointSize(15)
            item.setFont(font)
            self._widget.addItem(item)

        self._widget.itemClicked.connect(self.clicked)

    def get_widget(self):
        return self._widget

    def update_view(self, data):
        pass

    def clicked(self, item):
        shot = item.data(QtCore.Qt.UserRole)
        self._controller.raise_selection_change(self, shot)


