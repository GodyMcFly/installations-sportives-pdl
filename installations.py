import csv
import mysql.connector

class installations:

    """
    Classe définissant les installations caractérisée par :
    - le numéro
    - le nom
    - le code postal
    - la ville
    - la latitude
    - la longitude
    """

    def __init__(self, numero, nom, cp, ville, latitude, longitude):

        """Constructeur de notre classe"""

        self.numero = numero
        self.nom = nom
        self.cp = cp
        self.ville = ville
        self.latitude = latitude
        self.longitude = longitude


    try:
      connexion = mysql.connector.connect(user='E155530E', password='E155530E',
                              host='localhost')
    except mysql.connector.Error as erreur:
      if erreur.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Problème avec l'identifiant ou le mot de passe")
    elif erreur.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de données n'existe pas")
      else:
        print(erreur)
    else:
      connexion.close()

    DB_NAME = 'E155530E'




fname = "csv/installations.csv"
fileInstallations = open(fname, "r")

try:
    # Création du ''lecteur'' CSV.
    reader = csv.reader(fileInstallations)

    # Le ''lecteur'' est itérable, et peut être utilisé dans une boucle ''for'' pour extraire les lignes une par une.
    for row in reader:
	       print(row)

finally:
    # Fermeture du fichier source
    fileInstallations.close()
