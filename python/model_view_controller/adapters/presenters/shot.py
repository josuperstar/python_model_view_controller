from model_view_controller.business_entities.shot import Shot


class ShotPresenter(Shot):
    def __init__(self):
        super(ShotPresenter, self).__init__()
        self.title_color = 'red'
