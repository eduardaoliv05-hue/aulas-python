usuario = input("Digite o nome do usuário: ")
senha = input("Digite a senha: ")
if usuario == "admin" and senha == "1234":
    print("Acesso concedido.")
else:
    print("usuario ou senha invalidos.")