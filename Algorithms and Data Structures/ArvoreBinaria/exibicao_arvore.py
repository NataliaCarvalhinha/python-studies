from cria_arvore import arvore

# Exibe cada no da arvore informando os filhos
def printNiveis(raiz):
	if raiz == None:
		return
	esq = raiz['esq']
	if esq != None:
		esq = raiz['esq']['valor']

	dirNo = raiz['dir']
	if dirNo != None:
		dirNo = raiz['dir']['valor']

	print(f'{esq} <- {raiz["valor"]} -> {dirNo}')
	printNiveis(raiz['esq'])
	printNiveis(raiz['dir'])

'''
Arvore de teste:
			 A
		   /   \
		  /     \
		 B       C
		/      /   \
	   D      E     F
	   	\	 / \
	   	 G  H   I


Resultado esperado:

	B <- A -> C
	D <- B -> None
	None <- D -> G
	None <- G -> None
	E <- C -> F
	H <- E -> I
	None <- H -> None
	None <- I -> None
	None <- F -> None
'''

printNiveis(arvore)