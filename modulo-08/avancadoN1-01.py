def converter_numero(valor):
    try:
        if isinstance(valor, str):
            valor = valor.replace(",", ".")
        return float(valor)
    except ValueError:
        print(f"avis: '{valor}' não é um número válido")
        return None
    except TypeError:
        print(f"avis: tipo inválido: {type(valor).__name__}")
        return None
print(converter_numero("42"))
print(converter_numero("3.14"))
print(converter_numero("abc"))
print(converter_numero(None))
print(converter_numero("1,5"))