documentos = {
    "doc1": "python é uma linguagem poderosa e versátil",
    "doc2": "python é usada em ciência de dados e IA",
    "doc3": "javascript é a linguagem da web moderna",
    "doc4": "python e javascript são linguagens populares",
}
indice = {}
for nome_doc, texto in documentos.items():
    palavras = texto.split()
    for palavra in palavras:
        indice.setdefault(palavra, set()).add(nome_doc) #setdefault é um método de dicionário que retorna o valor associado a uma chave, se a chave não existir, ele define a chave com um valor padrão (neste caso, um conjunto vazio) e retorna esse valor.
busca = input("Digite a palavra para buscar: ")
resultado = indice.get(busca, set())
print(f"\n{busca} -> {resultado}")
