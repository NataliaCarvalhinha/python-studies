from cria_arvore import arvore

# Encontra maior e menor niveis da arvore
def exibe_folhas(arvore, folhas = []):
    if arvore is not None:
        if arvore['esq'] == None and arvore['dir'] == None:
            folhas.append(arvore['valor'])
        
        folhas = exibe_folhas(arvore['esq'], folhas)
        folhas = exibe_folhas(arvore['dir'], folhas)
        
    return folhas

    
    

print(exibe_folhas(arvore))