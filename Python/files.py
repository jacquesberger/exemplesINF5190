# coding: utf8

from os.path import exists

# Afficher le contenu d'un fichier à la console
text_file = open("input/input1")
print text_file.read()
text_file.close()

# Lire une seule ligne d'un fichier
fichiers_prenoms_masculins = open("input/input2")
une_ligne = fichiers_prenoms_masculins.readline()
print une_ligne
fichiers_prenoms_masculins.close()

# Créer un fichier et y écrire des données
output = open("result.txt", "w")
resto_prefere = "Chez Chose"
phrase = "J'adore le restaurant %s." % resto_prefere
output.write(phrase)
output.close()

# Vérifier si un fichier existe
print exists("input/input1")
print exists("input/input1000")
