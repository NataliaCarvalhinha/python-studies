from arvore_binaria_busca import *

arvore = ArvoreBinariaBusca(7)

arvore.inserir(3)
arvore.inserir(1)
arvore.inserir(5)
arvore.inserir(6)
arvore.inserir(11)
arvore.inserir(9)
arvore.inserir(8)

def simplesDireita(arvore):
    u = arvore.esq
    arvore.esq = u.dir
    u.dir = arvore
    return u

def duplaDireita(arvore):
    u = arvore.esq
    v = u.dir
    u.dir = v.esq
    arvore.esq = v.dir
    v.esq = u
    v.dir = arvore
    return v

def simplesEsquerda(arvore):
    u = arvore.dir
    arvore.dir = u.esq
    u.esq = arvore
    return u

def duplaEsquerda(arvore):
    u = arvore.dir
    v = u.esq
    arvore.dir = v.esq
    u.esq = v.dir
    v.esq = arvore
    v.dir = u
    return v

def getPosto(arvore):
    if arvore == None:
        return 0
    elif arvore.esq == None or arvore.dir == None:
        return 1
    else:
        maiorPostoNetos = max(
            getPosto(arvore.esq.esq),
            getPosto(arvore.esq.dir),
            getPosto(arvore.dir.esq),
            getPosto(arvore.dir.dir)
        )
        
        return maiorPostoNetos + 1
    
def verificaPosto(arvore, posto):
    if arvore == None and posto != 0:
        return False
    if (arvore.esq == None or arvore.dir == None) and posto != 1:
        return False
    postoEsq = getPosto(arvore.esq)
    postoDir =  getPosto(arvore.dir)
    if posto < postoEsq or posto < postoDir or \
       posto > postoEsq + 1 or posto > postoDir + 1:
        return False
    if arvore.esq != None:
        if arvore.esq.esq != None and posto <= getPosto(arvore.esq.esq):
            return False
        if arvore.esq.dir != None and posto <= getPosto(arvore.esq.dir):
            return False
    if arvore.dir != None:
        if arvore.dir.esq != None and posto <= getPosto(arvore.dir.esq):
            return False
        if arvore.dir.dir != None and posto <= getPosto(arvore.dir.dir):
            return False
    return True 

def transformaGraduada(arvore: ArvoreBinariaBusca):
    alturaEsq = 0
    alturaDir = 0
    if arvore.esq != None:
        arvore.esq = transformaGraduada(arvore.esq)
        alturaEsq = arvore.esq.altura()
    if arvore.dir != None:
        arvore.dir = transformaGraduada(arvore.dir)
        alturaDir = arvore.dir.altura()
        
    posto = getPosto(arvore)
    if verificaPosto(arvore, posto):
        return arvore
    
    if alturaEsq > alturaDir:
        if arvore.esq.alturaEsq() > arvore.esq.alturaDir():
            arvore = simplesDireita(arvore)
        elif arvore.esq.alturaEsq() < arvore.esq.alturaDir():
            arvore = duplaDireita(arvore)

    elif alturaEsq < alturaDir:
        if arvore.dir.alturaEsq() > arvore.dir.alturaDir():
            arvore = duplaEsquerda(arvore)
        elif arvore.dir.alturaEsq() < arvore.dir.alturaDir():
            arvore = simplesEsquerda(arvore)

    return arvore
    
arvore.prinPosOrdem()
print()
arvore = transformaGraduada(arvore)
arvore.prinPosOrdem()
        
           
        

    
    
