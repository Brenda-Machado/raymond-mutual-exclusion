# Implementação Raymond’s mutual exclusion algorithm.

Trabalho da disciplina INE5418, contendo a implementação de uma biblioteca do algoritmo Raymond’s mutual exclusion algorithm.

## Definição do trabalho

1. Criar uma biblioteca que possa ser reutilizada na construção de programas distribuídos, com base no algoritmo de exclusão mútua de Raymond;
2. Desenvolver uma aplicação distribuída para exemplo de uso da biblioteca.

## Como funciona o algoritmo

O algoritmo de Raymond implementa uma exclusão mútua baseada numa estrutura de nodos de uma árvore, em que há o provilégio/permissão de entrar na
região crítica. Um nodo por vez poderá ter o privilégio, o qual é requisitado mandando mensagem para o "holder", o nodo que o requisitante acredita
ter o privilégio no momento, o qual encaminhará o pedido para a fila de requisições. Caso o holder não seja de fato quem tem o privilégio, ele
encaminhará para quem ele acredita que seja. Caso o holder tenha o privilégio, ele o passará (caso tenha terminado sua execução) para o próximo nodo
da fila.

## Como usar a biblioteca

A biblioteca consiste em apenas o arquivo Nodo, que contém a classe Nodo e as principais funções da lógica do algoritmo de raymond. Para utilizá-la
em uma aplicação, é necessário apenas importar a lib para dentro da pasta da sua aplicação e para o file que contém a lógica das permissões dos processos.

Para cada processo que for eventualmente entrar na região crítica, crie um nodo e passe a ele uma queue compartilhada. Caso seja o primeiro nodo,
inicialize ele com um pedido de make_request().

Quando um nodo quiser entrar na região crítica, chame a função make_request(), a qual fará com que ele espere até ter o privilégio. Quando ele sair, 
chame a função exit_critical_section(), a qual dará o privilégio ao próximo da fila.


## Como rodar a aplicação de exemplo

A aplicação de exemplo consiste em uma implementação simples de key/value. Para testá-la, apenas chame o servidor pela pasta principal, ou:

`$ python3 app/servidor.py`

Em seguida, chame o cliente:

`$ python3 cliente.py`

A aplicação lhe dará algumas opções do que fazer, como get uma key ou set uma key. Entretanto, para uma visualização do funcionamento da biblioteca,
Deve criar vários outros clientes e conectar com o servidor, isso pode ser feito por uma VM ou outra máquina, com simples modificações do host.


## Referências

+ [Geeksforgeeks - Raymond’s tree based algorithm](https://www.geeksforgeeks.org/raymonds-tree-based-algorithm/);
+ [Implementation of Raymond's tree based algorithm for Distributed Mutual Exclusion](https://github.com/16priyesh/DME-algorithm);
+ [A simple implementation of Raymond's mutual exclusion algorithm](https://github.com/marcdelacruz/Raymond-s-Algorithm).