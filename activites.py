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

