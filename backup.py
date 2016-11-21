#!/usr/bin/python3
# -*-coding:Utf-8 -*
import os
from objects import *
from backup import *


def check_ignored(name):
    """ compare 'name' à la liste de fichiers à ignorer """
    pass
    # Plutôt qu'une fonction, définir une class ignore_table() avec une méthode check(name)

def walk(element_, ignoredLst_):
    """ walk(element, ignoredLst): -> list of "Element"
        element is an object from class Element that contain the root path du walk through.
        ignoredLst is a list op strings of the king of files to ignore.
        Parse the tree to backup starting at the root from the element given in argument,
        and returns a list of all files and dirs as Objects from class 'Element' """

    ignoreFilesLst = []
    startsWithLst = []
    endsWithLst = []

    finalIgnoredLst = []

    # AJOUTER ICI LES DIVERS LISTES DE FICHIERS A IGNORER
    for string in ignoredLst_: #{
        if "*" in string: #{
            if string[0] == "*":
                endsWithLst.append(string.replace('*',''))
            elif string[-1] == "*":
                startsWithLst.append(string.replace('*',''))
        else:
            ignoreFilesLst.append(string)

    def check_blacklist(name):#{
        """ check_name(name) where name is a string with the file name to compare to blacklist """
        for word in ignoreFilesLst: #{
            if name == word: #{
                finalIgnoredLst.append(name)
                return -1
            #}
        #}
        for word in startsWithLst: #{
            if name.startswith(word) is True: #{
                finalIgnoredLst.append(name)
                return -1
            #}
        #}
        for word in endsWithLst: #{
            if name.endswith(word): #{
                finalIgnoredLst.append(name)
                return -1
            #}
        #}
        return 1
    #}


# ON PARCOURE L'ARBORESCENCE À SAUVEGARDER
    tree = []
    tree.append(element_)


    if element_.what == "FILE" and check_blacklist(element.name):
       return tree

    for element_ in tree: #{
        if element_.what == "DIR" and check_blacklist(element_.name)== 1: #{
            for some in os.listdir(element_.path): #{
                if check_blacklist(some) == 1: #{
                    tree.append(Element(os.path.join(element_.path, some)))
                #}
            #}
        #}
    #}

    #print("Fichiers ignorés :")
    #print("Portant les noms: ", ignoreFilesLst)
    #print("Fichiers Comencants par :", startsWithLst)
    #print("Fichiers finissants par :", endsWithLst)
    #print("Les fichiers suivants ont été ignorés :", finalIgnoredLst)
    return tree



