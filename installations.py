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

    """
    Fonction qui permet de lire un fichier CSV, de recuperer les colonnes que l on souhaite et de les inserer
    param, fichier qui est le fichier CSV dans lequel sont present les colonnes a importer
    """

    def importInstallations(self, fichier):
		with open(fichier) as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				self.ajoutInstallations(row[1], row[0], (row[5]+" "+row[6]+" "+row[7]), row[4], row[2], row[10], row[9])

    """
    Fonction qui permet de creer la table si elle n'existe pas deja et permet d executer la requete d importation pour inserer les lignes dans notre base de donnee
    param, identifiant et nom qui sont les objets des colonnes respectives
    """


    def ajoutInstallations(self, numero, nom, adresse, cp, ville, latitude, longitude):
        ajoutInstallations = 'INSERT IGNORE INTO installation VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(numero, nom, adresse, cp, ville, latitude, longitude)
        ajoutTable = 'CREATE TABLE IF NOT EXISTS `installation` (`numero` int(64),`nom` varchar(64), `adresse` varchar(64), `cp` int(64), `ville` varchar(64), `latitude` decimal(30, 0), longitude decimal(30, 0)) ENGINE=InnoDB DEFAULT CHARSET=utf8;'
        db = DAO()
        db.execute(ajoutTable);
        db.execute("SET NAMES utf8;")
        db.execute("LOCK TABLES `installation` WRITE;")
        db.execute("SET foreign_key_checks = 0")
        db.execute(ajoutInstallations)
        db.execute("SET foreign_key_checks = 1")
