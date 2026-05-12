produtos = []
while True:
    print("=== MENU DE OPÇOES ===")
    print("1. Cadastrar produtos")
    print("2. Registrar venda")
    print("3. relatorio de estoque")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        quantidade = int(input("Quantos produtos vou cadastrar? "))
        for i in range(quantidade):
            nome = input(f"Nome do produto {i + 1}: ")
            qtd = int(input(f"Quantidade do produto {i + 1}: "))
            preco = float(input(f"Preço do produto {i + 1}: "))
            produtos.append({"nome": nome, "qtd": qtd, "preco": preco})
    elif opcao == "2":
        venda = input("Nome do produto vendido: ")
        qtd_venda = int(input("Quantidade vendida: "))
        for produto in produtos:
            if produto["nome"].lower() == venda.lower():
                if produto["qtd"] >= qtd_venda:
                    produto["qtd"] -= qtd_venda
                    print(f"Venda registrada: {qtd_venda} un. de {produto['nome']}")
                else:
                    print(f"Estoque insuficiente para {produto['nome']}. Disponível: {produto['qtd']} un.")
                break
        else:
            print("Produto não encontrado.")

    elif opcao == "3":
        print("=== RELATÓRIO DE ESTOQUE ===\n")
        valor_total = 0

        for produto in produtos:
            valor = produto["preco"] * produto["qtd"]
            valor_total += valor
            status = "⚠️ ESGOTADO" if produto["qtd"] == 0 else f"{produto['qtd']} un."
            print(f"{produto['nome']:<12} R${produto['preco']:>6.2f}  {status:<12}  Valor: R${valor:>8.2f}")

        print(f"\n{'─'*55}")
        print(f"Valor total em estoque: R$ {valor_total:.2f}")
        print(f"Produtos disponíveis: {len([p for p in produtos if p['qtd'] > 0])}/{len(produtos)}")
        print(f"Produto mais caro: {max(produtos, key=lambda p: p['preco'])['nome']}")
        print(f"Produto mais barato: {min(produtos, key=lambda p: p['preco'])['nome']}")
    elif opcao == "4":
        print("Encerrando o programa")
        break
    else:
        print("Opção inválida. Tente novamente.")