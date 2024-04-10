# Verifica se um numero é primo utilizando o metodo de Fermat
def primo(n):
	if n == 1:
		return False
	if (n == 2) or (n == 3):
		return True
	if (n % 2 == 0) or (n % 3 == 0):
		return False
	i = 5
	while i*i <= n:
		if (n % i == 0) or (n % (i+2) == 0):
			return False
		i += 6
	return True

# Busca os 2 numeros primos anteriores mais proximos de determinado numero
def antecessores(n):
	n -= 1
	primos = []
	while len(primos) < 2 and n > 1:
		if primo(n):
			primos.append(n)
		n -= 1
	return primos

# Busca os 2 numeros primos sucessores mais proximos de determinado numero
def sucessores(n):
	n += 1
	primos = []
	while len(primos) < 2:
		if primo(n):
			primos.append(n)
		n += 1
	return primos


n = int(input("Informe um número inteiro: "))
print(f" O {n} é um número primo? {primo(n)}")
if primo(n):
    print(f"Seus primos antecessores são: {antecessores(n)}")
    print(f"Seus primos sucessores são: {sucessores(n)}")
