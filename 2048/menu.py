import tkinter as tk
from tkinter import messagebox
import random
import os
import sys
import subprocess


class Tabuleiro:
    corFundo = {                    #Define as cores dos fundos de cada caractere do jogo

        '2': '#ADD8E6',
        '4': '#87CEEB',
        '8': '#87CEFA',
        '16': '#00BFFF',
        '32': '#1E90FF',
        '64': '#4169E1',
        '128': '#6495ED',
        '256': '#B0C4DE',
        '512': '#48D1CC',
        '1024': '#20B2AA',
        '2048': '#008B8B',
    }
    corLetra = {                    #Define as cores de cada caractere do jogo
        '2': '#776e65',
        '4': '#776e65',
        '8': '#776e65',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#776e65',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2',
    }

    def __init__(self):
        self.window = Tk()
        self.window.title('Projeto Final Computação')
        self.add_menu()
        self.jogoArea = Frame(self.window)
        self.mesa = []
        self.matriz = [[0] * 4 for i in range(4)]
        self.compress = False
        self.mesclar = False
        self.mover = False
        self.score = 0

        for i in range(4):                  #Cria o ambiente do jogo sem os numeros iniciais
            linhas = []
            for j in range(4):
                x = Label(self.jogoArea, text='', bg='azure4', font=('arial', 22, 'bold'), width=4, height=2)
                x.grid(row=i, column=j, padx=7, pady=7)
                linhas.append(x)
            self.mesa.append(linhas)
        self.jogoArea.grid()


    def add_menu(self):             #Cria o menu em barra do jogo contendo reiniciar, ver instruçoes e sair
        self.menubar = tk.Menu(self.window)
        self.menu = Menu(self.menubar,tearoff=0)
        self.add_comando("Reiniciar", self.novoJogo)
        self.add_comando("Instruções", self.regras)
        self.add_comando("Sair", self.sair)
        self.window.config(menu=self.menubar)

    def add_comando(self, label, command):
        self.menubar.add_command(label=label, command=command)

    def novoJogo(self):                 #Funcao que reinicia o jogo em outra janela, utilizando as libs os, sys e subprocess
        self.window.destroy()
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])

    def regras(self):           #Janela criada quando o botão de instruções é acionado

        self.window2 = Tk()

        self.label = Label(self.window2, text= "Instruções")
        self.label1 = Label(self.window2, text="1) 2048 Clássico é jogado em um tabuleiro de 4×4,")
        self.label2 = Label(self.window2, text="com peças numéricas que deslizam suavemente")
        self.label3 = Label(self.window2, text="quando o jogador as move em um dos quatro sentidos")
        self.label4 = Label(self.window2, text="disponíveis: para cima, para baixo, à esquerda e à direita. ")
        self.label5 = Label(self.window2, text="2) Cada vez, um novo número aparece aleatoriamente em um local")
        self.label6 = Label(self.window2, text="vazio na placa (com um valor de 2 ou 4). ")
        self.label7 = Label(self.window2, text="3) Os blocos deslizam o mais longe possível na direção escolhida")
        self.label8 = Label(self.window2, text="até que eles sejam interrompidos por qualquer outro bloco ou a borda do tabuleiro.")
        self.label9 = Label(self.window2, text="4) Se duas peças do mesmo número colidem durante a movimentação,")
        self.label10 = Label(self.window2, text="elas irão se fundir em um azulejo com o valor total das duas peças que colidiram.")


        self.label.grid(row=0, column=0)
        self.label1.grid(row=1, column=0)
        self.label2.grid(row=2, column=0)
        self.label3.grid(row=3, column=0)
        self.label4.grid(row=4, column=0)
        self.label5.grid(row=5, column=0)
        self.label6.grid(row=6, column=0)
        self.label7.grid(row=7, column=0)
        self.label8.grid(row=8, column=0)
        self.label9.grid(row=9, column=0)
        self.label10.grid(row=10, column=0)

        self.window2.geometry("470x250+100+100")
        self.window2.mainloop()

    def sair(self):                 #Funcao que encerra o jogo
        self.window.destroy()
        sys.exit()

    def janelarecord(self):                 #Funcao chamada quando o recorde do jogo é quebrado. OBS: o record é registrado em um arquivo .txt entregue junto ao código
        self.window3 = Tk()
        self.label = Label(self.window3, text= "Você acabou de bater o recorde!!!")
        self.label2 = Label(self.window3, text= "Seu recorde foi de:")
        self.label3 = Label(self.window3, text= self.score)
        self.label.grid(row=0, column=0)
        self.label2.grid(row=1, column=0)
        self.label3.grid(row=2, column=0)
        self.window3.geometry("200x100+100+100")
        self.window3.mainloop()

    def verificarRecord(self):              #Funcao chamada a cada jogada, verificado se o record foi quebrado
        try:
            arquivo = open('record.txt', 'r')           #Abre o arquivo em modo leitura para guardar o recorde anterior
        except OSError:
            print('Erro ao abrir arquivo de Recorde')
            return
        conteudo_record = arquivo.read()
        arquivo.close()

        conteudo_record = int(conteudo_record)

        if self.score > conteudo_record:  #verifica se o score atual é maior que o recorde. Se for, abre o arquivo em modo escrita e reescreve o valor atual
            self.janelarecord()
            conteudo_record = self.score
            try:
                arquivo2 = open('record.txt', 'w')
            except OSError:
                print('Erro ao abrir arquivo de Recorde')
                return
            print(conteudo_record)
            arquivo2.write(str(conteudo_record))
            print(conteudo_record)
            arquivo2.close()



    def reverse(self):              #Funcao que reverte a matriz do jogo
        for ind in range(4):
            i = 0
            j = 3
            while (i < j):
                self.matriz[ind][i], self.matriz[ind][j] = self.matriz[ind][j], self.matriz[ind][i]
                i += 1
                j -= 1

    def transpor(self):     #Funcao que transpoe a matriz do jogo
        self.matriz = [list(t) for t in zip(*self.matriz)]

    def compressmatriz(self):
        self.compress = False
        temp = [[0] * 4 for i in range(4)]
        for i in range(4):
            cnt = 0
            for j in range(4):
                if self.matriz[i][j] != 0:
                    temp[i][cnt] = self.matriz[i][j]
                    if cnt != j:
                        self.compress = True
                    cnt += 1
        self.matriz = temp

    def mesclarmatriz(self):            #Funcao que mescla as celulas quando elas são iguais e sendo direcionadas para o msm sentido
        self.mesclar = False
        for i in range(4):
            for j in range(4 - 1):
                if self.matriz[i][j] == self.matriz[i][j + 1] and self.matriz[i][j] != 0:
                    self.matriz[i][j] *= 2
                    self.matriz[i][j + 1] = 0
                    self.score += self.matriz[i][j]             #Concede a pontuação referente a soma das células
                    self.verificarRecord()                         #Chama funcao que verifica recorde
                    self.mesclar = True

    def celulaSel(self):                                        #Gera o 2 em posiçao pseudoaleatoria em uma das celulas de borda do jogo
        celulas = []
        for i in range(4):
            for j in range(4):
                if self.matriz[i][j] == 0:
                    celulas.append((i, j))
        curr = random.choice(celulas)
        i = curr[0]
        j = curr[1]
        self.matriz[i][j] = 2

    def verifica_mesclar(self):                         #Verifica se é possivel mesclar verticalmente ou horizontalmente
        for i in range(4):
            for j in range(3):
                if self.matriz[i][j] == self.matriz[i][j + 1]:
                    return True

        for i in range(3):
            for j in range(4):
                if self.matriz[i + 1][j] == self.matriz[i][j]:
                    return True
        return False

    def preencher(self):            #Preenche as células do jogo com suas respectivas cores de acordo com número
        for i in range(4):
            for j in range(4):
                if self.matriz[i][j] == 0:
                    self.mesa[i][j].config(text='', bg='azure4')
                else:
                    self.mesa[i][j].config(text=str(self.matriz[i][j]), bg=self.corFundo.get(str(self.matriz[i][j])), fg=self.corLetra.get(str(self.matriz[i][j])))

'''As funcoes a seguir são referentes ao estudo de manipulaçao de matrizes, após vermos diversos exemplos analisamos que 
os metodos aplicados deveriam ser esses na ordem disposta a seguir para cada um dos movimentos.
Ao transpor, mesclar, comprimir e mover em uma ordem pré estabelecida é possível manipular para que dê a impressão de que, 
por exemplo, as celulas estão apenas se movendo para direita, quando na realidade existe muito por trás dessa movimentação.
'''
class Jogo:
    def __init__(self, board):
        self.board = board
        self.fim = False
        self.vitoria = False

    def start(self):
        self.board.celulaSel()
        self.board.celulaSel()
        self.board.preencher()
        self.board.window.bind('<Key>', self.keys)
        self.board.window.mainloop()

    def keys(self, acao):
        if self.fim or self.vitoria:
            return

        self.board.compress = False
        self.board.mesclar = False
        self.board.mover= False

        selecionado = acao.keysym           #Verifica qual tecla foi apertada



        if selecionado == 'Up':             #Caso a tecla com  uma Seta para cima for apertada, movimenta nossas celulas preenchidas para cima
            self.board.transpor()
            self.board.compressmatriz()
            self.board.mesclarmatriz()
            self.board.mover = self.board.compress or self.board.mesclar
            self.board.compressmatriz()
            self.board.transpor()

        elif selecionado == 'Down':         #Caso a tecla com  uma Seta para baixo for apertada, movimenta nossas celulas preenchidas para baixo
            self.board.transpor()
            self.board.reverse()
            self.board.compressmatriz()
            self.board.mesclarmatriz()
            self.board.mover = self.board.compress or self.board.mesclar
            self.board.compressmatriz()
            self.board.reverse()
            self.board.transpor()

        elif selecionado == 'Left':         #Caso a tecla com  uma Seta para esquerda for apertada, movimenta nossas celulas preenchidas para esquerda
            self.board.compressmatriz()
            self.board.mesclarmatriz()
            self.board.mover = self.board.compress or self.board.mesclar
            self.board.compressmatriz()

        elif selecionado == 'Right':        #Caso a tecla com  uma Seta para direita for apertada, movimenta nossas celulas preenchidas para direita
            self.board.reverse()
            self.board.compressmatriz()
            self.board.mesclarmatriz()
            self.board.mover = self.board.compress or self.board.mesclar
            self.board.compressmatriz()
            self.board.reverse()
        else:
            pass

        self.board.preencher()
        print(self.board.score)

        indicador = 0
        for i in range(4):              #Analisa se alguma celula contem o 2048 indicando vitoria. Se encontrar, indicador recebe 1
            for j in range(4):
                if (self.board.matriz[i][j] == 2048):
                    indicador = 1
                    break

        if (indicador == 1):  # Se indicador for igual a 1, significa que o usuario ganhou. Dessa forma, exibindo uma mensagem de vitória
            self.vitoria = True
            messagebox.showinfo('2048', message='Vitória!!')
            print("vitoria")
            return

        for i in range(4):    #Verifica se ainda possui celula vazia
            for j in range(4):
                if self.board.matriz[i][j] == 0:
                    indicador = 1
                    break

        if not (indicador or self.board.verifica_mesclar()):   #Se não existe celula vazia e se não é possivel mais mesclar celulas, o jogo retorna derrota
            self.fim = True
            messagebox.showinfo('2048', 'Fim de Jogo!!!')
            print("Fim")

        if self.board.mover:
            self.board.celulaSel()

        self.board.preencher()


board = Tabuleiro()
game = Jogo(board)
game.start()