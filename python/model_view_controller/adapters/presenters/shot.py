from model_view_controller.adapters.presenters.task import Task

class Shot(object):
    def __init__(self):
        self.status = 'all good'
        self.title = 'test'
        self.title_color = 'red'
        self.description = 'blablabla'

        self.tasks = list()
