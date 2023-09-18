import sys
from PySide2 import QtGui, QtCore, QtWidgets

from model_view_controller.adapters.controller import Controller

from model_view_controller.frameworks.qt.views.shot_list_view import ShotListView
from model_view_controller.frameworks.qt.views.property_view import PropertyView
from model_view_controller.frameworks.qt.views.task_list_view import TaskListView


class QtShotApplication(object):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QWidget()
        application_layout = QtWidgets.QHBoxLayout(window)

        controller = Controller()

        shot_list_view = ShotListView(controller, 'shot_list')
        status_view = TaskListView(controller, 'task_list')
        property_view = PropertyView(controller, 'properties')

        controller.add_view(status_view)
        controller.add_view(property_view)

        window.setWindowTitle('MVC Example')

        application_layout.addWidget(shot_list_view.get_widget())
        application_layout.addWidget(status_view.get_widget())
        application_layout.addWidget(property_view.get_widget())

        window.show()

        sys.exit(app.exec_())


if __name__ == '__main__':
    qt_application = QtShotApplication()
