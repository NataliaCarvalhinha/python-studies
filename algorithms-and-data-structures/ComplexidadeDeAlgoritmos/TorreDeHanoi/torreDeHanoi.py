# Exibe a movimentação de uma peça na torre de Hanoi
def move(origem, destino):
	print(f'{origem}->{destino}')   

# Gera os movimentos necessários para resolver a torre de Hanoi com n peças
def hanoi(n, A, B, C):
	if n == 1: 
		move(A, B)
	else:						
		hanoi(n - 1, A, C, B)  # T(n-1)
		move(A, B)   		   
		hanoi(n - 1, C, B, A)  # T(n-1)

#T = 1 + (n - 1) + 1 + (n - 1)= 2(n - 1) + 2
#O(n)

# Teste dos métodos

hanoi(4, 'A', 'B', 'C')
