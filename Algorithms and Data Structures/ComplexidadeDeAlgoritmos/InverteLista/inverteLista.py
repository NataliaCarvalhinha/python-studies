# Dada uma lista retorna inverte as posições dos itens
def inverteList(lista):
	n = len(lista)

	for i in range(n//2):
		aux = lista[i]
		lista[i] = lista[n-i-1]
		lista[n-i-1] = aux

lista = [0,1,2,3,4]
print(lista)
inverteList(lista)
print(lista)