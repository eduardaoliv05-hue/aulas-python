
def contar_palavras():
    try:
        with open("texto.txt", "r", encoding="utf-8") as arquivo:
            texto = arquivo.read()

        palavras = texto.lower().split()

        contador = {}

        for palavra in palavras:
            contador[palavra] = contador.get(palavra, 0) + 1

        ranking = sorted(
            contador.items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]

        print("\n=== TOP 10 PALAVRAS ===")

        for posicao, (palavra, quantidade) in enumerate(ranking, start=1):
            print(f"{posicao}. {palavra:<12}: {quantidade}x")

        print(f"\nTotal de palavras: {len(palavras):,}".replace(",", "."))
        print(f"Palavras únicas: {len(contador)}")

    except FileNotFoundError:
        print("Arquivo não encontrado!")


contar_palavras()
