from colorsys import hsv_to_rgb


def test(n, n_max):
    return tuple(round(i * 255) for i in hsv_to_rgb(n / (n_max + 0), 1, 1))
