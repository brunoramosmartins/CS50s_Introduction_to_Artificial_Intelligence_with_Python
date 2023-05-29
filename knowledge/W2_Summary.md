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