# Ordena a lista pelo método insertion sorte utilizando loop
def insert_sort(lista):
	for i in range(1, len(lista)):
		for j in range(i - 1, -1, -1):
			if lista[j + 1] < lista[j]:
				lista[j + 1], lista[j] = lista[j], lista[j + 1]
			else:
				break
	return lista


# Ordena a lista pelo método insertion sorte utilizando recursão
def insert_sort_recursao(lista, i, j):
	if i >= len(lista):
		return

	if j < 0:
		insert_sort_recursao(lista, i + 1, i)
		return

	if lista[j + 1] < lista[j]:
		lista[j + 1], lista[j] = lista[j], lista[j + 1]
	
	insert_sort_recursao(lista, i, j - 1)

# Facilita chamada do método recursivo inserindo valores iniciais de navegação
def insert_sort2(lista):
	insert_sort_recursao(lista, 1, 0)

# Testes dos métodos

lista1 = [5, 2, 4, 6, 1, 3]
print(insert_sort(lista1))

lista2 = [5, 2, 4, 6, 1, 3]
insert_sort2(lista2)
print(lista2)
