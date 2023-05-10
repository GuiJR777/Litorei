def validar_tipo_do_parametro(tipo):
    def decorator(funcao):
        def wrapper(self, *args, **kwargs):
            for arg in args:
                if not isinstance(arg, tipo):
                    raise TypeError(f"O tipo do argumento {arg} é inválido")
            return funcao(self, *args, **kwargs)

        return wrapper

    return decorator
