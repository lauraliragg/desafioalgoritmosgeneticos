# Problema da Mochila
Este projeto é a implementação de um algoritmo genético para resolver o problema da mochila, cujo objetivo é maximizar o valor dos itens que podem ser transportados, respeitando uma capacidade de peso limitada.

Funcionamento
Representação dos Cromossomos: Cada cromossomo é representado por uma lista de bits, onde cada bit indica a inclusão ou exclusão de um item na mochila.
População Inicial: Uma população inicial de 150 cromossomos é gerada de forma aleatória.
Avaliação de Aptidão: A aptidão de cada cromossomo é avaliada com base no valor total dos itens selecionados.
Seleção por Roleta: Cromossomos com maior aptidão possuem mais chances de serem escolhidos para reprodução através do método da roleta.
Cruzamento e Mutação: Os cromossomos selecionados passam por cruzamento e mutação, introduzindo variação genética na população.
Iteração: O processo se repete por 50 gerações.
Resultado: O melhor cromossomo encontrado ao final das iterações representa a solução ótima para o problema.

Execução
Com Python instalado em seu sistema. Execute o script com o seguinte comando: python mochila.py

# Minimização de Funções
Este projeto utiliza um algoritmo genético para minimizar a função  aplicando codificação binária e operações genéticas para evoluir as soluções ao longo das gerações.

Funcionamento
Função Objetivo: A função que será minimizada ao longo do processo evolutivo.
Codificação Binária: Os valores de x são representados em binário.
Inicialização: A população inicial é gerada de maneira aleatória.
Seleção por Torneio: Indivíduos são selecionados para reprodução através do método de torneio.
Cruzamento: Indivíduos selecionados são cruzados para gerar novas soluções.
Mutação: Alterações aleatórias são aplicadas aos bits para aumentar a diversidade.
Elitismo: Os melhores indivíduos são preservados de uma geração para outra.
Iterações: O processo evolutivo é repetido por várias gerações até encontrar a solução ideal.

Execução
Com Python instalado em seu sistema. Execute o script com o seguinte comando: python funcao.py