import random

def calcula_fitness(mochila, pesos_e_valores):
    valor_total = 0
    peso_total = 0
    for i in range(len(mochila)):
        if mochila[i] == 1:
            peso_total += pesos_e_valores[i][0]
            valor_total += pesos_e_valores[i][1]
    return valor_total if peso_total <= peso_maximo else 0

def cria_populacao_inicial(tamanho_populacao, tamanho_cromossomo):
    return [[random.randint(0, 1) for _ in range(tamanho_cromossomo)] for _ in range(tamanho_populacao)]

def selecao_roleta(populacao, fitness):
    max_fitness = sum(fitness)
    pick = random.uniform(0, max_fitness)
    current = 0
    for i in range(len(populacao)):
        current += fitness[i]
        if current > pick:
            return populacao[i]

def cruzamento(pai1, pai2):
    ponto_corte = random.randint(1, len(pai1) - 1)
    filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
    filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]
    return filho1, filho2

def mutacao(individuo, taxa_mutacao):
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao:
            individuo[i] = 1 if individuo[i] == 0 else 0
    return individuo

pesos_e_valores = [[2, 10], [4, 30], [6, 300], [8, 10], [8, 30], [8, 300], [12, 50], [25, 75], [50, 100], [100, 400]]
peso_maximo = 100
numero_de_cromossomos = 150
geracoes = 50
taxa_mutacao = 0.01

populacao = cria_populacao_inicial(numero_de_cromossomos, len(pesos_e_valores))

melhores_individuos = []
for geracao in range(geracoes):
    fitness = [calcula_fitness(individuo, pesos_e_valores) for individuo in populacao]
    nova_populacao = []
    for _ in range(numero_de_cromossomos // 2):
        pai1 = selecao_roleta(populacao, fitness)
        pai2 = selecao_roleta(populacao, fitness)
        filho1, filho2 = cruzamento(pai1, pai2)
        nova_populacao.append(mutacao(filho1, taxa_mutacao))
        nova_populacao.append(mutacao(filho2, taxa_mutacao))
    populacao = nova_populacao
    melhor_individuo = max(populacao, key=lambda ind: calcula_fitness(ind, pesos_e_valores))
    melhores_individuos.append([calcula_fitness(melhor_individuo, pesos_e_valores), melhor_individuo])

print(f"Melhores individuos: {melhores_individuos}")
print(f"Melhor individuo: {melhor_individuo}")
print(f"Pesos: {pesos_e_valores}")