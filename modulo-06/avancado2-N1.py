def validar_senha(senha):
    if len(senha) < 8:
        return print("pelo menos 8 caracteres.")
    if not any(c.isupper() for c in senha):
        return print("pelo menos uma letra maiúscula.")
    if not any(c in "!@#$%" for c in senha):
        return print("pelo menos um caractere especial.")
    if not any(c.isdigit() for c in senha):
        return print("pelo menos um dígito.")
    return print("senha válida.")
senha = input("Digite a senha: ")
validar_senha(senha)
