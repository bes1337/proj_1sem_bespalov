import sqlite3 as sq
from peoplebd import touristiki, touriki, bron
with sq.connect('tourist.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Tourists(
    id_tourist INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL,
    surname VARCHAR NOT NULL, 
    gender INTEGER NOT NULL,
    date_of_birth DATE,
    phone_number VARCHAR NOT NULL,
    email VARCHAR NOT NULL
    )''')
    cur.executemany("INSERT INTO Tourists VALUES (?, ?, ?, ?, ?, ?, ?)", touristiki)

with sq.connect('tourist.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Tours(
    id_tour INTEGER PRIMARY KEY AUTOINCREMENT,
    tour_name VARCHAR NOT NULL,
    country VARCHAR NOT NULL,
    city INTEGER NOT NULL,
    start_day DATE,
    end_day DATE,
    price DECIMAL(10, 3)
    )''')
    cur.executemany("INSERT INTO Tours VALUES (?, ?, ?, ?, ?, ?, ?)", touriki)

with sq.connect('tourist.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Reservations(
    id_res INTEGER PRIMARY KEY AUTOINCREMENT,
    id_tourist INTEGER,
    id_tour ININTEGER,
    date_of_reservation DATE,
    number_of_tourists INTEGER,
    FOREIGN KEY (id_tourist) REFERENCES Tourists (id_tourist),
    FOREIGN KEY (id_tour) REFERENCES Tours (id_tour)
    )''')
    cur.executemany("INSERT INTO Reservations VALUES (?, ?, ?, ?, ?)", bron)

#SQL-запросы на выборку данных из БД:
#1
'''with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT name, surname FROM Tourists") 
    result = cur.fetchall()
print(result)

#2
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT tour_name, price FROM Tours ORDER BY price ASC") 
    result = cur.fetchall()
print(result)

#3
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT  Reservations.id_res, Reservations.id_tourist, Reservations.id_tour, Reservations.date_of_reservation, Reservations.number_of_tourists FROM Reservations JOIN Tours ON Reservations.id_tour = Tours.id_tour WHERE Tours.city = 'Адыгея'") 
    result = cur.fetchall()
print(result)

#4
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT DISTINCT name, surname, Reservations.date_of_reservation FROM Tourists JOIN Reservations ON Reservations.id_tourist WHERE date_of_reservation BETWEEN '2023-04-01' AND '2023-04-31'") 
    result = cur.fetchall()
print(result)

#5
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT tour_name, country, city FROM Tours") 
    result = cur.fetchall()
print(result)

#6
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT name, surname FROM Tourists WHERE gender = 2 AND date_of_birth > '1990-01-01'") 
    result = cur.fetchall()
print(result)

#7
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT tour_name, price FROM Tours WHERE price > 5000") 
    result = cur.fetchall()
print(result)

#8
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT name, surname FROM Tourists JOIN Reservations ON Tourists.id_tourist = Reservations.id_tourist WHERE Reservations.id_tour = 6") 
    result = cur.fetchall()
print(result)

#9
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT name, surname FROM Tourists JOIN Reservations ON Tourists.id_tourist = Reservations.id_tourist WHERE Reservations.date_of_reservation = '2023-04-17'") 
    result = cur.fetchall()
print(result)

#10
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT name, surname, phone_number FROM Tourists WHERE phone_number LIKE '+7%'") 
    result = cur.fetchall()
print(result)'''

#SQL-запросы на обновление данных из БД:
#1
'''with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE Tours SET start_day = '2023-05-01' WHERE id_tour = 1") 
    result = cur.fetchall()

#2
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE Tours SET price = 1500 WHERE id_tour = 7") 
    result = cur.fetchall()

#3
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE Tourists SET phone_number = '+1 (555) 123-4567' WHERE id_tourist = 5") 
    result = cur.fetchall()

#4
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE Reservations SET date_of_reservation = '2023-04-05' WHERE id_res = 3") 
    result = cur.fetchall()

#5
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE Reservations SET number_of_tourists = 3 WHERE id_res = 8") 
    result = cur.fetchall()

#6
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE Tours SET end_day =  '2023-08-31' WHERE id_tour = 2") 
    result = cur.fetchall()

#7
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE Tourists SET email = 'new_email@example.com' WHERE id_tourist = 1") 
    result = cur.fetchall()

#8
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE Tours SET start_day = '2023-06-15' WHERE id_tour = 4") 
    result = cur.fetchall()

#9
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE Tours SET start_day = '2023-05-01' WHERE country = 'Испания'") 
    result = cur.fetchall()

#10
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE Tours SET price = '1500' WHERE tour_name = 'Греция-отдых на море'") 
    result = cur.fetchall()

#11
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE Tours SET start_day = '2023-06-01' WHERE tour_name = 'Испания-путешествие по городам'") 
    result = cur.fetchall()

#12
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE Reservations SET number_of_tourists = 3 WHERE id_res = 1002") 
    result = cur.fetchall()

#13
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE Tourists SET phone_number = '+1 (123) 456-7890' WHERE id_tourist = 2001") 
    result = cur.fetchall()

#14
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE Tours SET start_day = '2024-07-01' WHERE price < '2000'") 
    result = cur.fetchall()

#15
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE Tourists SET email = 'new_email@example.com' WHERE phone_number LIKE '+7%'") 
    result = cur.fetchall()

#16
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE Reservations SET date_of_reservation = '2023-08-15' WHERE number_of_tourists > 2") 
    result = cur.fetchall()

#17
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE Tours SET tour_name = 'Египет-отдых на курорте' WHERE id_tour = 1003") 
    result = cur.fetchall()
print(result)'''


#SQL-запросы на удаление данных из БД:

'''#1
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("DELETE FROM Reservations WHERE id_tourist = 1") 
    result = cur.fetchall()

#2
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("DELETE FROM Reservations WHERE id_tour = 2") 
    result = cur.fetchall()

#3
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("DELETE FROM Reservations WHERE date_of_reservation = '2023-03-21'") 
    result = cur.fetchall()

#4
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("DELETE FROM Tourists WHERE id_tourist = (SELECT id_tourist FROM Reservations WHERE id_tour = 3)") 
    result = cur.fetchall()

#5
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("DELETE FROM Reservations WHERE id_tourist = (SELECT id_tourist FROM Tourists WHERE phone_number = '+7-931-992-45-12')") 
    result = cur.fetchall()

#6
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("DELETE FROM Reservations WHERE id_tourist = (SELECT id_tourist FROM Tourists WHERE email = 'danilless@gmail.com')") 
    result = cur.fetchall()

#7
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("DELETE FROM Reservations WHERE id_tour = (SELECT id_tour FROM Tours WHERE start_day > '2023-07-10')") 
    result = cur.fetchall()

#8
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("DELETE FROM Tourists WHERE id_tourist = (SELECT id_tourist FROM Reservations WHERE id_tour = '6')") 
    result = cur.fetchall()

#9 
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("DELETE FROM Reservations WHERE id_tour = (SELECT id_tour FROM Tours WHERE end_day < '2023-04-11')") 
    result = cur.fetchall()

#10
with sq.connect('tourist.db') as con: 
    cur = con.cursor()
    cur.execute("DELETE FROM Reservations WHERE id_tour = (SELECT id_tour FROM Tours WHERE price = '118000')") 
    result = cur.fetchall()'''







