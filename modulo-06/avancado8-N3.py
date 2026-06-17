pedidos_feitos = {}

def cardapio():
    print("CARDÁPIO")
    print("1. X-Burguer   R$ 25.00\n2. Pizza       R$ 45.00\n3. Sal. Caesar R$ 30.00")

def pedidos():
    pedido = int(input("Digite o número do prato que deseja pedir: "))
    quantidade = int(input("Digite a quantidade: "))
    if pedido == 1:
        pedidos_feitos[("X-Burguer", 25.00)] = quantidade
    elif pedido == 2:
        pedidos_feitos[("Pizza", 45.00)] = quantidade
    elif pedido == 3:
        pedidos_feitos[("Salada Caesar", 30.00)] = quantidade
    else:
        print("Prato inválido.")
    return pedidos_feitos

def conta():
    total = sum(item[0][1] * item[1] for item in pedidos_feitos.items())
    print("--- SUA CONTA ---")
    for item in pedidos_feitos.items():
        print(f"{item[0][0]} x{item[1]} - R$ {item[0][1] * item[1]:.2f}")
    print(f"Total: R$ {total:.2f}")

def mostrar_menu():
    print("====== RESTAURANTE KEI ======")
    print("1. Ver cardápio\n2. Fazer pedido\n3. Ver conta\n0. Sair")
    opcao = int(input("opcao: "))
    if opcao == 1:
        cardapio()
    elif opcao == 2:
        pedidos()
    elif opcao == 3:
        conta()
    elif opcao == 0:
        print("Obrigado por visitar o Restaurante Kei! Volte sempre!")
    else:
        print("opção inválida.")

while True:
    mostrar_menu()

