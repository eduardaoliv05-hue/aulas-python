usuarios = []
nomes = set()
emails = set()
while True:
    print("=== CADASTRO DE USUÁRIOS ===")
    print("1. Mostrar usuários cadastrados")
    print("2. Cadastrar novo usuário")
    print("3. Sair\n\n")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        print("Usuários cadastrados:")
        for usuario in usuarios:
            print(f" - {usuario['nome']} - {usuario['email']}")
    elif opcao == "2":
        while True:
            nome = input("Digite um usuário: ")
            if nome in nomes:
                print("❌ Usuário já existe.")
            else:
                nomes.add(nome)
                print("✅ Usuário cadastrado.")
                break
        while True:
            email = input("Digite o email do usuário: ")
            if email in emails:
                print("❌ Email já cadastrado.")
            else:
                usuarios.append({'nome': nome, 'email': email})
                emails.add(email)
                print("✅ Email cadastrado.")
                break
        
    elif opcao == "3":
        print("Encerrando o programa")
        break
    else:
        print("Opção inválida. Tente novamente.")