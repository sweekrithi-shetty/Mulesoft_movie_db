import sqlite3
connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS 
movies(movie_id INTEGER PRIMARY KEY, movie_title TEXT, actor_name TEXT,
 year INTEGER, director_name TEXT)"""

cursor.execute(command1)
cursor.execute("INSERT INTO movies VALUES(1,'Avengers','Chris Evens',2019,'Russo Brothers')")
cursor.execute("INSERT INTO movies VALUES(2,'Bahubali','prabas',2015,'Rajmouli')")
cursor.execute("INSERT INTO movies VALUES(3,'Vikram','Kamal Hassan',2022,'Kamal Hassan')")

cursor.execute("SELECT * FROM movies")
results = cursor.fetchall()

print(results)
print('Details of the movie in which  Kamal Hassan was the lead actor')
cursor.execute("SELECT * FROM movies WHERE actor_name='Kamal Hassan'")
res = cursor.fetchall()
print(res)