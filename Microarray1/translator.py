collection = {'conway': 'B3/S23',
              'amoeba': 'B357/S1358',
              'seeds': 'B2/S',
              'anti': 'B0123478/S01234678',
              'htree': 'B1/S012345678',
              'gnarl': 'B1/S1',
              'replicator': 'B1357/S1357',
              'liber': 'B2/S0',
              'snow': 'B25678/S5678',
              'corr': 'B3/S124',
              'coral': 'B3/S45678',
              'bacteria': 'B34/S456',
              'wall': 'B45678/S2345',
              'vote': 'B4678/S35678',
              'mice': 'B37/S1234',
              'stain': 'B3678/S235678',
              '2x2': 'B36/S125',
              'pseudo': 'B357/S238'}


def translate(rule):
    s, b = [0 for _ in range(9)], [0 for _ in range(9)]
    sr, br = rule.split('/')

    for i in range(9):
        if str(i) in list(sr):
            s[i] = 1
        if str(i) in list(br):
            b[i] = 1

    return b, s


def load(name):
    return translate(collection[name])
