# Calcula o fatorial de um numero utilizando loop
def fatorialLoop(n):
	f = n

	while n > 1:
		n = n - 1
		f = f * n

	return f

# Calcula o fatorial de um número utilizando recursao
def fatorialRecursivo(n):

	if n == 1:
		return 1

	return n * fatorialRecursivo(n-1)


# Testes dos métodos

print(fatorialLoop(3))
print(fatorialRecursivo(3))