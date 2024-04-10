from cria_arvore import arvore

# Encontra maior e menor niveis da arvore
def encontraNivel(arvore, nivelAtual = 1):
    if arvore == None:
        return -1, -1
    
    menorNivel = nivelAtual
    maiorNivel = nivelAtual
  
    menorNivelEsq, maiorNivelEsq = encontraNivel(arvore['esq'], nivelAtual + 1)
    menorNivelDir, maiorNivelDir = encontraNivel(arvore['dir'], nivelAtual + 1)

    if menorNivelDir != -1:
        menorNivel = min(menorNivel, menorNivelDir)
    if menorNivelEsq != -1:
        menorNivel = min(menorNivel, menorNivelEsq)
        
    if maiorNivelDir != -1:
        maiorNivel = max(maiorNivel,maiorNivelDir)
    if maiorNivelEsq != -1:
        maiorNivel = max(maiorNivel,maiorNivelEsq) 

    return menorNivel, maiorNivel

print(encontraNivel(arvore))
