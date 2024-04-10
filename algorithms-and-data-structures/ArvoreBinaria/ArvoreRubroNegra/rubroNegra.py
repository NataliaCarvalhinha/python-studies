from ArvoreBinaria.ArvoreRubroNegra.arvore_RN import *


arvore = ArvoreRubroNegra(7)

arvore.inserir(3)
arvore.inserir(1)
arvore.inserir(5)
arvore.inserir(4)
arvore.inserir(6)
arvore.inserir(11)
arvore.inserir(9)
arvore.inserir(8)

def simplesDireita(arvore):
    print('simplesDireita')
    u = arvore.esq
    arvore.esq = u.dir
    u.dir = arvore
    return u

def duplaDireita(arvore):
    print('duplaDireita')
    u = arvore.esq
    v = u.dir
    u.dir = v.esq
    arvore.esq = v.dir
    v.esq = u
    v.dir = arvore
    return v

def simplesEsquerda(arvore):
    print('simplesEsquerda')
    u = arvore.dir
    arvore.dir = u.esq
    u.esq = arvore
    return u

def duplaEsquerda(arvore):
    print('duplaEsquerda')
    u = arvore.dir
    v = u.esq
    arvore.dir = v.esq
    u.esq = v.dir
    v.esq = arvore
    v.dir = u
    return v

def contaNegros(arvore):
    if arvore == None:
        return 1
    if arvore.posto == ArvoreRubroNegra.NEGRA:
        return max(contaNegros(arvore.esq),contaNegros(arvore.dir)) + 1
    if arvore.posto == ArvoreRubroNegra.RUBRO:
        return max(contaNegros(arvore.esq),contaNegros(arvore.dir))
    

def atualizaPostos(arvore: ArvoreRubroNegra):
    if arvore == None:
        return 
    contaNegrosEsq = contaNegros(arvore.esq)
    contaNegrosDir = contaNegros(arvore.dir)
    print(f'{arvore.valor}->Esq[{contaNegrosEsq}] Dir[{contaNegrosDir}]')
    if (contaNegrosEsq > contaNegrosDir):
        if (arvore.esq.esq == None and arvore.esq.dir == None) or\
            ((arvore.esq.esq != None and arvore.esq.esq.posto != ArvoreRubroNegra.RUBRO) and\
            (arvore.esq.dir != None and arvore.esq.dir.posto != ArvoreRubroNegra.RUBRO)):
            arvore.esq.posto = ArvoreRubroNegra.RUBRO
            print(f'\t{arvore.esq.valor}->[{arvore.esq.posto}] ')
    elif contaNegrosEsq < contaNegrosDir:
        if (arvore.dir.esq == None and arvore.dir.dir == None)or\
            ((arvore.dir.esq != None and arvore.dir.esq.posto != ArvoreRubroNegra.RUBRO) and\
            (arvore.dir.dir != None and arvore.dir.dir.posto != ArvoreRubroNegra.RUBRO)):
            arvore.dir.posto = ArvoreRubroNegra.RUBRO
            print(f'\t{arvore.dir.valor}->[{arvore.dir.posto}] ')

    
        
def verificaPosto(arvore):
    if arvore == None and arvore.posto != ArvoreRubroNegra.NEGRA:
        return False
    contaNegrosEsq = contaNegros(arvore.esq)
    contaNegrosDir = contaNegros(arvore.dir)
    if contaNegrosEsq != contaNegrosDir:
        return False
    if arvore.posto == ArvoreRubroNegra.RUBRO:
        if arvore.esq != None and arvore.esq.posto == ArvoreRubroNegra.RUBRO:
            return False
        if arvore.dir != None and arvore.dir.posto == ArvoreRubroNegra.RUBRO:
            return False
    return True
    
    
    
def transformaRN(arvore: ArvoreRubroNegra):
    alturaEsq = 0
    alturaDir = 0
    if arvore.esq != None:
        arvore.esq = transformaRN(arvore.esq)
        alturaEsq = arvore.esq.altura()
    if arvore.dir != None:
        arvore.dir = transformaRN(arvore.dir)
        alturaDir = arvore.dir.altura()
    
    atualizaPostos(arvore)
    if verificaPosto(arvore):
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
arvore = transformaRN(arvore)
arvore.prinPosOrdem()