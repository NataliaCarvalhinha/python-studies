#  Transforma da notação infixa para prefixa
def infix_to_prefix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3} # Define a precedencia dos operadores, quanto mais alto, mais prioritário
    output = [] # Expressão final
    stack = []  # Pilha para operadores que ainda não foram concluidos

    expression = expression[::-1]  # Inverte a expressão infixa para facilitar
    
    for token in expression: # Para cada caracter da expressão
        if token.isalnum():  #  Se for um numero ou letra
            output.append(token) # Incluimos na expressão final
        elif token in "+-*/^": # Senão, se for um operador
            while (stack and stack[-1] in "+-*/^" and precedence[token] < precedence[stack[-1]]): # Se tiver algum operador com maior precedencia no topo da pilha de operadores
                output.append(stack.pop()) # Incluimos o operador de maior precedencia na expressão final
            stack.append(token) # Incluimos o operador atual no topo da pilha de operadores
        elif token == ')': # Se for um fecha parenteses
            stack.append(token) # Incluimos ele no topo da pilha de operadores
        elif token == '(': # Se for um abre parenteses
            while stack and stack[-1] != ')': # Enquanto não encontrarmos o fecha parenteses correspondente na pilha de operadores
                output.append(stack.pop()) # Desempilhamos a pilha de operadores e colocamos cada elemento na expressão final
            stack.pop() # Removemos o fecha parentes da pilha de operadores sem incluir na expressão final

    while stack: # Enquanto existir elementos na lista de operadores
        output.append(stack.pop()) # Desempilhamos a pilha de operadores colocando cada operador na expressão final

    return ''.join(output[::-1]) # Retornamos a expressão final invertida para voltar a inversão inicial


# Exemplo de uso:
print(infix_to_prefix("A + B * C"))
print(infix_to_prefix("A + B"))
print(infix_to_prefix("A + B - C"))
print(infix_to_prefix("(A + B) * (C - D)"))

''' --------------------------------[TESTE 1]--------------------------------

OUTPUT: []
STACK: []


EXPRESSAO ORIGINAL:(A + B) * (C - D)


INVERTE EXPRESSAO: )D - C( * )B + A(

----------[1ª ITERAÇÃO]----------

)D - C( * )B + A(
^
token

OUTPUT: []
STACK: [)]

----------[2ª ITERAÇÃO]----------

)D - C( * )B + A(
 ^
token

OUTPUT: [D]
STACK: [)]

----------[3ª ITERAÇÃO]----------

) D - C ( * ) B + A (
    ^
token

OUTPUT: [D]
STACK: [) -]

----------[4ª ITERAÇÃO]----------

) D - C ( * ) B + A (
      ^
token

OUTPUT: [DC]
STACK: [) -]

----------[5ª ITERAÇÃO]----------

) D - C ( * ) B + A (
        ^
token

OUTPUT: [DC-]
STACK: []

----------[6ª ITERAÇÃO]----------

) D - C ( * ) B + A (
          ^
token

OUTPUT: [DC-]
STACK: [*]


'''

''' --------------------------------[TESTE 2]--------------------------------
OUTPUT: []
STACK: []


EXPRESSAO ORIGINAL: A + B * C


INVERTE EXPRESSAO: C * B + A

----------[1ª ITERAÇÃO]----------

C * B + A
^
token

OUTPUT: [C]
STACK: []

----------[2ª ITERAÇÃO]----------

C * B + A
  ^
token

OUTPUT: [C]
STACK: [*]

----------[3ª ITERAÇÃO]----------

C * B + A
    ^
token

OUTPUT: [CB]
STACK: [*]

----------[4ª ITERAÇÃO]----------

C * B + A
      ^
token

OUTPUT: [CB*]
STACK: [+]

----------[5ª ITERAÇÃO]----------

C * B + A
        ^
token

OUTPUT: [CB*A]
STACK: [+]

----------[FIM DO FOR]----------

WHILE: 

OUTPUT: [CB*A+]
STACK: []

INVERTE OUTPUT: +A*BC

'''
