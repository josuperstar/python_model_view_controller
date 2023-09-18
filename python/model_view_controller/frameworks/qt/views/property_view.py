from PySide2 import QtGui, QtCore, QtWidgets
from model_view_controller.adapters.abstract_view import AbstractView
from model_view_controller.adapters.presenters.shot import Shot
from model_view_controller.adapters.presenters.task import Task


class PropertyView(AbstractView):

    def __init__(self, controller, name):
        super(PropertyView, self).__init__(controller, name)
        self._widget = QtWidgets.QListWidget()
        self._font = QtGui.QFont('arial')

    def update_view(self, selection):

        self._widget.resize(400, 320)
        self._widget.clear()
        if isinstance(selection, Shot):
            self._populate_shot(selection)
        elif isinstance(selection, Task):
            self._populate_task(selection)
        else:
            raise NotImplementedError

    def _populate_shot(self, shot):
        item = QtWidgets.QListWidgetItem(shot.title)
        item.setForeground(QtGui.QColor(shot.title_color))
        item.setData(QtCore.Qt.UserRole, shot)
        self._font.setPointSize(15)
        item.setFont(self._font)
        self._widget.addItem(item)

        item = QtWidgets.QListWidgetItem(shot.description)
        item.setForeground(QtGui.QColor(shot.title_color))
        item.setData(QtCore.Qt.UserRole, shot)
        self._font.setPointSize(15)
        item.setFont(self._font)
        self._widget.addItem(item)

    def _populate_task(self, task):
        item = QtWidgets.QListWidgetItem(task.name)
        item.setForeground(QtGui.QColor(task.name))
        item.setData(QtCore.Qt.UserRole, task)
        self._font.setPointSize(15)
        item.setFont(self._font)
        self._widget.addItem(item)

        item = QtWidgets.QListWidgetItem(task.description)
        item.setForeground(QtGui.QColor(task.task_color))
        item.setData(QtCore.Qt.UserRole, task)
        self._font.setPointSize(15)
        item.setFont(self._font)
        self._widget.addItem(item)

    def get_widget(self):
        return self._widget

    def clicked(self, item):
        if not self._controller:
            raise Exception('Controller has not been set')
        shot = item.data(QtCore.Qt.UserRole)
        self._controller.raise_selection_change(self, shot)



