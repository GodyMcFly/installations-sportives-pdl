from dao import *
from equipements import *
import csv

db = DAO()
db._connect()
#db.execute("INSERT into test(id) values(9)")
#print(db.get_rows("SELECT * FROM `test`"))
equipement = equipements()
equipement.importEquipements("csv/equipements.csv")
#activite.Lecture("csv/activites.csv")
