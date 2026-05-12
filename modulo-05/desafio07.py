perguntas = [

    {
        "pergunta": "Qual linguagem estamos aprendendo?",
        "opcoes": ["A) Java", "B) Python", "C) C++", "D) PHP"],
        "resposta": "B"
    },

    {
        "pergunta": "Qual estrutura guarda vários valores?",
        "opcoes": ["A) if", "B) print", "C) lista", "D) input"],
        "resposta": "C"
    },

    {
        "pergunta": "Qual comando usamos para mostrar algo na tela?",
        "opcoes": ["A) input()", "B) print()", "C) len()", "D) append()"],
        "resposta": "B"
    }
]
print("=== QUIZ DE PROGRAMAÇÃO ===\n")
for i, pergunta in enumerate(perguntas):
    print(f"Pergunta {i + 1}: {pergunta['pergunta']}")
    for opcao in pergunta["opcoes"]:
        print(opcao)
    resposta_usuario = input("Sua resposta (A, B, C ou D): ").upper()
    if resposta_usuario == pergunta["resposta"]:
        print("✅ Resposta correta!\n")
    else:
        print(f"❌ Resposta incorreta. A resposta correta é: {pergunta['resposta']}\n")