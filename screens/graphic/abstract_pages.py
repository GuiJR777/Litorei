from abc import ABC, abstractmethod

from flet import Banner, colors, Icon, icons, Text, TextButton, View

from utils.decorators import validar_tipo_do_parametro


class Page(ABC, View):
    def __init__(self, route: str) -> None:
        super().__init__(route)
        self.__payload = {}

    @property
    def payload(self) -> dict:
        return self.__payload

    @payload.setter
    @validar_tipo_do_parametro(dict)
    def payload(self, payload: dict) -> None:
        self.__payload = payload

    @abstractmethod
    def exibir_pagina(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def preencher_payload(self, event, *args, **kwargs) -> None:
        pass

    def start_alert_banner(self, message: str) -> None:
        return Banner(
            bgcolor=colors.AMBER_100,
            leading=Icon(icons.WARNING_AMBER_ROUNDED, color=colors.AMBER, size=40),
            content=Text(
                message,
            ),
            actions=[
                TextButton("Ok"),
            ],
        )

    def start_success_banner(self, message: str) -> None:
        return Banner(
            bgcolor=colors.LIGHT_GREEN_ACCENT_200,
            leading=Icon(icons.DONE_OUTLINE, color=colors.GREEN, size=40),
            content=Text(
                message,
            ),
            actions=[
                TextButton("Ok"),
            ],
        )
