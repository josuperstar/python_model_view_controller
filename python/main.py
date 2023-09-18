import sys
from PySide2 import QtGui, QtCore, QtWidgets

from model_view_controller.frameworks.qt.views.shot_list_view import ShotListView


class QtShotApplication(object):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        
        shot_list_view = ShotListView()



        shot_list_view.setWindowTitle('QListwidget Example')
        shot_list_view.itemClicked.connect(shot_list_view.clicked)

        shot_list_view.show()
        sys.exit(app.exec_())


if __name__ == '__main__':

    qt_application = QtShotApplication()
