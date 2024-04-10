class ArvoreRubroNegra:
    RUBRO = 0
    NEGRA = 1
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None
        self.posto = ArvoreRubroNegra.NEGRA
    
    def inserir(self, valor):
        if valor < self.valor:
            if self.esq == None:
                self.esq = ArvoreRubroNegra(valor)
            else:
                self.esq.inserir(valor)

        if valor > self.valor:
            if self.dir == None:
                self.dir = ArvoreRubroNegra(valor)
            else:
                self.dir.inserir(valor)

    def __str__(self):
        return f'[{self.esq}] <- [{self.valor}] -> [{self.dir}]'

    def prinSimetrica(self):
        if self.esq != None:
            self.esq.prinSimetrica()
        
        print(self.valor, end = ' ')

        if self.dir != None:
            self.dir.prinSimetrica()

    def prinPreOrdem(self):
        print(self.valor, end = ' ')

        if self.esq != None:
            self.esq.prinPreOrdem()

        if self.dir != None:
            self.dir.prinPreOrdem()

    def prinPosOrdem(self):
        if self.esq != None:
            self.esq.prinPosOrdem()

        if self.dir != None:
            self.dir.prinPosOrdem()
        
        print(f'{self.valor}[{self.posto}]', end = ' ')

    def busca(self,valor):
        
        if self.valor == valor :
            return valor

        if self.valor > valor:
            if self.esq == None:
                return None
            
            return self.esq.busca(valor)
        
        if self.dir == None:
            return None
        
        return self.dir.busca(valor)
    
    def altura(self):
        if self.esq == None and self.dir == None:
            return 1 
        if self.esq == None:
            return self.dir.altura() + 1
        if self.dir == None:
            return self.esq.altura() + 1
        return max(self.esq.altura(), self.dir.altura()) + 1
    
    def alturaEsq(self):
        if self.esq == None:
            return 0
        return self.esq.altura()
    
    def alturaDir(self):
        if self.dir == None:
            return 0
        return self.dir.altura()
