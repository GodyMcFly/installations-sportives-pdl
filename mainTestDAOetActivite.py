from dao import *
from equipements import *

db = DAO()
db._connect()
#db.execute("INSERT into test(id) values(9)")
#print(db.get_rows("SELECT * FROM `test`"))
<<<<<<< HEAD
equipement = equipements(10,"La poutre en bois",1)
equipement.ajout()
#equipement.Lecture("csv/equipements.csv")
=======
activite = Activite(1,"lol")
activite.ajout()
#activite.Lecture("csv/activites.csv")


, numero, nom, adresse, cp, ville, latitude, longitude

self.numero = numero
self.nom = nom
self.adresse = adresse
self.cp = cp
self.ville = ville
self.latitude = latitude
self.longitude = longitude
>>>>>>> d34ee1d58b2bbd9bc1b2ed3db9a6339e1d495df2
