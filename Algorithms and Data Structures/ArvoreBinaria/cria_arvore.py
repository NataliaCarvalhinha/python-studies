# Cria um no de arvore
def criaNo(valor):
	return {
		'valor': valor,
		'esq': None,
		'dir': None
	}

# Cria uma arvore binaria dada as expressoes simetrica e pre ordem
def criaArvore(simetrica, preOrdem):
	if len(simetrica) < 1 or len(preOrdem) < 1:
		return None
	
	popPre = preOrdem[0]
	preOrdem = preOrdem[1::]
	
	raiz = criaNo(popPre)
	
	noEsqSim , noDirSim = simetrica.split(raiz['valor'])
	noEsqPre = preOrdem[:len(noEsqSim)]
	noDirPre = preOrdem[len(noEsqSim):]

	raiz['esq'] = criaArvore(noEsqSim, noEsqPre)
	raiz['dir'] = criaArvore(noDirSim, noDirPre)

	return raiz


''' 
Teste do metodo

Expressao simetrica: DGBAHEICF
Expressao pre ordem: DGBAHEICF
Arvore esperada:
			 A
		   /   \
		  /     \
		 B       C
		/      /   \
	   D      E     F
	   	\	 / \
	   	 G  H   I

Forma de representação da arvore em python
	
	arvore = {
		'valor': 'A',
		'esq': {
			'valor': 'B',
			'esq': [...],
			'dir': [...]
		},
		'dir': {
			'valor': 'C',
			'esq': [...],
			'dir': [...]
		}
	}

'''

simetrica = 'DGBAHEICF'
preOrdem = 'ABDGCEHIF'

arvore = criaArvore(simetrica, preOrdem)