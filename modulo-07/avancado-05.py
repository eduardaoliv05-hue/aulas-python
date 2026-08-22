def formatar_cpf(cpf):
    if len(cpf) != 11:
        return "CPF inválido, deve conter 11 dígitos."
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
def formatar_tel(tel):
    if len(tel) < 10:
        return "Número de telefone inválido"
    elif len(tel) == 10:
        return f"({tel[:2]}) {tel[2:6]}-{tel[6:]}"
    elif len(tel) == 11:
        return f"({tel[:2]}) {tel[2:7]}-{tel[7:]}"
    else:
        return "Número de telefone inválido"
