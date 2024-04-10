def infix_to_posfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3} 
    stack = []
    output = []
    
    for token in expression:
        if token.isalnum():
            output.append(token)
        elif token in '+-*/^':
            while stack and stack[-1] in '+-*/^' and precedence[token] < precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
    while stack:
        output.append(stack.pop())
    return ''.join(output)


print(infix_to_posfix("A + B * C"))
print(infix_to_posfix("A + B"))
print(infix_to_posfix("A + B - C"))
print(infix_to_posfix("(A + B) * (C - D)"))
