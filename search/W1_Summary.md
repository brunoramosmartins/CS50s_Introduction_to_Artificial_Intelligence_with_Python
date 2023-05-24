# Week 1: Search

## Search Problems

- agent: entidade que percebe seu ambiente e age sobre esse ambiente
- state: um configuração do agent e seu ambiente
- initial state: o estado em que o agent começa
- actions: escolhas que podems ser feitas em uma estado
- transition model: uma descrição de qual estado resulta da execução de qualquer ação aplicável em qualquer estado
- state space: conjunto de todos os states alcançáveis a partir do initial state por quaisquer sequência de actions
- goal test: maneira de determinar se um estado é um estado objetivo
- path cost: custo número associado a um determinado caminho

Um problema de busca envolve um agente que procura encontrar uma solução em um espaço de estados, percorrendo diferentes estados através de aplicações de ações. O objetivo é encontrar uma sequência de ações que leve do estado inicial ao estado objetivo.

## Solution

Uma sequência de ações que leva do estado inicial a um estado objetivo. Algumas estratégias de busca mais comuns nesses problemas:

- Depth-First Search (DFS): Nessa estratégia, o agente explora o espaço de busca seguindo um ramo específico até atingir o limite máximo de profundidade ou encontrar um estado objetivo. Se não encontrar um estado objetivo, retrocede e explora outros ramos. O DFS é implementado usando uma pilha.

- Breadth-First Search (BFS): Nessa estratégia, o agente explora o espaço de busca em camadas, começando pelo estado inicial e visitando todos os estados adjacentes antes de se mover para os estados mais distantes. O BFS é implementado usando uma fila.

- Uninformed Search (UCS): Essa estratégia expande o nó com o menor custo acumulado até o momento. Em vez de considerar apenas profundidade ou a ordem de expansão, o UCS leva em conta os custos associados a cada ação ou transição de estado.

- A\* Search (A-Star): O algoritmo A\* é uma estratégia informada que combina a heurística (que fornece uma estimativa do custo do caminho restante) com o custo acumulado até o momento. Ele seleciona os nós para expansão com base em uma função de avaliação que leva em conta tanto o custo atual quanto a heurística.

- Greedy Best-First Search: Essa estratégia utiliza apenas a função heurística para decidir quais nós expandir. Ela sempre seleciona o nó mais promissor, de acordo com a heurística, na esperança de chegar rapidamente ao estado objetivo.

**Heuristc Function:** A função heurística em um problema de busca fornece uma estimativa do custo restante para atingir o estado objetivo a partir de um determinado estado. Em outras palavras, ela atribui um valor heurístico aos estados que indica quão promissores são em direção ao objetivo. Sendo assim, ela utiliza informações adicionais ou conhecimento sobre o problema para estimar o custo restante. Essas informações podem ser baseadas em características do estado, como distância, comparações com estados objetivos anteriores ou outras heurísticas específicas do domínio. É importante destacar que a função heurística não fornece um custo exato, mas sim uma estimativa. Ela é usada principalmente em algoritmos informados, como algoritmo A\*, para orientar a busca em direção aos estados mais promissores.

## Depth-First Search

O algoritmo de busca em profundidade (DFS) explora um caminho até o máximo de profundidade possível antes de retroceder e explorar outros caminhos. Ele começa pelo nó inicial e avança em uma direção específica até atingir um estado objetivo ou não haver mais nós para explorar nesse caminho. Nesse ponto, ele retrocede para o nó anterior e continua explorando outros caminhos disponíveis. O DFS utiliza uma estrutura de dados chamada de pilha para armazenar os nós a serem explorados. Cada nó é visitado e, em seguida, seus nó vizinhos são empilhados. Dessa forma, o algoritmo explora cada caminho em profundidade antes de voltar.

As vantagens do DFS incluem:

- O DFS é adequado para espaços de busca profundos, onde encontrar uma solução próxima ao nó inicial é mais desejável do que encontrar a solução mais curta em termos de número de ações. Isso pode ser útil em certos tipos de problemas ou situações específicas.
- Em comparação com o algoritmo de busca em largura, o DFS requer menos espaço de memória, pois explora um único caminho até a profundidade máxima antes de retroceder.

No entanto, o DFS também possui algumas desvantagens:

- O DFS pode encontrar uma solução rapidamente, mas não garante que seja a solução mais curta ou ótima em termos de custo. Isso ocorre porque o algoritmo pode seguir caminhos mais longos antes de explorar caminhos mais curtos que podem levar a soluções melhores.
- Se o grafo de busca contiver ciclos, o DFS pode ficar preso em um loop infinito, repetindo nós e caminhos indefinidamente, a menos que sejam tomadas medidas para evitar isso.

## Breadth-First Search

O algoritmo de busca em largura (BFS) é uma estratégia de busca que explora todos os estados vizinhos de um nó antes de prosseguir para os estados vizinhos desses estados. Ele começa pela raiz (estado inicial) e explora todos os nós em cada nível antes de passar para o próximo nível do grafo. O BFS garante que o caminho encontrado para o objetivo seja o mais curto possível. O BFS utiliza uma estrutura de dados chamada fila para armazenar os nós que serão explorados em ordem de descoberta. Cada nó é visitado e, em seguida, seus nós vizinhos são colocados na fila. Dessa forma, o algoritmo garante que os nós mais próximos do estado inicial sejam visitados antes dos nós mais distantes.

As vantagens do algoritmo de busca em largura (BFS) são:

- Encontrar a solução mais curta em termos de número de ações ou de caminho percorrido.
- Se houver uma solução, o BFS sempre encontrará uma.
- Quando todos os custos de ação são iguais, o BFS encontra uma solução ótima.

As desvantagens do BFS incluem:

- Requer muito espaço de memória. O BFS armazena todos os nós de um nível antes de passar para o próximo, o que pode levar a uma grande utilização de memória, especialmente em grafos extensos.
- Pode ser lento em grafos grandes. Se o espaço de busca for muito extenso, o BFS pode levar muito tempo para concluir a busca.

## A\* (A-Star)

O algoritmo A\* é uma estratégia de busca informada que combina o custo acumulado até o momento com uma função heurística para selecionar os próximos nós a serem explorados. Ele utiliza uma função de avaliação que leva em consideração o custo atual e uma estimativa do custo restante para atingir o estado objetivo. Essa estimativa é fornecida pela função heurística, que atribui um valor heurístico a cada nó com base em informações adicionais ou conhecimento sobre o problema. A função heurística fornece uma estimativa do custo restante para atingir o estado objetivo a partir de um determinado estado. O objetivo é selecionar os nós que têm o menor valor da função de avaliação, indicando que são promissores em direção ao objetivo.

O algoritmo A\* utiliza uma estrutura de dados chamada lista de prioridade para armazenar os nós a serem explorados, ordenando-os com base na função de avaliação. Ele seleciona o nó com menor valor da função de avaliação e o explora, atualizando os valores de custo acumulado e função de avaliação dos nós vizinhos. O A\* é amplamente utilizado em problemas de busca em que é necessário encontrar o caminho mais curto ou ótimo, levando em consideração tanto o custo acumulado quanto a estimativa heurística. Ele combina a eficiência do algoritmo de busca em largura com a orientação da função heurística.

O algoritmo A\* possui várias vantagens em relação ao BFS e DFS devido à sua combinação de eficiência e informações fornecidas pela função heurística.
