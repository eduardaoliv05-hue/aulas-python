n = int(input("Somar de 1 até qual número? "))  #somar ate 12
total = 0

for i in range(1, n + 1): #de 1 a n(12) +1, ou seja, de 1 a 13
    total += i 

print(f"Soma de 1 a {n} = {total}")