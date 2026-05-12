perfil = {
    "nome": input("Seu nome: "),
    "idade": int(input("Sua idade: ")),
    "cidade": input("Sua cidade: "),
    "linguagem_favorita": "Python"
}

print("\n=== SEU PERFIL ===")
for chave, valor in perfil.items():
    chave_formatada = chave.replace("_", " ").capitalize()#replace substitui os _ por espaço e capitalize deixa a primeira letra maiúscula
    print(f"  {chave_formatada}: {valor}")

# Verificando e consultando com .get()
telefone = perfil.get("telefone", "não informado")
print(f"\nTelefone: {telefone}")