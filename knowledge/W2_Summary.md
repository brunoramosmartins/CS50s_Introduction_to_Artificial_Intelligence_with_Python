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
|:-|:-:|
|false|true|
|true| false|

</center>

- **And (∧)** conecta duas proposições diferentes. Quando essas duas proposições, P e Q, são conectadas por ∧, a proposição resultante P ∧ Q é verdadeira apenas no caso de P e Q serem verdadeiras.

<center>

|**P**|**Q**|**P ∧ Q**|
|:-|:-|:-:|
|false|false|false|
|false|true|false|
|true|false|false|
|true|true|true|

</center>

- **Or (∨)** é verdadeiro desde que qualquer um de seus argumentos seja verdadeiro. Isso significa que para P ∨ Q ser verdadeiro, pelo menos um de P ou Q deve ser verdadeiro.

<center>

|**P**|**Q**|**P ∨ Q**|
|:-|:-|:-:|
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
|:-|:-|:-:|
|false|false|true|
|false|true|true|
|true|false|false|
|true|true|true|

</center>

**Biconditional (↔)** é uma implicação que vai em ambas as direções. Você pode ler como “se e somente se”. P ↔ Q é o mesmo que P → Q e Q → P juntos. Por exemplo, se P: “Está chovendo.” e Q: “Estou dentro de casa”, então P ↔ Q significa que “Se está chovendo, então estou dentro de casa” e “se estou dentro de casa, então está chovendo”. Isso significa que podemos inferir mais do que poderíamos com uma simples implicação. Se P é falso, então Q também é falso; se não está chovendo, a gente sabe que também não estou dentro de casa.

<center>

|**P**|**Q**|**P ↔ Q**|
|:-|:-|:-:|
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