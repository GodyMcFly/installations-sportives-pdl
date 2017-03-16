from dao import *
from equipements import *

db = DAO()
db._connect()
#db.execute("INSERT into test(id) values(9)")
#print(db.get_rows("SELECT * FROM `test`"))
equipement = equipements(10,"La poutre en bois",1)
equipement.ajout()
#equipement.Lecture("csv/equipements.csv")
