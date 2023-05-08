def drawings():
    product = []
    for i in range(-40, 41):
        product.append([i*10, -(i**2)/4 + 100])
    repeat = []
    for c in range(len(product)-1, 0, -1):
        repeat.append(product[c])
    return (product + repeat).copy()
