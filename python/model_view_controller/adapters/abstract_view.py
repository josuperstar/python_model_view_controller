class AbstractView(object):
    def __init__(self, controller, name):
        self._name = name
        self._controller = controller

    def update_view(self, data):
        raise NotImplementedError

    @property
    def name(self):
        return self._name

