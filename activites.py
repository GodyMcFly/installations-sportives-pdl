import csv

#
# Ouverture du fichier source.
#
# D'après la documentation, le mode ''b'' est
# *obligatoire* sur les plate-formes où il est
# significatif. Dans la pratique, il est conseillé
# de toujours le mettre.
#

fname = "csv/activites.csv"
fileActivites = open(fname, "r")

try:
    # Création du ''lecteur'' CSV.
    reader = csv.reader(fileActivites)

    # Le ''lecteur'' est itérable, et peut être utilisé dans une boucle ''for'' pour extraire les lignes une par une.
    for row in reader:
	       print(row)

finally:
    # Fermeture du fichier source
    fileActivites.close()
