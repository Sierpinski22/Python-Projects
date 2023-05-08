def obtain_grid(file):
    with open(file, 'r') as f:
        data = [int(r) for r in f.read().replace(' ', '').replace('\n', '')]
    return data


def write_output(file, output):
    with open(file, "w") as f:
        for rindex, row in enumerate(output):
            for cindex, col in enumerate(row):
                val = str(col[-1]+1) if col[-1] != -1 else '!'
                f.write(val)
                if cindex % 3 == 2:
                    f.write(" ")
            f.write("\n")
            if rindex % 3 == 2:
                f.write("\n")
