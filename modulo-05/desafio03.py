palavra = input("Digite uma palavra: ").lower() 

contagem = {}
for letra in palavra:
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1

print(f"\nLetras em '{palavra}':")
for letra, qtd in sorted(contagem.items(), key=lambda x: x[1], reverse=True):
    barra = "█" * qtd
    print(f"  '{letra}': {barra} ({qtd})")