from model_view_controller.business_entities.shot import Shot
from model_view_controller.business_entities.task import Task


class ListShotUseCase(object):

    @staticmethod
    def execute():
        task_a = Task()
        task_a.name = 'first task'

        task_b = Task()
        task_b.name = 'task of something'

        task_c = Task()
        task_c.name = 'cleaning task'

        list_of_entities = list()

        shot_a = Shot()
        shot_a.status = 'need vacations'
        shot_a.tasks.append(task_a)
        shot_a.tasks.append(task_b)

        shot_b = Shot()
        shot_b.title = 'test 2'
        shot_b.description = 'this shot is top notch'
        shot_b.tasks.append(task_b)
        shot_b.tasks.append(task_c)

        list_of_entities.append(shot_a)
        list_of_entities.append(shot_b)

        return list_of_entities
