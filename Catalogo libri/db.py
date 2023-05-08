import sqlite3


class Database:
    def __init__(self, db_):
        self.conn = sqlite3.connect(db_)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS libri (id INTEGER PRIMARY KEY, titolo text, autore text, genere text, luogo text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM libri")
        rows = self.cur.fetchall()
        return rows

    def insert(self, titolo, autore, genere, luogo):
        self.cur.execute("INSERT INTO libri VALUES (NULL, ?, ?, ?, ?)", (titolo, autore, genere, luogo))
        self.conn.commit()

    def remove(self, id_):
        self.cur.execute("DELETE FROM libri WHERE id=?", (id_,))
        self.conn.commit()

    def update(self, id_, titolo, autore, genere, luogo):
        self.cur.execute("UPDATE libri SET titolo=?, autore=?, genere=?, luogo=? WHERE id=?",
                         (titolo, autore, genere, luogo, id_))
        self.conn.commit()

    def search(self, titolo, autore, genere, luogo):
        titolo = '%' + titolo + '%' if titolo != '' else '%%'
        autore = '%' + autore + '%' if autore != '' else '%%'
        genere = '%' + genere + '%' if genere != '' else '%%'
        luogo = '%' + luogo + '%' if luogo != '' else '%%'

        self.cur.execute('SELECT * FROM libri WHERE titolo LIKE ? AND autore LIKE ? AND genere LIKE ? AND luogo LIKE ?',
                         (titolo, autore, genere, luogo))
        found = self.cur.fetchall()
        return found

    def __del__(self):
        self.conn.close()

