class AbstractView(object):
    def __init__(self, controller):
        self._controller = controller

    def update_view(self, data):
        raise NotImplementedError

