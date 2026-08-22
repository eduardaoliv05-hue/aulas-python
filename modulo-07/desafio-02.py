from datetime import date

contatos = [
    {"nome": "Ana", "nascimento": date(1995, 6, 15)},
    {"nome": "Bruno", "nascimento": date(1990, 3, 4)},
    {"nome": "Carlos", "nascimento": date(1988, 12, 25)},
]

hoje = date.today()

print("=== ANIVERSÁRIOS ===")
for c in contatos:
    anos = hoje.year - c["nascimento"].year
    aniversario_este_ano = c["nascimento"].replace(year=hoje.year)
    
    if aniversario_este_ano == hoje:
        status = "🎂 HOJE!"
    elif aniversario_este_ano > hoje:
        dias = (aniversario_este_ano - hoje).days
        status = f"em {dias} dias"
    else:
        status = "já passou este ano"
    
    print(f"{c['nome']}: {anos} anos — {status}")