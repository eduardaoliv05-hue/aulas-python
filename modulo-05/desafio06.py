contatos = []
while True:
    print("=== MENU DE OPÇOES ===")
    print("1. Adicionar contato")
    print("2. Buscar contato")
    print("3. Listar por grupo")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        nome = input("Nome do contato: ")
        telefone = input("Telefone do contato: ")
        grupo = input("Grupo do contato (ex: família, amigos, trabalho): ")
        contatos.append({"nome": nome, "telefone": telefone, "grupo": grupo})
    elif opcao == "2":
        busca = input("Digite o nome do contato: ")
        for contato in contatos:
            if contato["nome"].lower() == busca.lower():
                print(f"Contato encontrado: {contato['nome']} - {contato['telefone']} (Grupo: {contato['grupo']})")
                break
        else:
            print("Contato não encontrado.")
    elif opcao == "3":
        grupo_busca = input("Digite o nome do grupo: ")
        print(f"Contatos no grupo '{grupo_busca}':")
        for contato in contatos:
            if contato["grupo"].lower() == grupo_busca.lower():
                print(f"{contato['nome']} - {contato['telefone']}")
    elif opcao == "4":
        print("Encerrando o programa")
        break
    else:
        print("Opção inválida. Tente novamente.")