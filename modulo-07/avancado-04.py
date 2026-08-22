def analise_texto(texto):
    palavras = texto.split()
    num_caracteres = len(texto)
    print(f"Número de caracteres (com espaços): {num_caracteres}")
    num_caracteres_sem_espacos = len(texto.replace(" ", ""))
    print(f"Número de caracteres (sem espaços): {num_caracteres_sem_espacos}")
    num_palavras = len(palavras)
    print(f"Número de palavras: {num_palavras}")
    linhas = texto.splitlines()
    print(f"Número de linhas: {len(linhas)}")
    palavra_longa = max(palavras, key=len)
    print(f"Palavra mais longa: {palavra_longa}")
    palavra_frequente = max(set(palavras), key=palavras.count)
    repeticoes = palavras.count(palavra_frequente)
    print(f"Palavra mais frequente: {palavra_frequente} {repeticoes}x")


texto = input("entre com o texto: ")
analise_texto(texto)





