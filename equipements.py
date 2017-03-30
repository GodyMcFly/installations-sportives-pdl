import csv
from dao import *



class equipements:

    """
    Classe definissant les equipements caracterisee par :
    - le numero d identification
    - le nom
    - le numero d installation
    """

    """
    Fonction qui permet de lire un fichier CSV, de recuperer les colonnes que l on souhaite et de les inserer
    param, fichier qui est le fichier CSV dans lequel sont present les colonnes a importer
    """

    def importEquipements(self, fichier):
        with open(fichier) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.ajout(row[4], row[3], row[2])



    """
    Fonction qui permet de creer la table si elle n'existe pas deja et permet d executer la requete d importation pour inserer les lignes dans notre base de donnee
    param, identifiant et nom qui sont les objets des colonnes respectives
    """

    def ajout(self, numero, nom, numero_installation):
        ajoutEquipement = 'INSERT IGNORE INTO equipement VALUES ("{}","{}","{}")'.format(numero, nom, numero_installation)
        ajoutTable = 'CREATE TABLE IF NOT EXISTS `equipement`(`numero` int(64),`nom` varchar(64), `numero_installation` int(64) CHARACTER SET utf8 NOT NULL);'
        db = DAO()
        db.execute("LOCK TABLES `equipement` WRITE;")
        db.execute("SET foreign_key_checks = 0")
        db.execute(ajoutEquipement)
        db.execute("SET foreign_key_checks = 1")
