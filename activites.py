import csv

class Activite:

	def __init__(self, numero, nom):
		self.numero = numero
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

activite = Activite(1,"lol")
activite.Lecture("csv/activites.csv")
activite._get_nom()

