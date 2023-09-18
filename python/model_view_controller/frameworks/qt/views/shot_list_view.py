from PySide2 import QtGui, QtCore, QtWidgets
from model_view_controller.adapters.presenters.shot import Shot


class ShotListView(QtWidgets.QListWidget):

    def __init__(self):
        super(ShotListView, self).__init__()
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

    def clicked(self, item):
        shot = item.data(QtCore.Qt.UserRole)
        print(shot)
        QtWidgets.QMessageBox.information(self, "Shot Information",
                                "title: {} \ndescription: {}".format(shot.title, shot.description))


