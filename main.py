#!/usr/bin/python3
# -*-coding:Utf-8 -*
import os
from objects import *

# Fonction de parcours de l'arborescence et on crée des objets de type Element pour chaque élément rencontré
def walk(tree):
    for element in tree:
        if element.what == "DIR":
            for some in os.listdir(element.path):
                tree.append(Element(os.path.join(element.path, some)))

configPath = "yaba.conf"
configPath = os.path.abspath(configPath)
line = "init"

configFd = open(configPath, "r")
print("Lecture de la configuration...")
print(30 * "-")
line = configFd.readline()
while line != "":
    if (line[0] != "#") and (line != "\n"):
        print(" - ", line, end="")
    line = configFd.readline()
print(30 * "-")

### RECUPERATION DES RACINES DE FICHIERS À SAUVEGARDER DANS LE FICHIER YABA.CONF
try:
    fd_config = open(configPath)
except FileNotFoundError:
    print("Fichier de configuration introuvable:", configPath)
    exit()

bkpRootLst = [ "toto", "yop" ] #Liste des éléments à sauvegarder (dans le fichier yaba.conf)

### CREATION DE LA LISTE D'OBJETS DE TYPE ' ELEMENT ' A SAUVEGARDER
tree = [] # Liste d'Elements à sauvegarder
# Boucle de parcours des différentes racines.
for root in bkpRootLst:
    bkp_path = os.path.abspath(root) # résolution du chemin absolue
    if os.path.exists(bkp_path) is not True:
        msg = "\n---> Le chemin indiqué n'existe pas ou est inaccessible en lecture: " + bkp_path
        print (msg)
        print(len(msg) * "-")
    else:
        msg = "\n---> Analyse de l'arborescence à l'emplacement: " + bkp_path
        print(msg)
        print(len(msg) * "-")
        tree.append(Element(bkp_path))
        walk(tree)




#def inspect(files): # files is a list
#    for element in  files:
#        if isdir(element) is True:
#            inspect(element)
#        elif isfile(element):
#            addToIndex(element)
#        print(element)





