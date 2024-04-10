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
arvore.inserir(13)



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
    
def verificaRN(arvore: ArvoreRubroNegra):
    validaEsq = True
    validaDir = True
    if arvore.esq != None:
        validaEsq = verificaRN(arvore.esq)
    if arvore.dir != None:
        validaDir = verificaRN(arvore.dir)
    
    atualizaPostos(arvore)
    if verificaPosto(arvore):
        return validaEsq and validaDir
    return False
    

arvore.prinPosOrdem()
print()
verifica = verificaRN(arvore)
print(verifica)