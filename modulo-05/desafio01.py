compras =[]
print("==== MENU DE OPCOES ====")
print("1 - Adicionar item")
print("2 - Remover item")
print("3 - Listar itens")
print("4 - Sair")
opcao = int(input("escolha uma opção: "))
while opcao != 4:
    if opcao == 1:
        item = input("Digite o nome do item: ")
        compras.append(item)
        print(f"{item} adicionado à lista de compras.")
    elif opcao == 2:
        item = input("Digite o nome do item a remover: ")
        if item in compras:
            compras.remove(item)
            print(f"{item} removido da lista de compras.")
        else:
            print(f"{item} não encontrado na lista de compras.")
    elif opcao == 3:
        print("Itens na lista de compras:")
        for i, item in enumerate(compras, start=1):#start=1 para começar a contagem do índice a partir de 1
            print(f"{i}. {item}")
    else:
        print("Opção inválida. Tente novamente.")
    
    print("\n==== MENU DE OPCOES ====")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Listar itens")
    print("4 - Sair")
    opcao = int(input("escolha uma opção: "))