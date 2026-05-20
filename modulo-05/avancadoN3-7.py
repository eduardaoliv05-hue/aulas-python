texto = "python é incrivel python é poderoso python facilita tudo python"


contagem = {}
for palavra in texto.split():#split() divide o texto em palavras usando espaço como separador
    if palavra in contagem:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    else:
        contagem[palavra] = 1

for palavra, qtd in sorted(contagem.items(), key=lambda x: x[1], reverse=True):
    print(f"  {palavra:<10}:({qtd})")