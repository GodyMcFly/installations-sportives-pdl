import csv
from dao import *



class equipements:
    def __init__(self):

        """Constructeur de notre classe"""

    def _get_numero(self):
        return self.numero

    def _get_nom(self):
        return self.nom

    def _get_numero_installation(self):
        return self.numero_installation

    def _set_numero(self, numero):
        self.numero = numero

    def _set_nom(self, nom):
        self.nom = nom

    def _set_numero_installation(self, numero_installation):
        self.numero_installation


    def importEquipements(self, fichier):
        with open(fichier) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.ajout(row[4], row[3], row[2])


    def ajout(self, numero, nom, numero_installation):
        ajoutEquipement = 'INSERT IGNORE INTO equipement VALUES ("{}","{}","{}")'.format(numero, nom, numero_installation)

        db = DAO()
        db.execute("LOCK TABLES `equipement` WRITE;")
        db.execute("SET foreign_key_checks = 0")
        db.execute(ajoutEquipement)
        db.execute("SET foreign_key_checks = 1")
