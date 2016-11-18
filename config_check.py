#!/usr/bin/python3
# -*-coding:Utf-8 -*
import os
from objects import *

configPath      = "yaba.conf"
configPath      = os.path.abspath(configPath)

def config_error():
    """ config_error(): Affiche un message d'erreur et quitte le programme """

    print("Une erreur a été détectée dans le fichier de configuration")
    exit()


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


def check_configuration(configPath):
    """ chech_configuration(PATH/TO/CONIGURATION/FILE)
        Analyse les paramètres dans le fichier yaba.conf et retourne une liste d'objet de la classe Config."""

    line            = "init"
    lineLst         = []

    # Variables temporaires de configuration
    bkpRoot              = ""
    bkpName              = ""
    bkpIgnored           = []
    bkpStoragePath       = ""
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
            if len(lineLst) < 2:
                config_error("config")
            if lineLst[0] == "default_storage_path":
                defaultStoragePath = lineLst[1]
                line = configFd.readline()
                lineLst = line.split()
                continue
            elif lineLst[0] == "root":
                bkpRoot = lineLst[1]
                line = configFd.readline()
                lineLst = line.split()
                while line != "" and line.replace(' ','') != "\n" and line != "root":
                    if lineLst[0] == "name":
                        bkpName = lineLst[1]
                    elif lineLst[0] == "ignored_files":
                        lineLst.remove("ignored_files")
                        bkpIgnored = lineLst
                    elif lineLst[0] == "storage_path":
                        bkpStoragePath = lineLst[1]
                    line = configFd.readline()
                    lineLst = line.split()
                    if bkpStoragePath == "":
                        bkpStoragePath = defaultStoragePath
                configLst.append(Config(bkpRoot, bkpIgnored, bkpStoragePath, bkpName))
                bkpRoot = ""
                bkpName = ""
                bkpStoragePath = ""
                bkpIgnored = []

            else:
                config_error("config")
        else:
            line = configFd.readline()

    print(30 * "-")
    input("Appuyez sur ENTER pour continuer")
    return configLst

