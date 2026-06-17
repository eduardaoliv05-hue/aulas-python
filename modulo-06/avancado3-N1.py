def linha(tamanho=40, caractere="-"):
    print(caractere * tamanho)
def calcular_total(dados):
    return sum(dados.values())
def gerar_relatorio(titulo, dados):
    linha()
    print(titulo.center(40))
    linha()
    for chave, valor in dados.items(): print(f"{chave}: {valor}")
    linha()
    print(f"Total: {calcular_total(dados)}")
titulo = input("Digite o título do relatório: ")
dados = {}
while True:
    chave = input("Digite a chave (ou 'sair' para finalizar): ")
    if chave.lower() == "sair": break
    valor = float(input("Digite o valor: "))
    dados[chave] = valor
gerar_relatorio(titulo, dados)

	
		