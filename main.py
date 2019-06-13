from tkinter import *
from table import Table
from database import DB


db = DB()

window = Tk()
window.title('Прокат фильмов')
window.resizable(False, False)
window.minsize(470, 280)

menu = Menu(window)
window.config(menu=menu)

label1 = Label(window, text="First Name")
label1.grid(row=1, column=2)

label2 = Label(window, text="Last Name")
label2.grid(row=1, column=4)

firstname_text = StringVar()
entry1 = Entry(window, textvariable=firstname_text)
entry1.grid(row=1, column=3)

lastname_text = StringVar()
entry1 = Entry(window, textvariable=lastname_text)
entry1.grid(row=1, column=5)

table1 = Table(window, headings=('', '', ''))
table1.grid(row=2, column=0, rowspan=7, columnspan=2)


def view_actor():
    global table1
    table1.destroy()
    table1 = Table(window, headings=('First name', 'Last name', 'Date'), rows=db.get_data())
    table1.grid(row=2, column=0, rowspan=7, columnspan=2)


def search_command():
    global table1
    table1 = Table(window, headings=('First name', 'Last name', 'Date'),
                   rows=db.search_data(firstname_text.get(), lastname_text.get()))
    table1.grid(row=2, column=0, rowspan=7, columnspan=2)


def add_command():
    db.insert_data(firstname_text.get(), lastname_text.get())
    global table1
    table1 = Table(window, headings=('First name', 'Last name', 'Date'), rows=db.get_data())
    table1.grid(row=2, column=0, rowspan=7, columnspan=2)


def delete_command():
    db.delete_data(firstname_text.get(), lastname_text.get())
    global table1
    table1 = Table(window, headings=('First name', 'Last name', 'Date'), rows=db.get_data())
    table1.grid(row=2, column=0, rowspan=7, columnspan=2)


def update_command():
    # db.update_data(, firstname_text.get(), lastname_text.get())
    global table1
    table1 = Table(window, headings=('First name', 'Last name', 'Date'), rows=db.get_data())
    table1.grid(row=2, column=0, rowspan=7, columnspan=2)


def view_address():
    global table1
    table1.destroy()
    table1 = Table(window, headings=('Address', 'District', 'Postal code'), rows=db.get_address())
    table1.grid(row=2, column=0, rowspan=7, columnspan=2)


def view_film():
    global table1
    table1.destroy()
    table1 = Table(window, headings=('Title', 'Release year', 'Length (min)'), rows=db.get_film())
    table1.grid(row=2, column=0, rowspan=7, columnspan=2)


def view_category():
    global table1
    table1.destroy()
    table1 = Table(window, headings=('Category','Last update'), rows=db.get_category())
    table1.grid(row=2, column=0, rowspan=7, columnspan=2)


def view_country():
    global table1
    table1.destroy()
    table1 = Table(window, headings=('Country','Last update'), rows=db.get_country())
    table1.grid(row=2, column=0, rowspan=7, columnspan=2)


def view_language():
    global table1
    table1.destroy()
    table1 = Table(window, headings=('Language','Last update'), rows=db.get_language())
    table1.grid(row=2, column=0, rowspan=7, columnspan=2)


def view_customer():
    global table1
    table1.destroy()
    table1 = Table(window, headings=('First name', 'Last name', 'Email'), rows=db.get_customer())
    table1.grid(row=2, column=0, rowspan=7, columnspan=2)


def view_staff():
    global table1
    table1.destroy()
    table1 = Table(window, headings=('First name', 'Last name', 'Email'), rows=db.get_staff())
    table1.grid(row=2, column=0, rowspan=7, columnspan=2)


menu.add_command(label="Актёры", command=view_actor)
menu.add_command(label="Адреса", command=view_address)
menu.add_command(label="Фильмы", command=view_film)
menu.add_command(label="Категории", command=view_category)
menu.add_command(label="Страны", command=view_country)
menu.add_command(label="Языки", command=view_language)
menu.add_command(label="Клиенты", command=view_customer)
menu.add_command(label="Работники", command=view_staff)

#button1 = Button(window, text="Посмотреть всё", width=20, command=view_command)
#button1.grid(row=3, column=3)

button2 = Button(window, text="Найти запись", width=20, command=search_command)
button2.grid(row=4, column=3)

button3 = Button(window, text="Добавить запись", width=20, command=add_command)
button3.grid(row=5, column=3)

button4 = Button(window, text="Изменить запись", width=20, command=update_command)
button4.grid(row=6, column=3)

button5 = Button(window, text="Удалить запись", width=20, command=delete_command)
button5.grid(row=7, column=3)

button6 = Button(window, text="Выход", width=20, command=window.destroy)
button6.grid(row=8, column=3)

window.mainloop()

