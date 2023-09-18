from PySide2 import QtGui, QtCore, QtWidgets
from model_view_controller.adapters.abstract_view import AbstractView


class TaskListView(AbstractView):

    def __init__(self, controller, name):
        super(TaskListView, self).__init__(controller, name)
        self._widget = QtWidgets.QListWidget()
        self._widget.itemClicked.connect(self.clicked)

    def update_view(self, shot):

        font = QtGui.QFont('arial')

        self._widget.resize(400, 320)
        self._widget.clear()

        print('display tasks for shot {}'.format(shot.title))

        for task in shot.tasks:
            print('task {}'.format(task.name))
            item = QtWidgets.QListWidgetItem(task.name)
            item.setData(QtCore.Qt.UserRole, task)
            font.setPointSize(15)
            item.setFont(font)
            self._widget.addItem(item)

    def get_widget(self):
        return self._widget

    def clicked(self, item):
        shot = item.data(QtCore.Qt.UserRole)
        self._controller.raise_selection_change(self, shot)




