def validar_tipo_do_parametro(tipo):
    def decorador(funcao):
        def wrapper(*args, **kwargs):
            if all([isinstance(arg, tipo) for arg in args]):
                return funcao(*args, **kwargs)
            raise TypeError(f"Os parâmetros devem ser do tipo {tipo.__name__}")

        return wrapper

    return decorador
