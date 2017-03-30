# -*- coding: utf-8 -*-
from libs.bottle import run, view, post, request, route, template, static_file
import sys
sys.path.append('../common/model/')
from GestionDb import *
from dict_app import Glob

@route('/static/<filename:path>')
def server_static(filename):
	'''
	Gestion des librairies static.
	Routage des informations.
	'''

	return static_file(filename, root='static/')

@route('/')
@view('template.tpl')
def index():
	'''
	Fonction définissant le contexte de base.
	Retourne des informations au template.tpl
	'''

	context = {'title': "Formulaire",
				'titre': "Recherche",
				'ville' : "request.params.ville",
				'sport' : "request.params.sport",
				'equipement' : "request.params.equipement"}
	return (context)

@route('/resultat')
# @view('resultat.tpl')
def resultat():
	'''
	Fonction permettant de générer un résultat.
	Le résultat varie en fonction des mots-clés utilisateur.
	Utilisation de HTTP.GET pour récupérer les informations.
	Retourne les données du select au template resultat.
	'''

	# Objet base de données
	db = GestionBD(Glob.host, Glob.user, Glob.passwd, Glob.dbName)

	# Récupération des informations issues du formulaire
	ville = request.GET.get('ville')
	sport = request.GET.get('sport')
	equipement = request.GET.get('equipement')
	adresse = request.GET.get('adresse')
	coordonees = request.GET.get('coord')

	# Base fixe de la requête SQL select
	SELECT = "select ville, equipement.nom, activite.nom, code_postal, adresse, CONCAT(longitude, CONCAT(' ', latitude)) "
	TABLES = "from installation, equipement, equipement_activite, activite where installation.id_install = equipement.id_install and equipement.id_equip = equipement_activite.id_equipement and equipement_activite.id_activite = activite.id_activite "
	DATAS = "and activite.nom like '%"+sport+"%' and equipement.nom like '%"+equipement+"%' "

	req = SELECT+TABLES+DATAS

	if (ville != '' or sport != '' or equipement != ''):
		ville_composee = []
		ville_composee = ville.split(" ")
		# On parcourt tous les mots pouvant composer le nom d'une ville
		# On permet d'avoir une recherche plus souple selon l'input
		for mot in ville_composee:
			req += "and ville like '%"+mot+"%' "
		res = db.lireSelect(req)

		return template('resultat',rows=res, adr=adresse, coord=coordonees)
	else:
		return template('error',msg="Vous devez au moins entrer un mot clé pour avoir un résultat.")
	db.close()


@route('/plan')
@view('plan.tpl')
def plan():
	'''
	Fonction à implanter.
	Doit permettre d'afficher une map d'equipements / Installations
	'''

	context = {'title' : 'Plan', 'contient' : "Ceci est du text !"}

	return (context)


run(host='localhost', port=8081, reloader=True, debug=True)
