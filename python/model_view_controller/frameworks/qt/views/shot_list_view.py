from PySide2 import QtGui, QtCore, QtWidgets
from model_view_controller.adapters.presenters.shot import Shot


class ShotListView(QtWidgets.QListWidget):

    selected_shot = None

    def __init__(self, controller):
        super(ShotListView, self).__init__()
        self._controller = controller
        list_of_presenters = list()
        shot_a = Shot()
        shot_b = Shot()
        shot_b.title = 'test 2'
        shot_b.title_color = 'green'
        list_of_presenters.append(shot_a)
        list_of_presenters.append(shot_b)

        font = QtGui.QFont('arial')

        self.resize(400, 320)
        for shot in list_of_presenters:
            item = QtWidgets.QListWidgetItem(shot.title)
            item.setForeground(QtGui.QColor(shot.title_color))
            item.setData(QtCore.Qt.UserRole, shot)
            font.setPointSize(15)
            item.setFont(font)
            self.addItem(item)

        self.itemClicked.connect(self.clicked)

    def clicked(self, item):
        shot = item.data(QtCore.Qt.UserRole)
        self.selected_shot = shot
        self._controller.raise_selection_change(shot)


