import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="dbuser",
    passwd="123",
    db="first_db"
)

c = db.cursor()
c.execute('INSERT INTO prizivniki (name, surname, patronymic , categoriya, vozrast, otsrochka, adress) VALUES (Сергей, Крутой, Владимирович, 22, есть, Москва)');
db.commit()
c.close()
db.close()