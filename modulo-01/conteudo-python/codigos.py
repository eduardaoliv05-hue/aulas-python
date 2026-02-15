# region - if e else
clima = 30
if clima <= 19:
 print("clima legal")
else:
 print("clima nao tao legal")
# endregion

# region - input (para escrever enquanto o codigo roda)
nome = (input("digite seu nome: "))
print (f"bom dia {nome} :)")
# endregion

# region - .append (adicionar coisas a uma lista)
lista = ["gato", "cachorro", "coelho"]
print(lista)
lista.append("cavalo")
print(lista)
# endregion

# region - tipos de loops
#range roda o loop dentro de um raio, for cria uma condição ao loop
for n in range(1, 11):
  print(f"this is a loop {n}")

# while roda o loop enquanto ele for true, while true roda o loop infinitamente
contador = 0
while contador <=10:
    print(contador)
    contador +=1


# region - isalpha(): = identifica se todos os caracteres sao letras
texto = "abc123"
for c in texto:
    if c.isalpha():
     print(c, "é letra")
# endregion