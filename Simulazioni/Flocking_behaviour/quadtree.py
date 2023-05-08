## COME SI USA ##
#
# La classe element serve per dare al quadtree oggetti con cui lavorare. Essi possiedon un attributo "object" che è
# l'oggetto voluto dall'utilizzatore, uno "x" che rappresenta la posizione x
# e uno "y" per la coordinata y
#
# Creare il primo quadtree con la posizione, di solito (0, 0), e le dimensioni,di solito quelle della finestra.
# Volendo si può modificare la sensibilità, di base è 3.
#
# Le funzioni dell'albero chiamabili sono: put, query, show e reset
#       put: dato un array di elementi, inserisce il contenuto nel quadtree il quale si suddivide in automatico. Deve
#       essere una lista di element
#       query: restituisce gli elementi nella zona indicata (x e y sono i vertici in alto a sinistra, le altre le
#       dimensioni). La lista è formata da oggetti che da "element" sono riconvertiti (si restituisce una lista di
#       "element.object")
#       show: restituisce le dimensioni di ogni foglia, in un dizionario. 
#       reset: svuota l'albero ed elimina tutte le foglie
#
# Per ottimizzare un sistema in movimento bisogna usare in combinazione put e reset 
#
#
# Altre funzioni presenti nella libreria: to_centred
#       to_centred: dato un vertice in alto a sinistra e le dimensioni, restituisce i dati di un rettangolo con
#       dimensioni identiche e centro nel vertice dato


class quadtree:
    def __init__(self, x, y, w1, h1, sensitivity=3, passed_=None, depth=0):
        if passed_ is None:
            passed_ = []
        self.inside = []
        self.x = x
        self.y = y
        self.w = w1
        self.h = h1
        self.s = sensitivity
        self.nw = self.ne = self.sw = self.se = None
        self.depth = depth
        self.divided = False
        self.put(passed_)

    def contained(self, x, y):
        return self.x < x <= self.x + self.w and self.y < y <= self.y + self.h

    def intersect(self, x, y, w1, h1):
        dx = x - self.x
        dy = y - self.y

        check1 = dx < self.w if dx > 0 else -dx < w1
        check2 = dy < self.h if dy > 0 else -dy < h1

        return check1 and check2

    def subdivide(self):
        self.nw = quadtree(self.x, self.y, self.w / 2, self.h / 2, self.s, self.inside, self.depth + 1)
        self.ne = quadtree(self.x + self.w / 2, self.y, self.w / 2, self.h / 2, self.s, self.inside, self.depth + 1)
        self.sw = quadtree(self.x, self.y + self.h / 2, self.w / 2, self.h / 2, self.s, self.inside, self.depth + 1)
        self.se = quadtree(self.x + self.w / 2, self.y + self.h / 2, self.w / 2, self.h / 2, self.s, self.inside,
                           self.depth + 1)
        self.divided = True
        self.inside = []

    def put(self, array):
        if not self.divided:
            for a in array:
                if self.contained(a.x, a.y):
                    self.inside.append(a)

            if len(self.inside) > self.s:
                self.subdivide()
        else:
            self.nw.put(array)
            self.ne.put(array)
            self.sw.put(array)
            self.se.put(array)

    def query(self, x, y, w1, h1):
        to_give = acc = []
        if self.intersect(x, y, w1, h1):
            if self.divided:
                to_give += self.nw.query(x, y, w1, h1).copy()
                to_give += self.ne.query(x, y, w1, h1).copy()
                to_give += self.sw.query(x, y, w1, h1).copy()
                to_give += self.se.query(x, y, w1, h1).copy()
                return to_give
            else:
                for t in self.inside:
                    acc.append(t.object)
                return acc
        else:
            return []

    def reset(self):
        if self.divided:
            self.nw.reset()
            self.ne.reset()
            self.sw.reset()
            self.se.reset()
        self.divided = False
        self.inside = []
        self.nw = self.ne = self.sw = self.se = None

    def show(self):
        rectangles = []
        if self.divided:
            rectangles += self.nw.show()
            rectangles += self.ne.show()
            rectangles += self.sw.show()
            rectangles += self.se.show()
            return rectangles
        else:
            return [{'x': self.x, 'y': self.y, 'w': self.w, 'h': self.h}]


class element:
    def __init__(self, o, x, y):
        self.object = o
        self.x = x
        self.y = y


def to_centred(x, y, w1, h1, rounded=True):
    return round(x - w1 / 2) if rounded else x - w1 / 2, round(y - h1 / 2) if rounded else y - h1 / 2
