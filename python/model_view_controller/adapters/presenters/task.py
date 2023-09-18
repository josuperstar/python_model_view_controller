from model_view_controller.business_entities.task import Task

class TaskPresenter(Task):

    def __init__(self):
        super(TaskPresenter, self).__init__()
        self.task_color = 'blue'

