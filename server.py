from dao import *
from libs.bottle import route, static_file, run
import json
from urllib.parse import urlencode
from urllib import request as req

app = Bottle();

@route('/')
def installation():
	db = DAO()
	data = db.get_rows("SELECT numero, nom from activite order by nom asc;")
	data2 = db.get_rows("SELECT DISTINCT ville from installation order by ville asc;")

	liste = [data, data2]
	output = template('src/IHM/index.tpl', rows=liste)
	return output


"""@route('/recherche')
def recherche():
	ville = request.query.ville
	sport = request.query.sport

	db = dao._connect()
	dbc = db.cursor()

	if(ville!="all" and sport!="all"):
		dbc.execute("SELECT e.nom, i.nom, i.adresse, i.code_postal, i.ville, i.latitude, i.longitude from installation i, equipement e, equipement_activite ea, activite a where i.numero=e.numero_installation and e.numero=ea.numero_equipement and ea.numero_activite=a.numero and a.numero=\""+sport+"\" and i.ville=\""+ville+"\";")
		output = template('src/IHM/resultat.tpl', rows=c)
	if(ville=="all" and sport!="all"):
		dbc.execute("SELECT e.nom, i.nom, i.adresse, i.code_postal, i.ville, i.latitude, i.longitude from installation i, equipement e, equipement_activite ea, activite a where i.numero=e.numero_installation and e.numero=ea.numero_equipement and ea.numero_activite=a.numero and a.numero=\""+sport+"\";")
		output = template('src/IHM/resultat.tpl', rows=c)
	if(ville!="all" and sport=="all"):
		dbc.execute("SELECT a.nom, e.nom, i.nom, i.adresse, i.code_postal, i.ville, i.latitude, i.longitude from installation i, equipement e, equipement_activite ea, activite a where i.numero=e.numero_installation and e.numero=ea.numero_equipement and ea.numero_activite=a.numero and i.ville=\""+ville+"\";")
		output = template('src/IHM/resultatSP.tpl', rows=c)
	if(ville=="all" and sport=="all"):
		dbc.execute("SELECT a.nom, e.nom, i.nom, i.adresse, i.code_postal, i.ville, i.latitude, i.longitude from installation i, equipement e, equipement_activite ea, activite a where i.numero=e.numero_installation and e.numero=ea.numero_equipement and ea.numero_activite=a.numero;")
		output = template('src/IHM/resultatSP.tpl', rows=c)

	c.close()
	return output

@route('/api/activites')
def activites = allActivities()
	jsonActivites = []
	for activity in activities:
		jsonActivites.append(activity.__dict__)
	return { "activites" : jsonActivites }"""


run(app, host='localhost', port=8888)
