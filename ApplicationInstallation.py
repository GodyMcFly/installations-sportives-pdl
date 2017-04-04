from dao import *
from installations import *

db = DAO()
db._connect()
installation = installations()
installation.importInstallations("csv/installations.csv")
