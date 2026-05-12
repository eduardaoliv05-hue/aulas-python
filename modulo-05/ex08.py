# Conte quantas vezes cada letra aparece em uma palavra
palavra = input("Digite uma palavra: ").lower() 

contagem = {}#{letra: vezes}
for letra in palavra:#bola - b
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1

# Exibir em ordem de frequência (mais comum primeiro)
print(f"\nLetras em '{palavra}':")
for letra, qtd in sorted(contagem.items(), key=lambda x: x[1], reverse=True):#key=lambda x: x[1] ordena pelo valor (quantidade) e reverse=True para ordem decrescente
    barra = "█" * qtd
    print(f"  '{letra}': {barra} ({qtd})")