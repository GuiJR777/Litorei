from view.abstract_view import View


class ImovelView(View):
    def __init__(self, screen_manager) -> None:
        self.screen_manager = screen_manager
