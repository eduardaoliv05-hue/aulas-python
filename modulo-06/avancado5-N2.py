def fatorial(fa):
	if fa == 0: return 1
	return fa * fatorial(fa-1)

def fibonacci(fib):
	if fib <= 1: return fib
	return fibonacci(fib-1) + fibonacci(fib-2)
def soma_digitos(soma):
	if soma < 10:
		return soma
	return soma % 10 + soma_digitos(soma // 10)
def resultado(fa, fib, soma):
	print(f"Fatorial ({fa}): {fatorial(fa)}")
	print(f"Fibonacci ({fib}): {fibonacci(fib)}")
	print(f"Soma dos dígitos ({soma}): {soma_digitos(soma)}")
resultado(5, 8, 9875)