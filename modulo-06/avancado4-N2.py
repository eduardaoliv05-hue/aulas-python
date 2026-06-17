def resumo_pedido(*itens, **opcoes):
    mesa = opcoes.get("mesa")
    desconto = opcoes.get("desconto")

    print(f"=== PEDIDO (Mesa {mesa}) ===")

    for item in itens:
        print(f"- {item}")

    print(f"Subtotal: {len(itens)} itens")
    print(f"Desconto: {desconto}%")

resumo_pedido("Hambúrguer", "Batata Frita", "Refrigerante", mesa=5, desconto=10)
