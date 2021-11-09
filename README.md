## Índice
* [Descrição](#descricao)
* [Instalação](#instalacao)
* [Execução](#execucao)
* [Testes](#testes)


## Descrição
Trabalho 2 da disciplina CI1238 - Otimização, no semestre 2021/1.  
[Especificação do projeto](docs/especificacao.pdf).  
[Relatório](docs/texto.pdf).
	
## Instalação
Para instalar dependências e gerar o executável `./quimica`
```
make
```
	
## Execução
O programa recebe da entrada padrão o seguinte:

> Inicia com três números, n, m e c, que são, respectivamente, o némero de itens, o némero de pares proibidos, e a capacidade da mochila. Em seguida temos 2 linhas, cada uma com n némeros. Na primeira destas linhas temos o peso e na segunda temos os valores dos ıtens, numerados de 1 a n (e na mesma ordem).Logo após, temos m linhas, cada uma com dois números, i e j, representando dois itens que não podem estar juntos na mochila.

```
./quimica < arquivo_de_teste
```

## Testes
O script `./quimica.sh` aplica o make depois realiza testes com os arquivos dentro da pasta [/testes](/testes)

```
./quimica.sh
```