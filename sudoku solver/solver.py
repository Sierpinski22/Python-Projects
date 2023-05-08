from file_manager import *  # idea: usare griglia delle entropie?

SIZE = 9  # solo 9x9


def initialize_grid():
    grid = [[None for _ in range(SIZE)] for _ in range(SIZE)]
    for i in range(SIZE):
        for j in range(SIZE):
            grid[i][j] = [1 if i != SIZE else -1 for i in range(SIZE + 1)]
    return grid


def compile_grid(grid, data):
    for index, number in enumerate(data):
        if number != 0:
            for i in range(SIZE):
                grid[index // SIZE][index % SIZE][i] = int(i == number - 1)
                grid[index // SIZE][index % SIZE][-1] = number - 1
            decrease_entropy(grid, index % SIZE, index // SIZE)


def available(x, y):
    return 0 <= x < SIZE and 0 <= y < SIZE


def decrease_entropy(grid, x, y):  # chiamata quando viene compiuta una mossa
    v = grid[y][x][-1]

    for i in range(SIZE):
        if available(x, i) and grid[i][x][-1] == -1:  # colonna
            grid[i][x][v] = 0
        if available(i, y) and grid[y][i][-1] == -1:  # riga
            grid[y][i][v] = 0
        if grid[(y // 3) * 3 + i // 3][(x // 3) * 3 + i % 3][-1] == -1:  # quadrato
            grid[(y // 3) * 3 + i // 3][(x // 3) * 3 + i % 3][v] = 0


def collapse(grid, x, y, v):
    grid[y][x][-1] = v
    grid[y][x][v] = 0


def stack_add(stack, grid, x, y):  # dovrebbe funzionare...
    copy = [[None for _ in range(SIZE)] for _ in range(SIZE)]
    
    for i in range(SIZE):
        for j in range(SIZE):
            copy[i][j] = [k for k in grid[i][j]]
    copy[y][x][-1] = -1
    stack.append(copy)


def find_collapse(grid, stack):
    x, y, v, e = None, None, None, SIZE + 1
    flag = False
    status = None  # 0 avanti, 1 completo, 2 contraddizione

    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j][-1] == -1:
                current = sum(grid[i][j][:-1])

                if current < e and current != 0:  # randomizzare?
                    e = current
                    y, x = i, j
                    candidates = [n for n, k in enumerate(grid[i][j][:-1]) if k]
                    v = candidates[0]

                    if current == 1:
                        flag = True
                        break

                elif current == 0:
                    return i, j, 2

        if flag:
            break

    if x is None or y is None or v is None:  # tutte condizioni equivalenti...
        return x, y, 1

    collapse(grid, x, y, v)  # compi la scelta

    if not flag:  # scelta arbitraria
        status = 0
        stack_add(stack, grid, x, y)

    return x, y, status



def solve(input_file):
    data = obtain_grid(input_file)
    grid = initialize_grid()
    compile_grid(grid, data)

    stack = []

    while True:

        x, y, s = find_collapse(grid, stack)

        if s == 2:
            grid = stack.pop(-1)
        elif s != 1:
            decrease_entropy(grid, x, y)
        else:
            break


    print("done")
    write_output("output.txt", grid)


solve("input.txt")
