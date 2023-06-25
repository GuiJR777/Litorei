from abc import ABC, abstractmethod

from flet import Banner, colors, Icon, icons, Text, TextButton, View

from utils.decorators import validar_tipo_do_parametro


class Page(ABC, View):
    def __init__(self, route: str) -> None:
        super().__init__(route)
        self.__payload = {}
        self.__data = {}

    @property
    def payload(self) -> dict:
        return self.__payload

    @payload.setter
    @validar_tipo_do_parametro(dict)
    def payload(self, payload: dict) -> None:
        self.__payload = payload

    @property
    def data(self) -> dict:
        return self.__data

    @data.setter
    def data(self, data: dict) -> None:
        self.__data = data

    @abstractmethod
    def exibir_pagina(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def preencher_payload(self, event, *args, **kwargs) -> None:
        pass

    def start_alert_banner(self, message: str) -> None:
        return Banner(
            bgcolor=colors.RED_400,
            leading=Icon(
                icons.WARNING_AMBER_ROUNDED, color=colors.WHITE, size=40
            ),
            content=Text(
                message,
            ),
            actions=[
                TextButton("Ok"),
            ],
        )

    def start_success_banner(self, message: str) -> None:
        return Banner(
            bgcolor=colors.GREEN_ACCENT_700,
            leading=Icon(icons.CHECK, color=colors.WHITE, size=40),
            content=Text(
                message,
            ),
            actions=[
                TextButton("Ok"),
            ],
        )
