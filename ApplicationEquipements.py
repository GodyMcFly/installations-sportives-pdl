from dao import *
from equipements import *

db = DAO()
db._connect()
equipement = equipements()
equipement.importEquipements("csv/equipements.csv")
