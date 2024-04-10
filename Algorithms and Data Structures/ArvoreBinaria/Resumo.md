
Rotaçẽs:
-> 

AVL 
1. Percorrer a árvore recursivamente das folhas para a raiz (POS ORDEM)
2. Pegar as alturas das subarvores a esquerda e a direita em cada nível
3. Calcular o módulo da diferença das alturas das subarvores a esquerda e a direita
4. Se a diferença for menor ou igual a 1, avançamos para o próximo nó sem fazer nenhuma modificação. Se a diferença for maior que 1, validamosas rotações necessárias para equilibrar a árvore e aplicamos as rotações.

GRADUADA
1. Percorrer a árvore recursivamente das folhas para a raiz (POS ORDEM)
2. Pegar as alturas das subarvores a esquerda e a direita em cada nível
3. Calcular o posto do nó com base nas seguintes regras:
    3.1 Se o nó for externo, posto(nó) = 0
    3.2 Se o nó for pai de pelo menos um nó externo, posto(nó) = 1
    3.3 Se não, o posto do nó vai ser igual ao maior posto entre os netos + 1
4. Validamos se todos os postos respeitam TODAS as regras descritas no passo 3. Se respeitar, avançamos para o próximo nó sem fazer nenhuma modificação. Se não respeitar, validamos as rotações necessárias para equilibrar a árvore e aplicamos as rotações.

RUBRO-NEGRA
1. Percorrer a árvore recursivamente das folhas para a raiz (POS ORDEM)
2. Pegar as alturas das subarvores a esquerda e a direita em cada nível
3. Calcular o posto do nó e de seus descendentes com base nas seguintes regras:
    3.1 Todo nó externo é negro
    3.2 Partimos do princípio que todos os outros nós são inicialmente negros 
    3.3 Calculamos os caminhos do nó até seus descendentes nós externos. Se a quantidade de nós nos caminhos for diferente em qualquer possível caminho, transformamos um dos nós descendentes em rubro, garantindo a mesma quantatidade de nós negros em todos os possíveis caminhos. Desde que o nó não possua um filho rubro.
4. Validamos se todos os postos respeitam TODAS as regras descritas no passo 3. Se respeitar, avançamos para o próximo nó sem fazer nenhuma modificação. Se não respeitar, validamos as rotações necessárias para equilibrar a árvore e aplicamos as rotações.

