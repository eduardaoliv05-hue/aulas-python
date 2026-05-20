dados = [" Python ", " java ", " JAVASCRIPT ", " rust ", " go "]

pipeline = [
    ("strip", lambda x: x.strip()),#lambda é uma função anônima, ou seja, uma função sem nome, que pode ser usada para criar funções simples e rápidas. Nesse caso, a função lambda recebe um argumento x e retorna o resultado de x.strip(), que remove os espaços em branco no início e no final da string.
    ("lowercase", lambda x: x.lower()),
    ("capitalize", lambda x: x.capitalize()),
    ("filtrar >3", lambda x: len(x) > 3)
]

for i, (nome, funcao) in enumerate(pipeline, start=1):
    novo_resultado = []
    for item in dados:
        resultado = funcao(item)
        if isinstance(resultado, bool):#isinstance verifica se o resultado é um booleano, ou seja, se é uma condição de filtragem
            if resultado:
                novo_resultado.append(item)
        else:
            novo_resultado.append(resultado)
    dados = novo_resultado
    print(f"\n[ETAPA {i} - {nome}]")
    print(dados)
print("\nResultado final:")
print(dados)