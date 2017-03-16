from dao import *
from installations import *
import csv

db = DAO()
db._connect()
#db.execute("INSERT into test(id) values(9)")
#print(db.get_rows("SELECT * FROM `test`"))
installations = installations()
installations.importInstallations("csv/installations.csv")
#activite.Lecture("csv/activites.csv")
