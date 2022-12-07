# stamps-challenge

**Desafio dos Selos - Disciplina Matemática Discreta**

 - O arquivo contendo a explicação do exercício está anexado ao repositório.
 
 *A matemática possui ferramentas que podem ser utilizadas para resolver problemas. Juntamente com a implementação de uma linguagem de programação, é possivel utilizar da matemática discreta de forma a apresentar ao usuário uma possível solução.*
 
 **1.1 Descrição do Desafio**<br/>
 Utilizando dois selos contendo dois valores diferentes, é possível representar uma sequência de números utilizando esses valores, a partir de algum numero existente.
 Por exemplo, com o número 2 e 5 é possivel representar qualquer número N, N+1, N+2 até o infinito. Mas isso só é possível a partir de algum número existente, que ao provarmos por indução matemática, chamamos de "Passo Base". Continuando com o exemplo, com os números 2 e 5, podemos formar o número 2 (1.2 + 0.5) mas não podemos formar o número 3, mas a partir do 4 em diante, todos os números podem ser representados por 2 e 5.
 
| **Número** | **Representação** |
| ------------- | ------------- |
| **4** | [2][2]  |
| **5** | [5] |
| **6**| [2][2][2]  |
| **7** | [5][2]  |
| **8** | [2][2][2][2]  |
| ... | ...  |
| **16**  | [5][5][2][2][2] |
| **17**  | [5][5][5][2] |
| ... | ...  |

E isto segue até o infinito.</br>

**1.2 Descrição do Algorítimo**<br/>
O usuário irá inserir dois valores inteiros A e B, e o algoritimo deverá, retornar ao usuário:</br>
 (1) A partir de qual número a preposição é válida.</br>
 (2) Como representar o primeiro valor da preposição a partir de A e B</br>
 (3) Passos para continuar representando os números em sequência</br>

**[Exemplos]**</br>

**Entrada:** 4 7</br>
**Saída:**</br>
A proposição é verdadeira a partir de 18 centavos.</br>
O valor 18 centavos pode ser feito usando 2 selo(s) de 7 centavos e 1 selo(s) de 4 centavos.</br>
Troque 1 selo(s) de 7 centavos por 2 selo(s) de 4 centavos ou Troque 5 selo(s) de 4 centavos por 3 selo(s) de 7 centavos</br>

**Entrada:** 3 5</br>
**Saída:**</br>
A proposição é verdadeira a partir de 8 centavos.</br>
O valor 8 centavos pode ser feito usando 1 selo(s) de 3 centavos e 1 selo(s) de 5 centavos.</br>
Troque 1 selo(s) de 5 centavos por 2 selo(s) de 3 centavos ou Troque 3 selo(s) de 3 centavos por 2 selo(s) de 5 centavos</br>

**Entrada:** 8 9</br>
**Saída:**</br>
A proposição é verdadeira a partir de 56 centavos.</br>
O valor 56 centavos pode ser feito usando 7 selo(s) de 8 centavos e 0 selo(s) de 9 centavos.</br>
Troque 1 selo(s) de 8 centavos por 1 selo(s) de 9 centavos ou Troque 7 selo(s) de 9 centavos por 8 selo(s) de 8 centavos</br>

**2.0 Solução Abordada**<br/>
Para tratar dos dois números, que chamaremos de A e B, iremos primeiro, ressaltar alguns casos onde o desafio não é possível ou não é viável:</br>

**01.** Se A ou B for igual a 0, já que com um dos selos tendo valor 0, só podemos utilizar o outro, o que impossbilita o desafio (exceto quando esse outro selo tiver o valor 1).</br>

**02.** Se A ou B for igual a 1, nesse caso o desafio há solução, mas é utilizar o selo 1 e adcionar 1 em todos os casos, ou seja, uma solução padrão que foge do objetivo do desafio.</br>

**03.** A e B possuem divisor comum diferente de 1: Para representar os números com dois selos diferentes, A e B devem ser primos entre si, isso significa que: Dois numeros pares não torna isso possível, como iremos representar um numero impar utilizando dois números pares? Da mesma forma números como: (5 e 10), (3 e 6), (7, 21) cumprir com esse requisito pois possuem divisor comum diferente de zero, (5, 3 e 3).</br>

**04.** A e B não podem ser números iguais.</br>

**2.1 Determinando o Padrão**</br>
O primeiro passo a ser criado por mim, foi determinar o padrão utilizado para dois números A e B, isso antes mesmo de conseguir determinar sua base, pois a lógica por trás desse Padrão é independente. Para isso, é preciso encontrar um número que atenda a seguinte fórmula:</br>

*X1.A - Y1.B = -1*</br>
*X2.B - Y2.A = -1*</br>
</br>
Cada uma dessas fórmulas representa cada uma das instruções, lembrando que A é sempre o maior número, e o algorítimo garante isso não importa a ordem que o usuário insir. Veremos um exemplo para entender melhor:</br>

O usuário insere os números 4 e 7, substituindo na fórmula, temos:</br>

*X1.7 - Y1.4 = -1*</br>
*X2.4 - Y2.7 = -1*</br>
</br>
Neste caso, precisamos achar os menores números X1, Y1, X2, Y2 que solucionem essa equação. Os laços "while" na função "definir_passos()" fazem exatamente isso, percorrendo as possbilidades e usando uma analogia de "checkpoint" para diminuir a complexidade do algorítimo (Se eu sei que X.A >Y.B, logo sei que (X+1).A>Y.B, então não preciso analizar Y novamente).</br>
No caso do exemplo demonstrado, os valores são:</br>

**1**.7 - **2**.4 = -1</br>
**5**.4 - **3**.7 = -1</br>

Ao organizar os dados, o resultado final seria:</br>

*Troque 1 selo(s) de 7 centavos por 2 selo(s) de 4 centavos ou Troque 5 selo(s) de 4 centavos por 3 selo(s) de 7 centavos</br>*

**2.2 Deteminando Valor Base**<br/>

Após resolver um dos problemas, iremos encontrar uma fórmula de determinar qual o valor inicial da sequencia que pode ser formada utilizando dois números A e B:</br>
Tentando explicar minha analogia, tendo dois números A e B, sabemos que o algoritimo define A como o maior algoríotimo, logo eu determinei que B seria o principal número para determinar o valor inicial, para isso, consegui determinar matemáticamente como resolver esse problema:</br>
</br>
Para isso chegamos em uma observação importante, se eu possuo dois números A e B, na qual A>B, o valor inicial da sequencia (a qual chamarei de base) aumentará de forma igual a cada vez que A aumentará, por exemplo, a base de 5 e 6 é 20, enquanto a base de 5 e 7 é 24, enquanto a base de 5 e 8 é 28, percebe um padrão? A medida de que A aumenta,  diferença entre a base anterior é 4, e esse padrão pode ser diferente dependendo do valor de B, mas consegui determinar uma fórmula que estabelece esse padrão:</br>

Chamaremos D de Diferença, na qual **D = B - 1**, no caso de **B = 5**, **B = 5 - 1 = 4**.</br>

Chamaremos de I o valor a qual será incrementado **D**, a fórmula que representa I é:</br>
I = B.(B-1)-(B-1)</br> Podemos simplifica-la da seguinte forma:</br>
I = B.D-D</br>
I = D(B-1)</br>
I = D(D)</br>
I = D²</br>

Agora precisamos saber quantas vezes iremos incrementar o valor de D em I, exemplificado pela seguinte fórmula:</br>
P(1) = I + D(A-B)</br>
P(1) = D² + D(A-B)</br>

Posso demonstrar em outro momento as aplicações matemáticas e observações utilziadas para chegar neste resultado.</br> Agora um exemplo:</br>
Os números 4 e 7.</br>
D = 4 - 1 = 3</br>
3² + 3(7-3) = 9 + 9 = 18</br>

O número base utilizando os selos 4 e 7 é o número 18, a partir dele, você consegue representar qualquer número utilizando 4 e 7.</br>


**2.3 Como representar valor Base**<br/>
Para descobrir como representar o valor base, o algoritimo encontra a solução para a equação: X.A + Y.B = P(1)





