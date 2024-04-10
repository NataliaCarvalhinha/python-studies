from arvore_binaria_busca import *

arvore = ArvoreBinariaBusca(7)

arvore.inserir(3)
arvore.inserir(1)
arvore.inserir(5)
arvore.inserir(6)
arvore.inserir(11)
arvore.inserir(9)
arvore.inserir(8)

# def altura(arvore):
#         if arvore.esq == None and arvore.dir == None:
#             return 1 
#         if arvore.esq == None:
#             return altura(arvore.dir) + 1
#         if arvore.dir == None:
#             return altura(arvore.esq) + 1
#         return max(altura(arvore.esq), altura(arvore.dir)) + 1

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
    alturaEsq = 0
    alturaDir = 0
    if arvore.esq != None:
        alturaEsq = arvore.esq.altura()
    if arvore.dir != None:
        alturaDir = arvore.dir.altura()
        
    return abs(alturaEsq - alturaDir)

def verificaPosto(arvore, posto):
    return posto <= 1
    

    

def transformaAVL(arvore: ArvoreBinariaBusca):
    
    alturaEsq = 0
    alturaDir = 0
    if arvore.esq != None:
        arvore.esq = transformaAVL(arvore.esq)
        alturaEsq = arvore.esq.altura()
    if arvore.dir != None:
        arvore.dir = transformaAVL(arvore.dir)
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
arvore = transformaAVL(arvore)
arvore.prinPosOrdem()

