from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from db import Database

db = Database('library.db')
app = Tk()
app.title('Catalogo libri')
width, height = 700, 350
size_str = str(width) + 'x' + str(height)
app.geometry(size_str)

kinds = ['Narrativa', 'Divulgazione', 'Poesia', 'Filosofia', 'Politica', 'Turismo']
places = ['Casa', 'Montagna', 'In prestito']



def select_item(event):
    try:
        global selected_item
        index = book_list.focus()
        selected_item = book_list.item(index)['values']

        book_entry.delete(0, END)
        book_entry.insert(END, selected_item[1])
        author_entry.delete(0, END)
        author_entry.insert(END, selected_item[2])
        genere_entry.delete(0, END)
        genere_entry.insert(END, selected_item[3])
        place_entry.delete(0, END)
        place_entry.insert(END, selected_item[4])
    except IndexError:
        pass


def populate_list(lis=db.fetch()):
    for i in book_list.get_children():
        book_list.delete(i)
    for row in lis:
        book_list.insert(parent='', index='end', iid=row[0], values=row)


def add_item():
    if book_text.get().strip() != '':
        db.insert(book_text.get(), author_text.get(), genere_text.get(), place_text.get())
        populate_list()
        clear_text()
    else:
        messagebox.showerror('Errore inserimento', 'Il titolo del libro è un campo obbligatorio')


def remove_item():
    db.remove(selected_item[0])
    populate_list()


def update_item():
    if book_text.get().strip() != '':
        db.update(selected_item[0], book_text.get(), author_text.get(), genere_text.get(), place_text.get())
        populate_list()
    else:
        messagebox.showerror('Errore modifica', 'Il titolo del libro non è inserito')


def clear_text():
    global selected_item
    book_entry.delete(0, END)
    author_entry.delete(0, END)
    genere_entry.delete(0, END)
    place_entry.delete(0, END)
    # selected_item = ['' for _ in selected_item]


def search_item():
    if not (book_text.get() == '' and author_text.get() == '' and genere_text.get() == '' and place_text.get() == ''):
        found = db.search(book_text.get(), author_text.get(), genere_text.get(), place_text.get())
        populate_list(found)
    else:
        populate_list()


# Titolo libro
book_text = StringVar()
book_label = Label(app, text='Titolo libro:', font=('bold', 14))
book_label.place(x=5, y=5)
book_entry = Entry(app, textvariable=book_text)
book_entry.place(x=width / 4, y=10)

# Autore
author_text = StringVar()
author_label = Label(app, text='Autore libro:', font=('bold', 14))
author_label.place(x=width / 4 * 2, y=5)
author_entry = Entry(app, textvariable=author_text)
author_entry.place(x=width / 4 * 3, y=10)

# Tipo
genere_text = StringVar()
genere_label = Label(app, text='Genere:', font=('bold', 14), pady=10)
genere_label.place(x=5, y=30)
genere_entry = ttk.Combobox(app, values=kinds, textvariable=genere_text)
genere_entry.place(x=width / 4, y=5 + 40)

# Luogo
place_text = StringVar()
place_label = Label(app, text='Luogo', font=('bold', 14))
place_label.place(x=width / 4 * 2, y=10 + 30)
place_entry = ttk.Combobox(app, values=places, textvariable=place_text)
place_entry.place(x=width / 4 * 3, y=5 + 40)

book_list = ttk.Treeview(app)
book_list['columns'] = ('id', 'Titolo', 'Autore', 'Genere', 'Luogo')

book_list.column('#0', anchor=CENTER, width=0)
book_list.column('id', anchor=CENTER, width=20)
book_list.column('Titolo', anchor=W, width=300)
book_list.column('Autore', anchor=W, width=150)
book_list.column('Genere', anchor=W, width=100)
book_list.column('Luogo', anchor=W, width=100)

book_list.heading('id', text='ID', anchor=W)
book_list.heading('Titolo', text='Titolo', anchor=W)
book_list.heading('Autore', text='Autore', anchor=W)
book_list.heading('Genere', text='Genere', anchor=W)
book_list.heading('Luogo', text='Luogo', anchor=W)

book_list.place(x=5, y=120)
book_list.bind('<ButtonRelease-1>', select_item)

scrollbar = ttk.Scrollbar(app, orient="vertical", command=book_list.yview)
scrollbar.place(x=680, y=120, height=230)

# bottoni
xoff, space = 40, 130
add_btn = Button(app, text='Aggiungi', width=12, command=add_item)
add_btn.place(x=xoff, y=80)
remove_btn = Button(app, text='Rimuovi', width=12, command=remove_item)
remove_btn.place(x=xoff + space, y=80)
update_btn = Button(app, text='Modifica', width=12, command=update_item)
update_btn.place(x=xoff + space*2, y=80)
clear_btn = Button(app, text='Pulisci input', width=12, command=clear_text)
clear_btn.place(x=xoff + space*3, y=80)
search_btn = Button(app, text='Cerca', width=12, command=search_item)
search_btn.place(x=xoff + space*4, y=80)

# Compila lista
populate_list()
# start
app.mainloop()
