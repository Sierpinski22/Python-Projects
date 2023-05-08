import matplotlib.pyplot as plt
from random import choice, random

evalFitness = lambda p, t: sum([1 for i, e in enumerate(list(p)) if e == t[i]])
crossover = lambda s1, s2: s1[:length // 2] + s2[length // 2:]


def mutate(p):
    p = list(p)
    for i in range(length):
        if random() < chance:
            p[i] = choice(alphabet)
    return "".join(p)


def evolvePop(p):
    pool = []
    fitness = [evalFitness(p, target) for p in pop]
    maxFitness = max(fitness)

    # print(gen, p[fitness.index(maxFitness)])

    fitness = [pow(f // (maxFitness if maxFitness != 0 else 1), 4) if not cond else f // length for f in fitness]
    for e, f in zip(p, fitness):
        for _ in range(int(f * 100) + 1):
            pool.append(e)
    for i in range(n):
        p[i] = mutate(crossover(choice(pool), choice(pool)))

    return maxFitness


target = list(input("Inseire la frase da indovinare (in minuscolo): ").lower())

n = 150
length = len(target)
chance = 0.01

letters = "qwertyuiopasdfghjklzxcvbnm "
numbers = "1234567890"
punctuation = ".,;:"
alphabet = list(letters + numbers + punctuation)

pop = [''.join([choice(alphabet) for _ in range(length)]) for _ in range(n)]  # inizializza la popolazione
x = [0]
y = [0]
result = 0
gen = 0
cond = False

while result != length:
    gen += 1
    result = evolvePop(pop)
    x.append(gen)
    y.append(result)
    if gen > 1e4:
        break

print(f"Metodo 1 completato in {gen} generazioni")
plt.plot(x, y)
pop = [''.join([choice(alphabet) for _ in range(length)]) for _ in range(n)]  # inizializza la popolazione
x = [0]
y = [0]
result = 0
gen = 0
cond = True

while result != length:
    gen += 1
    result = evolvePop(pop)
    x.append(gen)
    y.append(result)
    if gen > 1e4:
        break

print(f"Metodo 2 completato in {gen} generazioni")
plt.plot(x, y, '--r')
plt.show()
