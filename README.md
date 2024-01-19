### Cálculo de impacto de um desorganizador

_"As principais transformações da sociedade são causadas por minorias barulhentas"_

----

Programa em python que simula dois tipos de pessoas em uma academia, onde:
- Um tipo é organizada;
- Outro tipo desorganizada

Com isso, o resultado final do programa é a probabilidade de certa quantidade de pessoas desorganizadas na academia poderia causar um "caos".

Ex.: Entre 20 pessoas sendo elas 2 bagunceiras qual a probabilidade que no final do dia a academia vai está desarumada

#### Tipo 1:
- A pessoa organizada guardará o haltere no porta haltere onde ela pegou, ou seja, no lugar certo onde o número do haltere e o porta se coincidem. Mas se caso o lugar em que o equipamento deveria ficar estiver certo ela irá guardar em qualquer outro local que esteja livre;
    
#### Tipo 2:
- O individuo bagunceiro pega o peso, mas ele vai colocar de forma aleatoria em qualquer lugar.

----

#### Estrutura de dados:
        porta_halteres: {
            10: 10,
            12: 12,
            14: 14,
            16: 16,
            ...:...,
        }
