print("=== CRIAR CONTA ===")
usuario = input("Crie seu usuário: ")
senha = input("Crie sua senha: ")
print("Agora faça login.\n")

tentativas = 3
while tentativas > 0:
    try:

        login_usuario = input("Usuário: ")
        login_senha = input("Senha: ")
        if login_usuario == usuario and login_senha == senha:
                print("\nLogin realizado com sucesso!")
                break
        else:
                tentativas -= 1
                print(f"\nUsuário ou senha incorretos!")
                print(f"Você ainda tem {tentativas} tentativa(s).\n")
    except:
        print("Ocorreu um erro. Tente novamente.")
if tentativas == 0:
    print("Conta bloqueada por excesso de tentativas.")