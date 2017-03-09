from dao import *
from activites import *

db = DAO()
db._connect()
#db.execute("INSERT into test(id) values(9)")
#print(db.get_rows("SELECT * FROM `test`"))
activite = Activite(1,"lol")
activite.ajout()
#activite.Lecture("csv/activites.csv")
