import csv
from dao import *

# -*- coding: utf-8 -*-

class installations:

    """
    Classe definissant les installations caracterisee par :
    - le numero
    - le nom
    - l adresse
    - le code postal
    - la ville
    - la latitude
    - la longitude
    """

    def __init__(self):

        """Constructeur de notre classe"""


    """Getters and Setters"""

    def _set_numero(self, leNum):
        self.numero = leNum

    def _set_nom(self, leNom):
        self.nom = leNom

    def _set_adresse(self, lAdresse):
        self.numero = lAdresse

    def _set_cp(self, leCp):
        self.cp = leCp

    def _set_ville(self, laVille):
        self.ville = laVille

    def _set_nom(self, laLatitude):
        self.latitude = laLatitude

    def _set_nom(self, laLongitude):
        self.longitude = laLongitude


    def _get_num():
        return self.nom

    def _get_numero():
        return self.numero

    def _get_adresse():
        return self.adresse

    def _get_cp():
        return self.cp

    def _get_ville():
        return self.ville

    def _get_latitude():
        return self.latitude

    def _get_longitude():
        return self.longitude


    def importInstallations(self, fichier):
		with open(fichier) as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				self.ajoutInstallations(row[1], row[0], (row[5]+" "+row[6]+" "+row[7]), row[4], row[2], row[10], row[9])


    def ajoutInstallations(self, numero, nom, adresse, cp, ville, latitude, longitude):
		ajoutInstallations = 'INSERT IGNORE INTO installation VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(numero, nom, adresse, cp, ville, latitude, longitude)
		db = DAO()
		db.execute("SET NAMES utf8;")
		#db.execute("LOCK TABLES `installations` WRITE;")
		db.execute("SET foreign_key_checks = 0")
		db.execute(ajoutInstallations)
		db.execute("SET foreign_key_checks = 1")
