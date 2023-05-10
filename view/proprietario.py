from view.abstract_view import View


class ProprietarioView(View):
    def __init__(self, screen_manager) -> None:
        self.screen_manager = screen_manager
