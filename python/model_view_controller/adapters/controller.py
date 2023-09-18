from model_view_controller.adapters.presenters.shot import Shot
from model_view_controller.adapters.presenters.task import Task


class Controller(object):
    def __init__(self):
        self._views = list()

    def add_view(self, view):
        self._views.append(view)

    @staticmethod
    def get_list_of_shot():

        # Method that mocks a list of shot and tasks and return it
        # Typically, this could come from a use case class, but it's out of the scope of this example

        task_a = Task()
        task_a.task_color = 'pink'

        task_b = Task()
        task_b.name = 'task of something'

        task_c = Task()
        task_c.name = 'cleaning task'

        list_of_presenters = list()

        shot_a = Shot()
        shot_a.status = 'need vacations'
        shot_a.tasks.append(task_a)
        shot_a.tasks.append(task_b)

        shot_b = Shot()
        shot_b.title = 'test 2'
        shot_b.title_color = 'green'
        shot_b.description = 'this shot is top notch'
        shot_b.tasks.append(task_b)
        shot_b.tasks.append(task_c)

        list_of_presenters.append(shot_a)
        list_of_presenters.append(shot_b)

        return list_of_presenters

    def raise_selection_change(self, selection):
        for view in self._views:
            view.update_view(selection)
