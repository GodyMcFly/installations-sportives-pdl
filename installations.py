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
                print("Problème avec la base de donnée")

        DB_NAME='E155530E'


    """Getters and Setters"""

    def _set_numero(leNum):
        self.nom = leNum

    def _set_nom(leNom):
        self.nom = leNom

    def _set_cp(leCp):
        self.nom = leNom

    def _set_ville(laVille):
        self.nom = laVille

    def _set_nom(laLatitude):
        self.nom = laLatitude

    def _set_nom(laLongitude):
        self.nom = laLongitude





    def lecture(self):
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

    def geocoding(self, row):


installations = Installations(1, "nom", "cp", "ville", "latitude", "longitude")
installations.lecture()
