# -*- coding: utf-8 -*-

name = "python_model_view_controller"

version = "0.1.0"

description = "Generic Publisher User Interface"

requires = [
    "PySide2-5.12+",
    "python-2+<4",
]


def commands():
    env.PYTHONPATH.append("{root}/python")


tests = {

    "test_views": {
        "command": "python {root}/tests/unit_tests/test_views.py",
        "requires": ['houdini'],
    },

}
