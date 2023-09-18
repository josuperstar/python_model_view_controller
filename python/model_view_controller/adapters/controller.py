
from model_view_controller.use_case.list_shot_use_case import ListShotUseCase
from model_view_controller.adapters.presenters.shot import ShotPresenter
from model_view_controller.adapters.presenters.task import TaskPresenter


class Controller(object):
    def __init__(self):
        self._views = list()

    def add_view(self, view):
        self._views.append(view)

    def get_list_of_shot(self):

        list_of_presenters = list()
        list_shots = ListShotUseCase()
        list_of_business_entities = list_shots.execute()

        for entity in list_of_business_entities:
            shot_presenter = self.shot_presenter_convesrion(entity)
            list_of_presenters.append(shot_presenter)

        return list_of_presenters

    def shot_presenter_convesrion(self, shot):
        shot_presenter = ShotPresenter()
        shot_presenter.title = shot.title
        shot_tasks = shot.tasks
        task_presenter_list = list()
        for task in shot_tasks:
            task_presenter = self.task_presenter_conversion(task)
            task_presenter_list.append(task_presenter)
            print("{} - {}".format(task.name, task_presenter.name))
        shot_presenter.tasks = task_presenter_list
        shot_presenter.status = shot.status
        shot_presenter.description = shot.description
        shot_presenter.title_color = 'green'
        return shot_presenter

    @staticmethod
    def task_presenter_conversion(entity):
        task_presenter = TaskPresenter()
        task_presenter.name = entity.name
        task_presenter.status = entity.status
        if entity.status != 'all good':
            task_presenter.task_color = 'red'
        else:
            task_presenter.task_color = 'green'
        task_presenter.description = entity.description
        return task_presenter

    def raise_selection_change(self, view_caller, selection):
        for view in self._views:
            if view.name != view_caller.name:
                view.update_view(selection)
