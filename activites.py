import csv
from dao import *

class Activite:

	def __init__(self, identifiant, nom):
		self.identifiant = identifiant
		self.nom = nom

	def _get_numero(self):
		return self.numero

	def _get_nom(self):
		return self.nom

	def _set_numero(self, numero):
		self.numero = numero

	def _set_nom(self, nom):
		self.nom = nom

	def Lecture(self, fichier):
		with open(fichier) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				print(row)

	def ajout(self):
		ajoutActivte = 'INSERT IGNORE INTO activite VALUES ("{}","{}")'.format(self.identifiant, self.nom)

		db = DAO()
		db.execute("LOCK TABLES `activite` WRITE;")
		db.execute("SET foreign_key_checks = 0")		
		db.execute(ajoutActivte)
		db.execute("SET foreign_key_checks = 1")


