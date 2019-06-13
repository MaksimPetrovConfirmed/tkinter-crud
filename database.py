import mysql.connector


class DB:
    def __init__(self):
        self.conn = mysql.connector.connect(host='localhost',
                                            database='sakila',
                                            user='root',
                                            password='12345',
                                            buffered=True)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def remove_id(self, row):
        lst = list(row)
        lst.remove(lst[0])
        row = tuple(lst)
        return row

    # Получение списка всех актеров
    def get_data(self):
        self.cursor.execute("SELECT * FROM actor")
        rows = self.cursor.fetchall()
        no_id = []
        for row in rows:
            lst = list(row)
            lst.remove(lst[0])
            row = tuple(lst)
            no_id.append(row)
            print(row)
        return no_id

    # Добавление новых
    def insert_data(self, firstname, lastname):
        self.cursor.execute("INSERT INTO actor(first_name, last_name) VALUES ('{0}','{1}')".format(firstname, lastname))
        self.conn.commit()

    # Поиск отдельного актера
    def search_data(self, firstname="", lastname=""):
        self.cursor.execute("SELECT * FROM actor WHERE first_name='{0}' AND last_name='{1}'".format(firstname, lastname))
        foundRows = self.cursor.fetchall()
        no_id = []
        for row in foundRows:
            lst = list(row)
            lst.remove(lst[0])
            row = tuple(lst)
            no_id.append(row)
        return no_id

    # Изменение записи
    def update_data(self, id, firstname, lastname):
        self.cursor.execute("UPDATE actor SET first_name='{0}', last_name='{1}' WHERE id=?".format(firstname, lastname, id))
        self.conn.commit()

    # Удаление записи
    def delete_data(self, firstname, lastname):
        self.cursor.execute("DELETE from actor WHERE first_name='{0}' AND last_name='{1}'".format(firstname, lastname))
        self.conn.commit()

    def rows_count(self):
        self.cursor.execute("SELECT * FROM actor")
        rows = self.cursor.fetchall()
        print(rows)
        return len(rows)

    def get_address(self):
        self.cursor.execute("SELECT address, district, postal_code FROM address")
        rows = self.cursor.fetchall()
        return rows

    def get_film(self):
        self.cursor.execute("SELECT title, release_year, length FROM film")
        rows = self.cursor.fetchall()
        return rows

    def get_category(self):
        self.cursor.execute("SELECT name, last_update FROM category")
        rows = self.cursor.fetchall()
        return rows

    def get_country(self):
        self.cursor.execute("SELECT country, last_update FROM country")
        rows = self.cursor.fetchall()
        return rows

    def get_language(self):
        self.cursor.execute("SELECT name, last_update FROM language")
        rows = self.cursor.fetchall()
        return rows

    def get_customer(self):
        self.cursor.execute("SELECT first_name, last_name, email FROM customer")
        rows = self.cursor.fetchall()
        return rows

    def get_staff(self):
        self.cursor.execute("SELECT first_name, last_name, email FROM staff")
        rows = self.cursor.fetchall()
        return rows
