# Week 2: Knowledge

- knowledge-based agents: Agentes fonte que raciocinam operando em representações internas de conhecimento.

    No contexto de AI, os agentes fonte são sistemas computacionais projetados para tomar decisões e realizar tarefaz com base em conhecimento. Esses agentes são capazes de raciocinar e tomar decisões ao operar em representações internas de conhecimento.

    O conhecimento é uma parte essencial da AI, pois permite que os agentes compreendam o mundo, tomem decisões informadas e ajam de maneira inteligente. A representação do conhecimento refere-se à forma como o conhecimento é estruturado e organizado dentro de um sistema computacional.

    Os agentes fonte que operam em representações internas de conhecimento podem utilizar diferentes métodos e técnicas para representar e manipular o conhecimento. Alguns exemplos comuns de representação do conhecimento incluem lógica proposicional, redes semânticas, ontologias e grafos. Essas representações permitem que o agente codifique informações de forma estruturada, facilitando o processo de raciocínio e inferência.

    Ao utilizar essas representações internas de conhecimento, os agentes fonte podem realizar raciocínio lógico e inferência para tirar conclusões, responder a perguntas, resolver problemas e tomar decisões. Eles aplicam regras e princípios lógicos para derivar novas informações a partir do conhecimento existente.

    No geral, os agentes fonte que operam em representações internas de conhecimento são fundamentais para a AI, pois permite que os sistemas compreendam e manipulem informações de maneira inteligente, auxiliando na tomada de decisões e na resolução de problemas complexos.

## Logic

- sentence: uma afirmação sobre o mundo em uma linguagem de representação do conhecimento.
- model: atribuição de um valor de verdade para cada símbolo proposicional (um "mundo possível").
- knowledge base: um conjunto de sentenças conhecidas por um agente baseado em conhecimento.
- entailment (implicação):$$\alpha ⊨ \beta$$ em todo modelo no qual a sentença α é verdadeira,a sentença β também é verdadeira.
- inference: o processo de derivar novas sentenças a partir de sentenças antigas.

## Inference Rules

- Modus Ponens: Modus Ponens é uma forma válida de inferência lógica na qual, se temos uma sentença condicional ("se... então...") e a afirmativa da antecedente, podemos concluir a afirmativa do consequente. Em termos mais simples, é um método de raciocínio que nos permite derivar uma nova sentença a partir de uma sentença condicional e sua premissa verdadeira.

    O Modus Ponens é formalmente definido da seguinte maneira:

    Se A, então B (sentença condicional)
    A (premissa verdadeira)
    Portanto:

    B (conclusão)
    Aqui, "A" representa a antecedente da sentença condicional e "B" representa o consequente. Com base nas premissas, podemos inferir que o consequente "B" também é verdadeiro.

    Vamos ver um exemplo prático:

    If it is raining, then Harry is inside.
    It is raining.
    
    Podemos usar o Modus Ponens para concluir:

    Portanto, Harry is inside.
    
    O Modus Ponens é um exemplo de como a inferência lógica pode ser aplicada para derivar novas sentenças a partir de sentenças antigas, utilizando as regras da lógica e as relações estabelecidas pelas premissas. É uma ferramenta fundamental no raciocínio dedutivo e é amplamente utilizada em diversas áreas da inteligência artificial e da lógica formal.
- And Elimination
- Double Negation Elimination
- Implication Elimination
- Biconditional Elimination
- De Morgan's Law: As Leis de De Morgan são dois princípios fundamentais da lógica que relacionam negações de conjunções e disjunções de proposições. Elas são chamadas de Leis de De Morgan em homenagem ao matemático e lógico britânico Augustus De Morgan, que as formulou.

    Existem duas leis de De Morgan:

    Primeira Lei de De Morgan: A negação de uma conjunção é equivalente à disjunção das negações das proposições individuais.
    Formalmente, a primeira lei de De Morgan pode ser expressa da seguinte maneira:

    $$¬(A ∧ B) ≡ (¬A ∨ ¬B)$$

    Isso significa que a negação de uma conjunção entre A e B é o mesmo que ter a disjunção das negações de A e B separadamente.

    Por exemplo, se considerarmos as proposições A: "Está chovendo" e B: "Está frio", podemos aplicar a primeira lei de De Morgan da seguinte forma:

    $$¬(A ∧ B) ≡ (¬A ∨ ¬B)$$
    ¬(Está chovendo e está frio) ≡ (Não está chovendo ou não está frio)

    Segunda Lei de De Morgan: A negação de uma disjunção é equivalente à conjunção das negações das proposições individuais.
    Formalmente, a segunda lei de De Morgan pode ser expressa da seguinte maneira:

    $$¬(A ∨ B) ≡ (¬A ∧ ¬B)$$

    Isso significa que a negação de uma disjunção entre A e B é o mesmo que ter a conjunção das negações de A e B separadamente.

    Continuando com o exemplo anterior:

    $$¬(A ∨ B) ≡ (¬A ∧ ¬B)$$
    ¬(Está chovendo ou está frio) ≡ (Não está chovendo e não está frio)

    As Leis de De Morgan são ferramentas úteis na simplificação e transformação de expressões lógicas. Elas permitem que expressemos negações de forma alternativa e, muitas vezes, mais conveniente. Essas leis têm aplicações amplas em áreas como matemática, lógica, ciência da computação e projetos de circuitos lógicos.


# Notes

# Knowledge

Os humanos raciocinam com base no conhecimento existente e tiram conclusões. O conceito de representar o conhecimento e tirar conclusões a partir dele também é usado na IA, e nesta palestra vamos explorar como podemos alcançar esse comportamento.

## Knowledge-Based Agents

São agentes que raciocinam operando sobre representações internas do conhecimento.

O que significa “raciocínio baseado no conhecimento para tirar uma conclusão”?

Vamos começar a responder isso com um exemplo de Harry Potter. Considere as seguintes sentenças:

1. Se não chovesse, Harry visitaria Hagrid hoje.
2. Harry visitou Hagrid ou Dumbledore hoje, mas não os dois.
3. Harry visitou Dumbledore hoje.

Com base nessas três frases, podemos responder à pergunta “choveu hoje?”, embora nenhuma das frases individuais nos diga se está chovendo hoje. Aqui está como podemos fazer isso: olhando para a frase 3, sabemos que Harry visitou Dumbledore. Olhando para a frase 2, sabemos que Harry visitou Dumbledore ou Hagrid, e assim podemos concluir

4. Harry não visitou Hagrid.

Agora, olhando para a frase 1, entendemos que se não tivesse chovido, Harry teria visitado Hagrid. No entanto, conhecendo a sentença 4, sabemos que não é esse o caso. Portanto, podemos concluir

5. Choveu hoje.

Para chegar a essa conclusão, usamos a lógica, e a palestra de hoje explora como a IA pode usar a lógica para chegar a novas conclusões com base nas informações existentes.

**Sentence**

Uma frase é uma afirmação sobre o mundo em uma linguagem de representação do conhecimento. Uma frase é como a IA armazena conhecimento e o usa para inferir novas informações.

# Propositional Logic

A lógica proposicional é baseada em proposições, declarações sobre o mundo que podem ser verdadeiras ou falsas, como nas sentenças 1-5 acima.

**Símbolos Proposicionais**

Os símbolos proposicionais geralmente são letras (P, Q, R) usadas para representar uma proposição.

**Conectivos Lógicos**

Conectivos lógicos são símbolos lógicos que conectam símbolos proposicionais para raciocinar de maneira mais complexa sobre o mundo.

- **Not(¬)** inverte o valor de verdade da proposição. Assim, por exemplo, se P: “Está chovendo”, então ¬P: “Não está chovendo”.

As tabelas de verdade são usadas para comparar todas as atribuições de verdade possíveis a proposições. Essa ferramenta nos ajudará a entender melhor os valores de verdade das proposições quando conectadas com diferentes conectivos lógicos. Por exemplo, abaixo está nossa primeira tabela verdade:
<center>

|**P**|**¬P**|
|:-:|:-:|
|false|true|
|true| false|

</center>

- **And (∧)** conecta duas proposições diferentes. Quando essas duas proposições, P e Q, são conectadas por ∧, a proposição resultante P ∧ Q é verdadeira apenas no caso de P e Q serem verdadeiras.

<center>

|**P**|**Q**|**P ∧ Q**|
|:-:|:-:|:-:|
|false|false|false|
|false|true|false|
|true|false|false|
|true|true|true|

</center>

- **Or (∨)** é verdadeiro desde que qualquer um de seus argumentos seja verdadeiro. Isso significa que para P ∨ Q ser verdadeiro, pelo menos um de P ou Q deve ser verdadeiro.

<center>

|**P**|**Q**|**P ∨ Q**|
|:-:|:-:|:-:|
|false|false|false|
|false|true|true|
|true|false|true|
|true|true|true|

</center>

Vale ressaltar que existem dois tipos de Ou: um Ou inclusivo e um Ou exclusivo. Em um Ou exclusivo, P ∨ Q é falso se P ∧ Q é verdadeiro. Ou seja, um Ou exclusivo requer apenas um de seus argumentos para ser verdadeiro e não ambos. Um Ou inclusivo é verdadeiro se qualquer um de P, Q ou P ∧ Q for verdadeiro. No caso de Ou (∨), a intenção é um Ou inclusivo.

---
**Algumas notas laterais não mencionadas na palestra:**

Às vezes, um exemplo ajuda a entender Ou Inclusivo versus Exclusivo.

* Inclusive Ou: “para comer sobremesa tem que limpar o quarto ou cortar a grama”. Nesse caso, se você fizer as duas tarefas, ainda receberá os cookies.

* Exclusivo Ou: “Na sobremesa, você pode comer biscoito ou sorvete.” Nesse caso, você não pode ter os dois.

Se você estiver curioso, o Or exclusivo é geralmente abreviado para XOR e um símbolo comum para ele é ⊕).

---

**Implication (→)** representa uma estrutura de “se P, então Q”. Por exemplo, se P: “Está chovendo” e Q: “Estou dentro de casa”, então P → Q significa “Se está chovendo, então estou dentro de casa”. No caso de P implica Q (P → Q), P é chamado de `antecedente` e Q é chamado de `consequente`.

Quando o antecedente é verdadeiro, a implicação é verdadeira se o consequente também for verdadeiro. Por exemplo, se está chovendo e eu estou dentro de casa, então a sentença "se está chovendo, então estou dentro de casa" é verdadeira. No entanto, quando o antecedente é verdadeiro e o consequente é falso, a implicação é falsa. Por exemplo, se estou fora enquanto chove, então a sentença "se está chovendo, então estou dentro de casa" é falsa.

Por outro lado, quando o antecedente é falso, a implicação é sempre verdadeira, independentemente do consequente. Isso pode ser um conceito confuso. Logicamente, não podemos obter informações úteis de uma implicação (P → Q) se o antecedente (P) for falso. Voltando ao nosso exemplo, se não está chovendo, a implicação não nos diz nada sobre se estou dentro de casa ou não. Eu posso ser alguém que prefere ficar dentro de casa o tempo todo, mesmo quando não está chovendo, ou posso ser alguém que gosta de ficar ao ar livre e passa o tempo todo fora quando não está chovendo. Quando o antecedente é falso, dizemos que a implicação é _trivialmente_ verdadeira.

<center>

|**P**|**Q**|**P → Q**|
|:--:|:--:|:--:|
|false|false|true|
|false|true|true|
|true|false|false|
|true|true|true|

</center>

**Biconditional (↔)** é uma implicação que vai em ambas as direções. Você pode ler como “se e somente se”. P ↔ Q é o mesmo que P → Q e Q → P juntos. Por exemplo, se P: “Está chovendo.” e Q: “Estou dentro de casa”, então P ↔ Q significa que “Se está chovendo, então estou dentro de casa” e “se estou dentro de casa, então está chovendo”. Isso significa que podemos inferir mais do que poderíamos com uma simples implicação. Se P é falso, então Q também é falso; se não está chovendo, a gente sabe que também não estou dentro de casa.

<center>

|**P**|**Q**|**P ↔ Q**|
|:--:|:--:|:--:|
|false|false|true|
|false|true|false|
|true|false|false|
|true|true|true|

</center>

**Modelo**

O modelo é uma atribuição de um valor de verdade para cada proposição. Para reiterar, as proposições são declarações sobre o mundo que podem ser verdadeiras ou falsas. No entanto, o conhecimento sobre o mundo está representado nos valores de verdade dessas proposições. O modelo é a atribuição de valor de verdade que fornece informações sobre o mundo.

Por exemplo, se P: “Está chovendo.” e Q: “É terça-feira.”, um modelo poderia ser a seguinte atribuição de valor de verdade: {P = Verdadeiro, Q = Falso}. Este modelo significa que está chovendo, mas não é terça-feira. No entanto, existem mais modelos possíveis nesta situação (por exemplo, {P = Verdadeiro, Q = Verdadeiro}, onde está chovendo e uma terça-feira). De fato, o número de modelos possíveis é 2 elevado ao número de proposições. Neste caso, tínhamos 2 proposições, portanto $2²=4$ modelos possíveis.

**Base de conhecimento (KB)**

A base de conhecimento é um conjunto de sentenças conhecidas por um agente baseado em conhecimento. Este é o conhecimento que a IA fornece sobre o mundo na forma de sentenças lógicas proposicionais que podem ser usadas para fazer inferências adicionais sobre o mundo.

**Entailment (⊨)**

Se α ⊨ β (α Entailment β), então em qualquer mundo onde α é verdadeiro, β também é verdadeiro.

Por exemplo, se α: “É uma terça-feira em janeiro” e β: “É uma terça-feira”, então sabemos que α ⊨ β. Se é verdade que é terça-feira em janeiro, também sabemos que é terça-feira. Entailment é diferente de implication. implication é um conectivo lógico entre duas proposições. O Entailment, por outro lado, é uma relação que significa que se toda a informação em α for verdadeira, então toda a informação em β é verdadeira.

# Inference

A inferência é o processo de derivar novas sentenças de antigas.

Por exemplo, no exemplo anterior de Harry Potter, as sentenças 4 e 5 foram inferidas das sentenças 1, 2 e 3.

Existem várias maneiras de inferir novos conhecimentos com base no conhecimento existente. Primeiro, vamos considerar o algoritmo `Model Checking`.

- Para determinar se KB ⊨ α (em outras palavras, respondendo à pergunta: “podemos concluir que α é verdadeiro com base em nossa base de conhecimento”)

    - Enumere todos os modelos possíveis.
    -   Se em todo modelo onde KB é verdadeiro, α também é verdadeiro, então KB implica α (KB ⊨ α).

Considere o seguinte exemplo:

P: É uma terça-feira. P: Está chovendo. R: Harry vai correr. KB: (P ∧ ¬Q) → R (em palavras, P e não Q implica R) P (P é verdadeiro) ¬Q (Q é falso) Questão: R (Queremos saber se R é verdadeiro ou falso; KB ⊨ R?)

Para responder à consulta usando o algoritmo Model Checking, enumeramos todos os modelos possíveis.

<center>

|   P  |   Q  |   R  |  KB  | 
| :--: | :--: | :--: | :--: |   
| false| false| false|      |  	 
| false| false| true | 	    |  
| false| true | false| 	    |  
| false| true | true | 	    |  
| true | false| false| 	    |  
| true | false| true | 	    |  
| true | true | false| 	    |  
| true | true | true | 	    |

</center>

Em seguida, examinamos todos os modelos e verificamos se são verdadeiros em nossa Base de Conhecimento.

Primeiro, em nosso KB, sabemos que P é verdadeiro. Assim, podemos dizer que o KB é falso em todos os modelos onde P não é verdadeiro.

<center>

|   P  |   Q  |   R  |  KB  | 
| :--: | :--: | :--: | :--: |   
| false| false| false| false|
| false| false| true | false|  
| false| true | false| false|  
| false| true | true | false|  
| true | false| false| 	    |  
| true | false| true | 	    |  
| true | true | false| 	    |  
| true | true | true | 	    |

</center>

Em seguida, da mesma forma, em nosso KB, sabemos que Q é falso. Assim, podemos dizer que o KB é falso em todos os modelos onde Q é verdadeiro.

<center>

|   P  |   Q  |   R  |  KB  | 
| :--: | :--: | :--: | :--: |   
| false| false| false| false|
| false| false| true | false|  
| false| true | false| false|  
| false| true | true | false|  
| true | false| false| 	    |  
| true | false| true | 	    |  
| true | true | false| false|  
| true | true | true | false|

</center>

Por fim, ficamos com dois modelos. Em ambos, P é verdadeiro e Q é falso. Em um modelo R é verdadeiro e no outro R é falso. Devido a (P ∧ ¬Q) → R estar em nosso KB, sabemos que no caso em que P é verdadeiro e Q é falso, R deve ser verdadeiro. Assim, dizemos que nosso KB é falso para o modelo em que R é falso e verdadeiro para o modelo em que R é verdadeiro.

|   P  |   Q  |   R  |  KB  | 
| :--: | :--: | :--: | :--: |   
| false| false| false| false|
| false| false| true | false|  
| false| true | false| false|  
| false| true | true | false|  
| true | false| false| <span style="color:red">**false**</span>   |  	    |  
| true | false| true | <span style="color:green">**true**</span>   |  
| true | true | false| false|  
| true | true | true | false|

Olhando para esta tabela, há apenas um modelo onde nossa base de conhecimento é verdadeira. Neste modelo, vemos que R também é verdadeiro. Pela nossa definição de implicação, se R é verdadeiro em todos os modelos onde o KB é verdadeiro, então KB ⊨ R.

Em seguida, vamos ver como o conhecimento e a lógica podem ser representados como código.

```Python

from logic import *

# Create new classes, each having a name, or a symbol, representing each proposition.
rain = Symbol("rain")  # It is raining.
hagrid = Symbol("hagrid")  # Harry visited Hagrid
dumbledore = Symbol("dumbledore")  # Harry visited Dumbledore

# Save sentences into the KB
knowledge = And(  # Starting from the "And" logical connective, becasue each proposition represents knowledge that we know to be true.

    Implication(Not(rain), hagrid),  # ¬(It is raining) → (Harry visited Hagrid)

    Or(hagrid, dumbledore),  # (Harry visited Hagrid) ∨ (Harry visited Dumbledore).

    Not(And(hagrid, dumbledore)),  # ¬(Harry visited Hagrid ∧ Harry visited Dumbledore) i.e. Harry did not visit both Hagrid and Dumbledore.

    dumbledore  # Harry visited Dumbledore. Note that while previous propositions contained multiple symbols with connectors, this is a proposition consisting of one symbol. This means that we take as a fact that, in this KB, Harry visited Dumbledore.
    )

```

Para executar o algoritmo de verificação de modelo, são necessárias as seguintes informações:

- Base de conhecimento, que será usada para fazer inferências
- Uma consulta, ou a proposição que nos interessa se é implicada pela KB
- Símbolos, uma lista de todos os símbolos (ou proposições atômicas) usados (no nosso caso, são chuva, hagrid e dumbledore)
- Modelo, uma atribuição de valores verdadeiros e falsos a símbolos

O algoritmo de verificação do modelo é o seguinte:

```Python

def check_all(knowledge, query, symbols, model):

    # If model has an assignment for each symbol
    # (The logic below might be a little confusing: we start with a list of symbols. The function is recursive, and every time it calls itself it pops one symbol from the symbols list and generates models from it. Thus, when the symbols list is empty, we know that we finished generating models with every possible truth assignment of symbols.)
    if not symbols:

        # If knowledge base is true in model, then query must also be true
        if knowledge.evaluate(model):
            return query.evaluate(model)
        return True
    else:

        # Choose one of the remaining unused symbols
        remaining = symbols.copy()
        p = remaining.pop()

        # Create a model where the symbol is true
        model_true = model.copy()
        model_true[p] = True

        # Create a model where the symbol is false
        model_false = model.copy()
        model_false[p] = False

        # Ensure entailment holds in both models
        return(check_all(knowledge, query, remaining, model_true) and check_all(knowledge, query, remaining, model_false))

```

Observe que estamos interessados apenas nos modelos em que o KB é verdadeiro. Se o KB for falso, então as condições que sabemos serem verdadeiras não estão ocorrendo nesses modelos, tornando-os irrelevantes para o nosso caso.

---

>Um exemplo de palestra externa: Let P: Harry joga como apanhador, Q: Oliver joga como goleiro, R: Grifinória vence. Nosso KB especifica que P Q (P ∧ Q) → R. Em outras palavras, sabemos que P é verdadeiro, ou seja, Harry joga como apanhador, e que Q é verdadeiro, ou seja, Oliver joga como goleiro, e que se P e Q são verdadeiros, então R também é verdadeiro, o que significa que a Grifinória venceu a partida. Agora imagine um modelo onde Harry jogava como batedor em vez de apanhador (portanto, Harry não jogava como apanhador, ¬P). Bem, neste caso, não nos importa se a Grifinória ganhou (se R é verdadeiro ou não), porque temos a informação em nosso KB de que Harry jogou como apanhador e não como batedor. Estamos interessados apenas nos modelos em que, como no nosso caso, P e Q são verdadeiros.)

---

Além disso, a forma como a função `check_all` funciona é recursiva. Ou seja, ele pega um símbolo, cria dois modelos, em um o símbolo é verdadeiro e no outro o símbolo é falso, e então chama a si mesmo novamente, agora com dois modelos que diferem pela atribuição de verdade deste símbolo. A função continuará fazendo isso até que todos os símbolos tenham seus valores de verdade atribuídos nos modelos, deixando a lista de símbolos vazia. Uma vez vazio (conforme identificado pela linha, se não símbolos), em cada instância da função (em que cada instância contém um modelo diferente), a função verifica se o KB é verdadeiro dado o modelo. Se a KB for verdadeira neste modelo, a função verifica se a consulta é verdadeira, conforme descrito anteriormente.

# Knowledge Engineering

A engenharia do conhecimento é o processo de descobrir como representar proposições e lógica na IA.

Vamos praticar a engenharia do conhecimento usando o jogo Clue.

No jogo, um assassinato foi cometido por uma pessoa, utilizando uma ferramenta em um local. Pessoas, ferramentas e locais são representados por cartas. Uma carta de cada categoria é escolhida aleatoriamente e colocada em um envelope, cabendo aos participantes desvendar o mistério. Os participantes o fazem descobrindo cartas e deduzindo dessas pistas o que deve estar no envelope. Usaremos o algoritmo de Verificação de modelo anterior para desvendar o mistério. Em nosso modelo, marcamos como `Verdadeiros` os itens que sabemos que estão relacionados ao assassinato e `Falsos` caso contrário.

Para nossos propósitos, suponha que temos três pessoas: Mustard, Plum e Scarlet, três ferramentas: faca, revólver e chave inglesa e três locais: salão de baile, cozinha e biblioteca.

Podemos começar a criar nossa base de conhecimento adicionando as regras do jogo. Sabemos com certeza que uma pessoa é o assassino, que uma ferramenta foi usada e que o assassinato aconteceu em um local. Isso pode ser representado na lógica proposicional da seguinte maneira:

(Mustard ∨ Plum ∨ Scarlet)

(knife ∨ revolver ∨ wrench)

(ballroom ∨ kitchen ∨ library)

O jogo começa com cada jogador vendo uma pessoa, uma ferramenta e um local, sabendo assim que não estão relacionados ao assassinato. Os jogadores não compartilham as informações que viram nessas cartas. Suponha que nosso jogador receba as cartas Mostarda, cozinha e revólver. Assim, sabemos que estes não estão relacionados ao assassinato e podemos adicionar ao nosso KB

¬(Mustard)

¬(kitchen)

¬(revolver)

Em outras situações do jogo, pode-se dar um palpite, sugerindo uma combinação de pessoa, ferramenta e local. Suponha que o palpite seja que Scarlet usou uma chave inglesa para cometer o crime na biblioteca. Se esse palpite estiver errado, o seguinte pode ser deduzido e adicionado ao KB:

(¬Scarlet ∨ ¬biblioteca ∨ ¬chave)

Agora, suponha que alguém nos mostre o cartão Plum. Assim, podemos adicionar

¬(Plum)

ao nosso KB.

Neste ponto, podemos concluir que o assassino é Scarlet, já que tem que ser um dos Mustard, Plum e Scarlet, e temos evidências de que os dois primeiros não são.

Acrescentar apenas mais um conhecimento, por exemplo, de que não é o salão de baile, pode nos dar mais informações. Primeiro, atualizamos nosso KB

¬(ballroom)

E agora, usando vários dados anteriores, podemos deduzir que Scarlet cometeu o assassinato com uma faca na biblioteca. Podemos deduzir que é a biblioteca porque tem que ser o salão de baile, a cozinha ou a biblioteca, e os dois primeiros provaram não ser os locais. No entanto, quando alguém adivinhou Scarlet, biblioteca, chave inglesa, o palpite foi falso. Assim, pelo menos um dos elementos nesta declaração tem que ser falso. Como sabemos que Scarlet e a biblioteca são verdadeiras, sabemos que a chave inglesa é a parte falsa aqui. Como um dos três instrumentos tem que ser verdadeiro, e não é a chave nem o revólver, podemos concluir que é a faca.

Aqui está como as informações seriam adicionadas à base de conhecimento em Python:

```Python

# Add the clues to the KB
knowledge = And(

    # Start with the game conditions: one item in each of the three categories has to be true.
    Or(mustard, plum, scarlet),
    Or(ballroom, kitchen, library),
    Or(knife, revolver, wrench),

    # Add the information from the three initial cards we saw
    Not(mustard),
    Not(kitchen),
    Not(revolver),

    # Add the guess someone made that it is Scarlet, who used a wrench in the library
    Or(Not(scarlet), Not(library), Not(wrench)),

    # Add the cards that we were exposed to
    Not(plum),
    Not(ballroom)
)

```

Também podemos olhar para outros quebra-cabeças lógicos. Considere o seguinte exemplo: quatro pessoas diferentes, Gilderoy, Pomona, Minerva e Horace, são designadas para quatro casas diferentes, Grifinória, Lufa-Lufa, Corvinal e Sonserina. Há exatamente uma pessoa em cada casa. Representar as condições do quebra-cabeça na lógica proposicional é bastante complicado. Primeiro, cada uma das atribuições possíveis terá que ser uma proposição em si: MinervaGryffindor, MinervaHufflepuff, MinervaRavenclaw, MinervaSlytherin, PomonaGryffindor…

Em segundo lugar, para representar que cada pessoa pertence a uma casa, é necessária uma declaração Or com todas as possíveis atribuições de casas por pessoa

(MinervaGryffindor ∨ MinervaHufflepuff ∨ MinervaRavenclaw ∨ MinervaSlytherin), repeat for every person.

Then, to encode that if one person is assigned to one house, they are not assigned to the other houses, we will write

(MinervaGryffindor → ¬MinervaHufflepuff) ∧ (MinervaGryffindor → ¬MinervaRavenclaw) ∧ (MinervaGryffindor → ¬MinervaSlytherin) ∧ (MinervaHufflepuff → ¬MinervaGryffindor)…

e assim por diante para todas as casas e todas as pessoas. Uma solução para essa ineficiência é oferecida na seção sobre lógica de primeira ordem. No entanto, esse tipo de enigma ainda pode ser resolvido com qualquer tipo de lógica, com dicas suficientes.

Outro tipo de quebra-cabeça que pode ser resolvido usando a lógica proposicional é o jogo Mastermind. Neste jogo, o jogador um organiza as cores em uma determinada ordem e, em seguida, o jogador dois deve adivinhar essa ordem. A cada turno, o jogador dois dá um palpite e o jogador um devolve um número, indicando quantas cores o jogador dois acertou. Vamos simular um jogo com quatro cores. Suponha que o jogador dois sugira a seguinte ordem:

$${red, blue, green, yellow}$$

O jogador um responde “dois”. Assim, sabemos que duas das cores estão na posição correta e as outras duas estão no lugar errado. Com base nessas informações, o jogador dois tenta trocar as localizações de duas cores.

$${blue, red, green, yellow}$$

Agora o jogador um responde “zero”. Assim, o jogador dois sabe que as cores trocadas estavam no local certo inicialmente, o que significa que as duas cores intocadas estavam no local errado. O jogador dois os troca.

$${red, blue, yellow, green}$$

O jogador um diz “quatro” e o jogo acaba.

Representar isso na lógica proposicional exigiria que tivéssemos (número de cores)² proposições atômicas. Assim, no caso de quatro cores, teríamos as proposições red0, red1, red2, red3, blue0... representando cor e posição. O próximo passo seria representar as regras do jogo em lógica proposicional (que há apenas uma cor em cada posição e nenhuma cor se repete) e adicioná-las à KB. A etapa final seria adicionar todas as sugestões que temos à KB. No nosso caso, acrescentaríamos que, no primeiro palpite, duas posições estavam erradas e duas corretas, e no segundo palpite, nenhuma estava certa. Usando esse conhecimento, um algoritmo de Verificação de Modelo pode nos dar a solução para o quebra-cabeça.

# Inference Rules

A verificação de modelo não é um algoritmo eficiente porque tem que considerar todos os modelos possíveis antes de dar a resposta (um lembrete: uma consulta R é verdadeira se sob todos os modelos (atribuições de verdade) onde o KB é verdadeiro, R também é verdadeiro). As regras de inferência nos permitem gerar novas informações com base no conhecimento existente sem considerar todos os modelos possíveis.

As regras de inferência são geralmente representadas por uma barra horizontal que separa a parte superior, a premissa, da parte inferior, a conclusão. A premissa é qualquer conhecimento que tenhamos, e a conclusão é o conhecimento que pode ser gerado com base na premissa.

<center>

**If is raining, then Harry is inside.**

**It is raining.**

---

**Harry is inside.**
</center>

Neste exemplo, nossa premissa consiste nas seguintes proposições:

- Se estiver chovendo, então Harry está dentro.
- Está chovendo.

Com base nisso, a maioria dos humanos razoáveis pode concluir que

- Harry está lá dentro.

**Modus ponens**

O tipo de regra de inferência que usamos neste exemplo é Modus Ponens, que é uma maneira sofisticada de dizer que, se soubermos que uma implicação e seu antecedente são verdadeiros, então o consequente também é verdadeiro.

<center>

**$\alpha \rightarrow \beta$**

**$\alpha$**

---

**$\beta$**
</center>

**And Elimination**

If an And proposition is true, then any one atomic proposition within it is true as well. For example, if we know that Harry is friends with Ron and Hermione, we can conclude that Harry is friends with Hermione.

<center>

**$\alpha ∧ \beta$**

---

**$\alpha$**
</center>


**Double Negation Elimination**

A proposition that is negated twice is true. For example, consider the proposition “It is not true that Harry did not pass the test”. We can parse it the following way: “It is not true that (Harry did not pass the test)”, or “¬(Harry did not pass the test)”, and, finally “¬(¬(Harry passed the test)).” The two negations cancel each other, marking the proposition “Harry passed the test” as true.

<center>

**$¬(¬\alpha)$**

---

**$\alpha$**

</center>

**Implication Elimination**

An implication is equivalent to an Or relation between the negated antecedent and the consequent. As an example, the proposition “If it is raining, Harry is inside” is equivalent to the proposition “(it is not raining) or (Harry is inside).”

<center>

**$\alpha \rightarrow \beta$**

---

**$¬\alpha∨\beta$**

</center>

