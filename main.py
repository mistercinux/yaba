#!/usr/bin/python3
# -*-coding:Utf-8 -*
import os
from objects import *
from config_check import *

line            = "init"
lineLst         = []

# Variables temporaires de configuration
bkpRoot              = ""
bkpName              = ""
bkpIgnored           = []
bkpStoragePath       = ""
defaultStoragePath   = ""

# Récupération de la liste des différentes configurations dans le fichier de conf 
#( liste de classes Config() )
configLst = check_configuration(configPath)


### RECUPERATION DES RACINES DE FICHIERS À SAUVEGARDER DANS LE FICHIER YABA.CONF
bkpRootLst = []
for some in configLst:
    bkpRootLst.append(some.root) #Liste des éléments à sauvegarder (dans le fichier yaba.conf)

### CREATION DE LA LISTE D'OBJETS DE TYPE ' ELEMENT ' A SAUVEGARDER
# Boucle de parcours des différentes racines.
for root in bkpRootLst:
    tree = [] # Liste d'Elements à sauvegarder
    bkp_path = os.path.abspath(root) # résolution du chemin absolue
    if os.path.exists(bkp_path) is not True:
        msg = "\n---> Le chemin indiqué n'existe pas ou est inaccessible en lecture: " + bkp_path
        print (msg)
        print(len(msg) * "-")
    else:
        msg = "\n---> Analyse de l'arborescence à l'emplacement: " + bkp_path
        print(msg)
        print(len(msg) * "-")
        first_element = Element(bkp_path)
        walk(first_element)






