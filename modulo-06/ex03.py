def exibir_menu():
    print("=== Cardapio ===")
    print("1. lanches")
    print("2. bebidas")
    print("3. sair")
def exibir_lanches():
    lanches = ["X-Burguer (R$15)", "X-Salada (R$18)", "Veggie (R$14)"]
    for i, lanche in enumerate(lanches, 1):
        print(f"{i}. {lanche}")
def exibir_bebidas():
	bebidas = ["Coca (R$5)", "Suco (R$7)", "Agua (R$3)"]
	for i, bebida in enumerate(bebidas, 1):
		print(f" {i} . {bebida}")
            
while True:
	exibir_menu()
	opcao = input(" opcao: ")
	if opcao == "1" : exibir_lanches()
	elif opcao == "2" : exibir_bebidas()
	elif opcao == "0" : break
	else: print ("opcao invalida")