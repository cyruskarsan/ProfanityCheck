import sqlite3
from sqlite3 import Error
def sql_connection():
	try:
		con = sqlite3.connect('mydatabase.db')
		return con
	except Error:
		print(Error)

def sql_table(con):
	cursorObj = con.cursor()
	#cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
	cursorObj.execute("CREATE TABLE projects(id integer, name text)")
	con.commit()

def sql_insert(con, entities):
	cursorObj = con.cursor()
#	cursorObj.execute("INSERT INTO employees VALUES(1, 'John', 700, 'HR', 'Manager', '2017-01-04')")
	cursorObj.execute('''INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)''', entities)
	con.commit()
entities = (3, 'Cyrus', 10000, 'IT', 'Tech', '2019-08-05')

def sql_update(con):
	cursorObj = con.cursor()
	data = ("tegro",1)
	cursorObj.execute('UPDATE employees SET name = ? where id= ?', data)
	con.commit()

def sql_fetch(con):
	cursorObj = con.cursor()
	#choosing what we want to fetch (select)
	#cursorObj.execute('SELECT * FROM employees WHERE salary>500')
	cursorObj.execute('SELECT ID, name FROM employees WHERE salary>500')
	rows = cursorObj.fetchall()
	for row in rows:
		print(row)
	con.commit()

def sql_addMany(con):
	cursorObj = con.cursor()
	data = [(1, "bad"), (2, "word")]
	cursorObj.executemany("INSERT INTO projects VALUES(?,?)", data)
	con.commit()

con = sql_connection()
sql_update(con)
con.close()