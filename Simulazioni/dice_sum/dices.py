from random import randint
import matplotlib.pyplot as plt


def get_sum(nt, nd, nf):
    min_sum = nd * min_face
    n_sums = nd * (nf - 1) + 1
    sums = list(range(min_sum, nf * nd + 1))
    results = [0 for _ in range(n_sums)]

    for _ in range(nt):
        throw = 0
        for _ in range(nd):
            throw += randint(1, n_faces)
        results[throw - min_sum] += 1
    results = [x / nt * 100 for x in results]
    return sums, results


while True:
    n_dices = int(input("Numero di dadi: "))
    n_faces = int(input("Numero di facce: "))
    n_throw = int(input("Numero di lanci: "))
    fig, ax = plt.subplots(figsize=(7, 5))
    min_face = 1  # inutile

    x1, y1 = get_sum(n_throw, n_dices, n_faces)
    ax.plot(x1, y1, 'o-', linewidth=2, color='b', markersize=7)
    ax.set_ylim(0)
    ax.set_facecolor((0, 0, 0))
    
    for i in range(len(x1)):
        ax.hlines(y=y1[i], xmin=0, xmax=x1[i], linestyles='--', linewidth=0.5, colors='r')
        ax.vlines(x=x1[i], ymin=0, ymax=y1[i], linestyles='--', linewidth=0.5, colors='r')

    plt.title(f'Distribuzione delle somme dei risultati di {n_dices} dadi a {n_faces} facce. Tiri di prova: {n_throw}')
    plt.ylabel('Frequenza risultato (%)')
    plt.xlabel('Risultato somma')
    print(f"\nValore minimo della somma: {min(x1)}, valore massimo: {max(x1)}.\nFrequenza minima tra i risultati: {min(y1):.2f}%, freqenza massima {max(y1):.2f}%") 
    print('\nGrafico completato\nPer provare con nuovi dati chiudere la finestra con il grafico\n')
    plt.show()                                                          
    print("=================================================================")
