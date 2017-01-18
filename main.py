#!/usr/bin/python3
# -*-coding:Utf-8 -*
import os
from objects import *
from config_check import *
from backup import *

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

### CREATION DE LA LISTE D'OBJETS DE TYPE ' ELEMENT ' A SAUVEGARDER
# Boucle de parcours des différentes racines.
for conf in configLst: #{
    tree = [] # Liste d'Elements à sauvegarder
    bkp_path = os.path.abspath(conf.root) # résolution du chemin absolue
    if os.path.exists(bkp_path) is not True: #{
        msg = "\n---> Le chemin indiqué n'existe pas ou est inaccessible en lecture: " + bkp_path
        print (msg)
        print(len(msg) * "-")
    #}
    else: #{
        msg = "\n---> Analyse de l'arborescence à l'emplacement: " + bkp_path
        print(msg)
        print(len(msg) * "-")
        first_element = Element(bkp_path)
        element_tree = walk(first_element, conf.ignoredFiles)
    #}

    write_backup(conf, element_tree)

#}

