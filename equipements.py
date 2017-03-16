import csv
from dao import *



class equipements:
    def __init__(self, numero, nom, numero_installation):
        self.numero = numero
        self.nom = nom
        self.numero_installation = numero_installation

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


    def Lecture(self, fichier):
        with open(fichier) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)


    def ajout(self):
        ajoutEquipement = 'INSERT IGNORE INTO equipement VALUES ("{}","{}","{}")'.format(self.numero, self.nom, self.numero_installation)

        db = DAO()
        db.execute("LOCK TABLES `equipement` WRITE;")
        db.execute("SET foreign_key_checks = 0")
        db.execute(ajoutEquipement)
        db.execute("SET foreign_key_checks = 1")
