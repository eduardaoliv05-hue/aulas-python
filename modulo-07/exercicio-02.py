linha = "Produto A,15.90,100,true"
campos = linha.split(",") #.split separa a string em uma lista de campos usando a vírgula como delimitador

nome = campos[0]
preco = float(campos[1])
estoque = int(campos[2])
ativo = campos[3].lower() == "true"

print(f"Produto: {nome}")
print(f"Preço: R$ {preco:.2f}")
print(f"Estoque: {estoque} unidades")
print(f"Ativo: {ativo}")