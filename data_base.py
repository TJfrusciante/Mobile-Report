import sqlite3

class DataBase():
    def __init__(self) -> None:
        self.manipular_db("CREATE TABLE IF NOT EXISTS money(description,date,value,selected,category)")
        self.manipular_db("CREATE TABLE IF NOT EXISTS tasks(name,date,selected,status)")
        self.manipular_db("CREATE TABLE IF NOT EXISTS categories(category)")
        self.results = self.manipular_db('SELECT * FROM tasks')
        self.transactions = self.manipular_db('SELECT * FROM money')
        self.categories= self.manipular_db('SELECT category FROM categories')
        
    def update_variables(self):
        self.results = self.manipular_db('SELECT * FROM tasks')
        self.transactions = self.manipular_db('SELECT * FROM money')
        self.categories= self.manipular_db('SELECT * FROM categories')
        
    def manipular_db(self, command, parametros = []):
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute(command, parametros)
            con.commit()
            return cur.fetchall()