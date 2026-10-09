usuarios = {
    "admin": "admin123"
}

tentativas = 3

while tentativas > 0:

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    try:
        senha_correta = usuarios[usuario]

        if senha == senha_correta:
            print(f"Bem-vindo, {usuario}! Acesso concedido.")
            break
        else:
            tentativas -= 1

            if tentativas > 0:
                print(f"Senha incorreta. Tentativas restantes: {tentativas}")
            else:
                print("Acesso bloqueado! Máximo de tentativas atingido.")

    except KeyError:
        print("Usuário não encontrado.")