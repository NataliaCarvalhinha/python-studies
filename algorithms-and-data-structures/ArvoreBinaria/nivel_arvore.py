from cria_arvore import arvore

# Encontra em qual nivel determinado elemento esta em qualquer arvore
def encontraNivel(arvore, numero, nivelAtual = 0):
	nivelAtual += 1
	if arvore == None:
		return -1
	if arvore['valor'] == numero:
		return nivelAtual

	resultEsq = encontraNivel(arvore['esq'], numero, nivelAtual)
	if resultEsq != -1:
		return resultEsq
	return encontraNivel(arvore['dir'], numero, nivelAtual)

''' 
Arvore de teste:

Nivel 1			 A
		       /   \
		      /     \
Nivel 2		 B       C
    		/      /   \
Nivel 3	   D      E     F
	       	\	 / \
Nivel 4	   	 G  H   I


Resultados esperados:

H - Nivel 4
L - Não está na lista (-1)
D - Nivel 3

'''
print(encontraNivel(arvore, 'H'))
print(encontraNivel(arvore, 'L'))
print(encontraNivel(arvore, 'D'))