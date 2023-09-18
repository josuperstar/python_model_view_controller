import sys
from PySide2 import QtGui, QtCore, QtWidgets

from model_view_controller.frameworks.qt.views.shot_list_view import ShotListView
from model_view_controller.frameworks.qt.views.property_view import PropertyView


class Controller(object):
    def __init__(self, view):
        self._property_view = view

    def raise_selection_change(self, selection):
        self._property_view.update_view(selection)

class QtShotApplication(object):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QWidget()
        application_layout = QtWidgets.QHBoxLayout(window)

        property_view = PropertyView()
        controller = Controller(property_view)

        shot_list_view = ShotListView(controller)

        window.setWindowTitle('MVC Example')




        application_layout.addWidget(shot_list_view)
        application_layout.addWidget(property_view)

        window.show()

        sys.exit(app.exec_())


if __name__ == '__main__':

    qt_application = QtShotApplication()
