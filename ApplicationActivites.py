from dao import *
from activites import *

db = DAO()
db._connect()
activite = Activite()
activite.importActivites("csv/activites.csv")