import random
import string
import time

m = 100
sample = string.ascii_lowercase + ' '
mating_pool = []
mutation = 0.01
average: float = 0

print("Gli l'output è tutto in minuscolo \n")

class attempt:
    def __init__(self, dna=None, objective=None):
        if dna is None:
            dna = list("".join(random.choice(sample) for _ in range(len(objective))))

        self.dna = dna

        for h in range(len(objective)):
            if random.random() < mutation:
                self.dna[h] = random.choice(sample)

        counter = 0
        for i in range(len(objective)):
            if objective[i] == self.dna[i]:
                counter += 1

        self.fitness = pow(counter / len(objective), 4) * 100

        if self.fitness < average:
            for h in range(len(objective)):
                if random.random() < mutation:
                    self.dna[h] = random.choice(sample)


def selection(best, population):
    high = 0
    average = 0
    for boys in population:
        average += boys.fitness
        if boys.fitness > high:
            high = boys.fitness
            if boys.fitness > best.fitness:
                best.fitness = boys.fitness
                best.dna = boys.dna.copy()

    average /= len(population)

    for thing in population:
        thing.fitness /= high

    mating_pool.clear()

    for guess in population:
        n = int(guess.fitness * 100)
        for j in range(n):
            mating_pool.append(guess)


def reproduction(population, objective):
    population.clear()

    for k in range(m):
        a = random.choice(mating_pool).dna.copy()
        b = random.choice(mating_pool).dna.copy()

        population.append(attempt(a[:int(len(a))] + b[int(len(b)):], objective))


def to_string(lis):
    return "".join(lis[w] for w in range(len(lis)))


def run(best, population, objective):
    count = 0
    while best.dna[:] != objective[:]:
        selection(best, population)
        reproduction(population, objective)
        count += 1
        print(to_string(best.dna) + "  >  generazione " + str(count))


def choice():
    objective = input("Frase da indovinare (non troppo lunga eh) > ")
    objective = objective.lower()
    objective = list(objective)
    population = [attempt(None, objective) for _ in range(m)]
    best = attempt(None, objective)
    best.fitness = 0
    run(best, population, objective)
    print("\n")


choice()

while input("Continuare? (y/n) > ") == "y":
    choice()

print("Arrivederci")
time.sleep(0.5)
