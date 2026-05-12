cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Salvador", "Fortaleza"]

print(f"Total de cidades: {len(cidades)}")
print(f"Primeira: {cidades[0]}")
print(f"Última: {cidades[-1]}")
print(f"Duas primeiras: {cidades[:2]}")

for i, cidade in enumerate(cidades, 1): #verifica todas as cidades na lista
    if cidade.startswith("S"):
        print(f"  {i}. {cidade}")