#!/usr/bin/python3
# -*-coding:Utf-8 -*
import os
from objects import *

configPath      = "yaba.conf"
configPath      = os.path.abspath(configPath)

def config_error():
#{
    """ config_error(): Affiche un message d'erreur et quitte le programme """

    print("Une erreur a été détectée dans le fichier de configuration")
    exit()
#}


def walk(element):
    """ walk(element): -> list of "Element"
        element is an object from class Element that contain the root path du walk through.
        Parse the tree to backup starting at the root from the element given in argument, 
        and returns a list of all files and dirs as Objects from class 'Element' """
    tree = []
    tree.append(element)
    for element in tree:
        if element.what == "DIR":
            for some in os.listdir(element.path):
                tree.append(Element(os.path.join(element.path, some)))
    return tree


def handle_directory(configFd, configLst, defaultStoragePath):
#{
    """handle_directory(configFd, configLst, defaultStoragePath) where:
            configFd is a file descriptor
            configLst is a list of 'Element' objects
            defaultConfigPath is a string with the default config file path"""

    bkpDirectory = ""
    bkpName = ""
    bkpStoragePath = ""
    bkpIgnored = []
    line = configFd.readline()
    lineLst = line.split()

    while line.replace(' ','') != "\n" and line != "</end>": #{

        # On ignore les lignes vides et les commentaires
        if (line[0] != "#") and (line.replace(' ','') != "\n"): #{
            if line == "": #{
                config_error()
            #}
            if lineLst[0] == "directory": #{
                bkpDirectory = lineLst[1]
            #}
            elif lineLst[0] == "name": #{
                bkpName = lineLst[1]
            #}
            elif lineLst[0] == "ignored_files": #{
                lineLst.remove("ignored_files")
                bkpIgnored = lineLst
            #}
            elif lineLst[0] == "storage_path": #{
                bkpStoragePath = lineLst[1]
            #}
        #}
        line = configFd.readline()
        lineLst = line.split()

    #}
        if bkpStoragePath == "": #{
            bkpStoragePath = defaultStoragePath
    #}
    configLst.append(Config(bkpDirectory, bkpIgnored, bkpStoragePath, bkpName))
#}



def check_configuration(configPath):
    """ chech_configuration(PATH/TO/CONIGURATION/FILE)
        Analyse les paramètres dans le fichier yaba.conf et retourne une liste d'objet de la classe Config."""

    line            = "init"
    lineLst         = []

    # Variables temporaires de configuration
    defaultStoragePath   = ""

    # Liste des différentes configurations de sauvegarde
    configLst = [] # Liste d'objets de la classe Config()

    try:
        configFd = open(configPath, "r")
    except FileNotFoundError:
        print("Fichier de configuration introuvable:", configPath)
        exit()

    print("Lecture de la configuration...")
    print(30 * "-", "\n")

    line = configFd.readline()
    while line != "":
        #input("DEBUG 1")
        if (line[0] != "#") and (line.replace(' ','') != "\n"):
            lineLst = line.split()
            if lineLst[0] == "default_storage_path":
                defaultStoragePath = lineLst[1]
                line = configFd.readline()
                lineLst = line.split()
                print("Répertoire de stockage par défaut: ", defaultStoragePath)
                continue
            elif lineLst[0] == "<backup_directory>":
                print("Handling Directory...")
                handle_directory(configFd, configLst, defaultStoragePath)

        line = configFd.readline()

    print(30 * "-")
    input("Appuyez sur ENTER pour continuer")
    return configLst

