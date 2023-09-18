class Controller(object):
    def __init__(self):
        self._views = list()

    def add_view(self, view):
        self._views.append(view)

    def raise_selection_change(self, selection):
        for view in self._views:
            view.update_view(selection)
