import sys
from PySide2 import QtGui, QtCore, QtWidgets

from model_view_controller.frameworks.qt.views.shot_list_view import ShotListView
from model_view_controller.frameworks.qt.views.property_view import PropertyView
from model_view_controller.frameworks.qt.views.status_view import StatusView


class Controller(object):
    def __init__(self):
        self._views = list()

    def add_view(self, view):
        self._views.append(view)

    def raise_selection_change(self, selection):
        for view in self._views:
            view.update_view(selection)


class QtShotApplication(object):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QWidget()
        application_layout = QtWidgets.QHBoxLayout(window)

        status_view = StatusView()
        property_view = PropertyView()

        controller = Controller()

        shot_list_view = ShotListView(controller)

        controller.add_view(status_view)
        controller.add_view(property_view)

        window.setWindowTitle('MVC Example')

        application_layout.addWidget(shot_list_view)
        application_layout.addWidget(property_view)
        application_layout.addWidget(status_view)

        window.show()

        sys.exit(app.exec_())


if __name__ == '__main__':
    qt_application = QtShotApplication()
