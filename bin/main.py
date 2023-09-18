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

        shot_list_layout = QtWidgets.QVBoxLayout()
        shot_list_label = QtWidgets.QLabel('Shot List View')
        shot_list_view = ShotListView(controller, 'shot_list')
        shot_list_layout.addWidget(shot_list_label)
        shot_list_layout.addWidget(shot_list_view.get_widget())
        application_layout.addLayout(shot_list_layout)

        task_list_layout = QtWidgets.QVBoxLayout()
        task_list_label = QtWidgets.QLabel('Task List View')
        status_view = TaskListView(controller, 'task_list')
        task_list_layout.addWidget(task_list_label)
        task_list_layout.addWidget(status_view.get_widget())
        application_layout.addLayout(task_list_layout)

        property_view_layout = QtWidgets.QVBoxLayout()
        property_view_label = QtWidgets.QLabel('Property View')
        property_view = PropertyView(controller, 'properties')
        property_view_layout.addWidget(property_view_label)
        property_view_layout.addWidget(property_view.get_widget())
        application_layout.addLayout(property_view_layout)

        controller.add_view(status_view)
        controller.add_view(property_view)

        window.setWindowTitle('MVC Example')


        window.show()

        sys.exit(app.exec_())


if __name__ == '__main__':
    qt_application = QtShotApplication()
