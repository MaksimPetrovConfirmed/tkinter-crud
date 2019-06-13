from tkinter import *
from table import Table
from database import DB
from main import window,db,firstname_text,lastname_text


def view_actor():
    global table1
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
    table1 = Table(window, headings=('Address', 'District', 'Postal code'), rows=db.get_address())
    table1.grid(row=2, column=0, rowspan=7, columnspan=2)


def view_film():
    global table1
    table1 = Table(window, headings=('Title', 'Release year', 'Length (min)'), rows=db.get_film())
    table1.grid(row=2, column=0, rowspan=7, columnspan=2)


def view_category():
    global table1
    table1 = Table(window, headings=('Category','Last update'), rows=db.get_category())
    table1.grid(row=2, column=0, rowspan=7, columnspan=2)


def view_country():
    global table1
    table1 = Table(window, headings=('Country','Last update'), rows=db.get_country())
    table1.grid(row=2, column=0, rowspan=7, columnspan=2)


def view_language():
    global table1
    table1 = Table(window, headings=('Language','Last update'), rows=db.get_language())
    table1.grid(row=2, column=0, rowspan=7, columnspan=2)


def view_customer():
    global table1
    table1 = Table(window, headings=('First name', 'Last name', 'Email'), rows=db.get_customer())
    table1.grid(row=2, column=0, rowspan=7, columnspan=2)


def view_staff():
    global table1
    table1 = Table(window, headings=('First name', 'Last name', 'Email'), rows=db.get_staff())
    table1.grid(row=2, column=0, rowspan=7, columnspan=2)
