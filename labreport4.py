import random

def fitness(chromosome):
    conflicts = 0
    n = len(chromosome)
    for i in range(n):
        for j in range(i + 1, n):
            if chromosome[i] == chromosome[j] or \
               abs(chromosome[i] - chromosome[j]) == abs(i - j):
                conflicts += 1
    return conflicts


def generate_population(size, n):
    population = []
    for _ in range(size):
        chromosome = list(range(n))
        random.shuffle(chromosome)
        population.append(chromosome)
    return population


def selection(population):
    population.sort(key=lambda x: fitness(x))
    return population[:2]


def crossover(parent1, parent2):
    n = len(parent1)
    point = random.randint(0, n - 1)
    child = parent1[:point] + [x for x in parent2 if x not in parent1[:point]]
    return child


def mutate(chromosome):
    i, j = random.sample(range(len(chromosome)), 2)
    chromosome[i], chromosome[j] = chromosome[j], chromosome[i]


def genetic_algorithm(n, population_size=100, generations=1000):
    population = generate_population(population_size, n)

    for _ in range(generations):
        population.sort(key=lambda x: fitness(x))
        if fitness(population[0]) == 0:
            return population[0]

        parent1, parent2 = selection(population)
        child = crossover(parent1, parent2)
        mutate(child)
        population.append(child)

    return None


n = int(input("Enter number of queens: "))
solution = genetic_algorithm(n)

if solution:
    print("Solution Found:")
    print(solution)
else:
    print("No solution found")
