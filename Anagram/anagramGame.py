import random


def alterar_ranking(conteudo_ranking, nome, pontos):                                #Altera o ranking alterando pontos ou adicionando pessoas
    inserida = False
    for i in range(len(conteudo_ranking)):                                          #Percorre as posicoes da lista do arquivo
        nome_rank, ponto_rank = conteudo_ranking[i].split(' ')                      #Define as variaveis
        if nome == nome_rank:                                                       #Compara as strings de nome
            inserida = True
            if pontos > int(ponto_rank):                                            #Verifica se os pontos da pessoa foram maiores
                conteudo_ranking[i] = f'{nome} {pontos}\n'                          #Caso maiores, alteram na lista
                break
    if inserida == False:                                                           #Caso nao exista o nome, ele e adicionado
        conteudo_ranking.append(f'{nome} {pontos}\n')
    return conteudo_ranking


def pega_segundoelem(elem):   #Gera o parametro nao fixo que esta sendo passado
    return int(elem[1])                                                             #Retorna os pontos como inteiro


def ordenar_ranking(lista):  # [3,1,4,2,5]  [['w','5'],['k','2']]
    lista_info = []
    for i in range(len(lista)):                                                     #Percorre a posicao da lista
        lista_info.append(lista[i].split(' '))                                      #Adiciona elemento na posicao indicada pulando o ' '
    lista_info.sort(key=pega_segundoelem, reverse=True)                             #Faz o ordenamento reverso chamando a funcao que retorna os pontos
                                                                                    # Key representa o parametro que esta sendo passado
    return lista_info


def pop_de_string(palavra, pos):  # Reproduz a função pop de listas para o caso de string
    palavra_lista = list(palavra)                                                   #Separa todas as letras e transforma as letras em elemntos da lista
    palavra_lista.pop(pos)                                                          #Retira a letra da posicao especificada
    "".join(palavra_lista)                                                          #Junta as palavras novamente
    return palavra_lista


def findword(linhas, tamanho):  # Encontra uma palavra base para buscar anagramas
    while True:
        pos = random.randint(0, len(linhas))                                        #Seleciona posicao pseudoaleatoria de da lista
        if len(linhas[pos]) == tamanho:                                             #Verifica se o tamanho da palavra e igual ao tamanho pedido
            print(linhas[pos])                                                      #Printa a palavra base
            return linhas[pos]


def is_anagram(palavra_base, palavra):  # Analisa se a palavra é anagrama de outra
    result = True
    copy_palavra_base = palavra_base                                                #Cria copia da palavra base
    copy_palavra = palavra                                                          #Cria copia da palavra
    for letra in copy_palavra:                                                      #Percorre cada letra da palavra
        if letra in copy_palavra_base:                                              #Verifica se a letra se encontra na palavra
            indice = copy_palavra.index(letra)                                      #O index verifica a posicao da letra
            indice_base = copy_palavra_base.index(letra)

            copy_palavra = pop_de_string(copy_palavra, indice)                      #A funcao retira a letra analisada da copia da palavra
            copy_palavra_base = pop_de_string(copy_palavra_base, indice_base)
        else:                                                                       #Caso a letra nao se encontre, nao e anagrama
            result = False
            break
    return result


def find_anagram(palavra, linhas):  # Encontra todos os anagramas da lista
    anagramas = []
    for i in linhas:                                                                    #Percorre cada palavra na lista
        if is_anagram(palavra, i) == True:                                              #Verifica se a funcao chamada retorna verdadeiro
            anagramas.append(i)                                                         #Adiciona a palavra a lista
    return anagramas

def criar_sublistas(palavra,linhas):  # Transforma a lista de palavras em uma lista com sublista de palavras de acordo com o tamanho de caracteres
    lista = []
    for letras in range(1, len(palavra)+1):                                             #Loop com o valor cresncente de letras
        sublista = []
        for word in linhas:                                                             #Acessa cada palavra na lista de anagramas
            if len(word) == letras:                                                     #Compara o valor de letras com o tamanho da palavra
                sublista.append(word)                                                   #Adiciona a palavra a subslista
        lista.append(sublista)                                                          #Adiciona sublista a lista
    return lista


def anagram_codigo(lista):  # Codifica o anagrama para ser possivel ver apenas a quantidade de caracteres
    string = ''
    for sublista in lista:                                                              #Acessa sublista
        for palavra in sublista:                                                        #Acessa elemento
            string = string + '*' * len(palavra) + ' '                                  #Adiciona codigo do mesmo tamanho da palavra a string
        string = string + '\n'
    return string


def revelar_anagram(lista, palavras_acerto):   #Revela a palavra-anagrama que foi acertada
    string = ''
    for sublista in lista:                                                              #Acessa a sublista
        for palavra in sublista:                                                        #Acessa o elemento
            if palavra in palavras_acerto:                                              #Verifica se o elemento esta na lista de palavras acertadas
                string = string + palavra + ' '                                         #Adciona a palavra acertada
            else:
                string = string + '*' * len(palavra) + ' '                              #Adiciona codigo no lugar da palavra nao acertada
        string = string + '\n'
    return string


def acertos_erros(anagramas, lista):  # Analisa as respostas do usuario e conta seus pontos e tentativas
    tentativas = 10                                                                     #Define as 'vidas' dos jogo
    palavras = len(anagramas)
    pontos = 0
    palavras_acerto = []                                                                #Lista das palavras que ja foram acertadas
    print(anagram_codigo(lista))                                                        #Printa os anagramas criptografados
    print(f'\nVoce tem 10 tentativos e {palavras} palavras para acertar')
    while tentativas >= 1 and palavras >= 1:                                            #Loop para manter as tentativas ate terminar as vidas ou as palavras
        palavra_base = input('\nTente acertar uma palavra:   ')                         #Input da tentativa
        if palavra_base in anagramas:                                                   #Verifica se o anagrama esta na lista
            for sublista in lista:
                if palavra_base in sublista:                                            #Verifica se anagrama esta em sublista
                    pontos = pontos + len(palavra_base)                                 #Adiciona pontuaçao em caso de acerto
                    palavras = palavras - 1                                             #Diminui as palavras restantes
                    palavras_acerto.append(palavra_base)                                #Adiciona a palavra acertada na lista
                    print(f'\n Parabens, voce acertou\n Voce tem {pontos} pontos e {palavras} palavras para acertar.\n')  #Printa as tentativas e vidas
                    print(revelar_anagram(lista, palavras_acerto))                      #Revela as palavras ja acertadas
        else:
            tentativas = tentativas - 1                                                 #Diminui as vidas
            print(f'\n Poxa, voce errou. Tente novamente.\n Voce tem {tentativas} tentativas. \n Voce tem {pontos} pontos')  #Printa as tentativas e os pontos
    if tentativas == 0:
        print('Suas tentativas acabaram. Para continuar retorne ao menu.')
    return pontos


def jogo(linhas, tamanho):                                          #Funcao onde o jogo roda
    palavra = sorted(findword(linhas, tamanho))                     #Encontra a palavra base
    anagramas = find_anagram(palavra, linhas)                       #Encontra os anagramas dessa palavras base
    lista = criar_sublistas(palavra, anagramas)                     #Transforma a lista de anagramas em uma lista com sublistas que divide pelo numero de caracteres
    pontos = acertos_erros(anagramas, lista)                        #Realiza a contagem de pontos a partir dos acertos
    return pontos


def menu():
    print('------------Anagrama------------')
    print('1 - Jogar')
    print('2 - Instruçoes')
    print('3 - Ranking')
    print('4 - Sair')

    selecionar = int(input('\nDigite uma das opçoes acima:   '))    #Recebe a escolha do usuario

    if selecionar == 1:                                             #Direciona o usuario para o jogo
        nome = input('Digite seu nome:    ')                        #Recebe o nome do usuario
        print('1 - Nivel Facil')
        print('2 - Nivel Medio')
        print('3 - Nivel Dificil')

        selecionar_nivel = int(input('\n Digite uma das opçoes acima:    '))    #Recebe a escolha de nivel do usario
        arquivo = open('dicionario.txt', 'r')                                   #Abre o arquivo com as palavras
        conteudo = arquivo.read()                                               #
        linhas = conteudo.split('\n')                                           #Transforma o arquivo em uma lista de palavras
        pontos = 0
        if selecionar_nivel == 1:                                               #Direciona para o nivel facil
            tamanho = 5
            pontos = jogo(linhas, tamanho)                                      #Chama a funcao jogo com os argumentos: lista de palavras e tamamho das palavras
        if selecionar_nivel == 2:                                               #Direciona para o nivel medio
            tamanho = 7
            pontos = jogo(linhas, tamanho)                                      #Chama a funcao jogo com os argumentos: lista de palavras e tamanho das palavras
        if selecionar_nivel == 3:                                               #Direciona para o nivel dificil
            tamanho = 9
            pontos = jogo(linhas, tamanho)                                      #Chama a funcao jogo com os argumentos: lista de palavras e tamanho das palavras

        ranking = open('Ranking.txt', 'r')                                      #Abre o arquivo Ranking
        conteudo_ranking = ranking.readlines()                                  #Recebe uma lista com as informacoes do arquivo
        ranking.close()                                                         #Fecha o arquivo
        ranking = open('Ranking.txt', 'w')                                      #Abre o arquivo em modo escrita
        lista_ranking = alterar_ranking(conteudo_ranking, nome, pontos)         #Chama a funcao que altera a lista do arquivo
        ranking.writelines(lista_ranking)                                       #Reescreve o arquivo
        ranking.close()                                                         #Fecha o arquivo

    if selecionar == 2:                                                         #Direciona para as Instrucoes
        print('Forme o maior número possível de palavras usando as letras disponíveis.')
        print('O nivel limita o tamanho da palavras')
        print('O nivel facil sao palavras com 5 caracteres ou menos')
        print('O nivel medio sao palavras com 7 caracteres ou menos')
        print('O nivel dificil sao palavras com 9 caracteres ou menos')

    if selecionar == 3:                                                         #Direciona para printar o ranking
        ranking = open('Ranking.txt', 'r')                                      #Abre o arquivo
        conteudo = ranking.readlines()                                          #Transforma o arquivo em lista
        ranking_ordenado = ordenar_ranking(conteudo)                            #Chama a funcao que ordena o ranking de acordo com a pontuacao
        ranking.close()                                                         #Fecha arquivo

        print(f'{str("Nome").ljust(10)}Pontos')                                 #Printa nome e ponto para formar a tabela

        for elem in ranking_ordenado:                                           #Loop para acessar cada elemento da lista gerada na funcao de ordenar
            print(f'{str(elem[0]).ljust(10)}{elem[1]}')

    if selecionar == 4:                                                         #Direciona para a saida do jogo
        print('Saindo')

    else:
        print('Insira uma valor valido')                                        #Garante que o valor e valido
    return selecionar

while menu() != 4:                                                              #Mantem o menu em loop, exceto quando a saida seja escolhida
    pass