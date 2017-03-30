import csv
from dao import *

# -*- coding: utf-8 -*-

class Activite:

	"""
    Classe definissant les activites caracterisee par :
    - le numero d identification
    - le nom de l activite
    """

	"""
	Fonction qui permet de lire un fichier CSV, de recuperer les colonnes que l on souhaite et de les inserer
	param, fichier qui est le fichier CSV dans lequel sont present les colonnes a importer
	"""

	def importActivites(self, fichier):
		with open(fichier) as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				self.ajout(row[4], row[5])

	"""
	Fonction qui permet de creer la table si elle n'existe pas deja et permet d executer la requete d importation pour inserer les lignes dans notre base de donnee
	param, identifiant et nom qui sont les objets des colonnes respectives
	"""

	def ajout(self, identifiant, nom):

		ajoutTable = 'CREATE TABLE IF NOT EXISTS `activite` (`identifiant` int(64),`nom` varchar(64) CHARACTER SET utf8 NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8;'
		ajoutActivite = 'INSERT IGNORE INTO activite VALUES ("{}","{}")'.format(identifiant, nom)
		db = DAO()
		data = db.execute(ajoutTable)
		#db.execute("LOCK TABLES `activite` WRITE;")
		db.execute("SET foreign_key_checks = 0")
		db.execute(ajoutActivite)
		db.execute("SET foreign_key_checks = 1")
