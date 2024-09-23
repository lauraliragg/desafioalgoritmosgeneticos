import numpy as np 
import random

def func(x):
    return x**3 - 6*x + 14

def bin_to_real(bin_str, x_min, x_max):
    return x_min + int(bin_str, 2) * (x_max - x_min) / (2**len(bin_str) - 1)

def real_to_bin(x, x_min, x_max, n_bits):
    return format(int((x - x_min) * (2**n_bits - 1) / (x_max - x_min)), f'0{n_bits}b')

def init_population(pop_size, n_bits, x_min, x_max):
    return [real_to_bin(random.uniform(x_min, x_max), x_min, x_max, n_bits) for _ in range(pop_size)]

def tournament_selection(pop, scores, k=3):
    selected = random.sample(list(zip(pop, scores)), k)
    selected.sort(key=lambda x: x[1])
    return selected[0][0]

def crossover(parent1, parent2, n_points=1):
    if n_points == 1:
        point = random.randint(1, len(parent1) - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    elif n_points == 2:
        point1, point2 = sorted(random.sample(range(1, len(parent1)), 2))
        return (parent1[:point1] + parent2[point1:point2] + parent1[point2:], 
                parent2[:point1] + parent1[point1:point2] + parent2[point2:])

def mutate(bitstring, mutation_rate):
    return ''.join(bit if random.random() > mutation_rate else '1' if bit == '0' else '0' for bit in bitstring)

# Algoritmo genético
def genetic_algorithm(func, x_min, x_max, pop_size=10, n_bits=16, n_generations=100, 
                      mutation_rate=0.01, crossover_points=1, elitism=True, elite_pct=0.1):
    population = init_population(pop_size, n_bits, x_min, x_max)
    best, best_eval = population[0], func(bin_to_real(population[0], x_min, x_max))
    
    for gen in range(n_generations + 1):
        decoded = [bin_to_real(ind, x_min, x_max) for ind in population]
        scores = [func(d) for d in decoded]
        
        if elitism:
            elite_size = int(elite_pct * pop_size)
            elite_indices = np.argsort(scores)[:elite_size]
            elite = [population[i] for i in elite_indices]
        
        selected = [tournament_selection(population, scores) for _ in range(pop_size)]
        children = []
        
        for i in range(0, pop_size, 2):
            parent1, parent2 = selected[i], selected[i+1]
            for c in crossover(parent1, parent2, crossover_points):
                children.append(mutate(c, mutation_rate))
        
        if elitism:
            children = children[:-elite_size] + elite
        
        population = children
        
        for i in range(pop_size):
            decoded = bin_to_real(population[i], x_min, x_max)
            score = func(decoded)
            if score < best_eval:
                best, best_eval = population[i], score
        
        print(f"Generation {gen}, Best: {bin_to_real(best, x_min, x_max)}, Score: {best_eval}")
    
    return bin_to_real(best, x_min, x_max)

x_min, x_max = -10, 10
pop_size = 10
n_bits = 16
n_generations = 100
mutation_rate = 0.01
crossover_points = 1
elitism = True
elite_pct = 0.1

best_x = genetic_algorithm(func, x_min, x_max, pop_size, n_bits, n_generations, 
                           mutation_rate, crossover_points, elitism, elite_pct)

print(f"Melhor valor de x: {best_x}")