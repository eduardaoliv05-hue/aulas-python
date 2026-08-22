def validar_senha(senha):
    erros = []
    
    if len(senha) < 8:
        erros.append("Mínimo 8 caracteres")
    
    if not any(c.isdigit() for c in senha):
        erros.append("Precisa ter pelo menos 1 número")
    
    if not any(c.isupper() for c in senha):
        erros.append("Precisa ter pelo menos 1 maiúscula")
    
    return erros

while True:
    senha = input("Crie uma senha: ")
    erros = validar_senha(senha)

    if not erros:
        print("✅ Senha válida!")
        break
    else:
        print("Senha inválida:")
        for erro in erros:
            print(f"  - {erro}")
