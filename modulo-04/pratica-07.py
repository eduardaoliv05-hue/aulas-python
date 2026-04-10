n= int(input("quantos numeros na sequencia de Fibonacci? "))#5
a, b= 0, 1
print("Sequência de Fibonacci:")
for i in range(n):
    print(a, end=" ") #0\1\1
    a, b = b, a + b #a =1, b= 0+1 = 1\a=1, b= 1+1 = 2\a=2\b= 1+2 = 3\a=3\b= 2+3 = 5
print()