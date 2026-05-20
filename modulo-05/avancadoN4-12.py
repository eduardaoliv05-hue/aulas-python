agenda = [
    {"nome": "Ana Lima",     "tel": "11999990001", "grupos": ["Trabalho", "Amigos"]},
    {"nome": "Bruno Costa",  "tel": "11999990002", "grupos": ["Família"]},
    {"nome": "Carlos Melo",  "tel": "11999990003", "grupos": ["Trabalho"]},
    {"nome": "Diana Torres", "tel": "11999990004", "grupos": ["Amigos", "Família"]},
    {"nome": "Elena Souza",  "tel": "11999990005", "grupos": ["Trabalho", "Amigos"]},
]
print("===MENU DE OPÇÕES===")
print("1 - Adicionar nome, telefone e grupos de cada contato")
print("2 - Buscar contato por nome (parcial)")
print("3 - Listar todos os contatos de um grupo")
print("4 - Mostrar todos os grupos existentes")
opcao = input("Escolha uma opção: ")
if opcao == "1":
    nome = input("Nome do contato: ")
    tel = input("Telefone do contato: ")
    grupos = input("Grupos (separados por vírgula): ").split(",")
    agenda.append({"nome": nome, "tel": tel, "grupos": [g.strip() for g in grupos]})
elif opcao == "2":
    nome = input("Nome do contato: ").lower()
    for contato in agenda:
        if nome in contato["nome"].lower():
            print(f"Nome: {contato['nome']} | Telefone: {contato['tel']} | Grupos: {', '.join(contato['grupos'])}")
            break
    else:
        print("Contato não encontrado.")
elif opcao == "3":
    grupo = input("Nome do grupo: ")
    print(f"Contatos no grupo {grupo}:")
    for contato in agenda:
        if grupo in contato["grupos"]:
            print(f"  - {contato['nome']} ({contato['tel']})")
elif opcao == "4":
    grupos_unicos = set()
    for contato in agenda:
        grupos_unicos.update(contato["grupos"])
    print("Grupos existentes:")
    for g in sorted(grupos_unicos):
        print(f"  - {g}")
else:
    print("Opção inválida.")