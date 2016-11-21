#!/usr/bin/python3
# -*-coding:Utf-8 -*
import os
import hashlib

#####################
#   C L A S S E S   #
#####################

class ignore_table:

    ignoreFilesLst = []
    startsWithLst = []
    endsWithLst = []

    realIgnoredLst = []


    pass

class Config:
    """ Class de configuration
        Chaque racine à sauvegarder sera un nouvel objet de type Config
        root = Racine des fichiers à savegarder
        ignored_file = """
    def __init__(self, root, ignored_files, storage_dir, name):
        if storage_dir == "":
            print("Erreur: Aucun repertoire de stockage par défaut dans le fichier de configuration")
            exit()
        self.root         = root            # Emplacements des éléments à sauvegarder
        self.ignoredFiles = ignored_files   # Fichiers ignorés lors de la sauvegarde
        self.storage      = storage_dir     # Emplacement de la sauvegarde
        self.name         = name            # Nom de la sauvegarde
        print("---- Configuration détéctée ----")
        print("Racine:", self.root)
        print("Nom:", self.name)
        print("fihiers ignorés: ", self.ignoredFiles)
        print("Storage path: ", self.storage)
        print("\n")

class Element:
    """ what = ["FILE" | "DIR"],
        path = str("abs_path_string"),
        filename = str(nom_du_fichier"),
        md5 = str("current md5sum"),
        lastMod = last_modification_date,
        lastAcc = last_access_date,
        """
    def __init__(self, path):
        if os.path.exists(os.path.abspath(path)) is True:
            self.path = os.path.abspath(path)
            self.name = os.path.basename(path)
            if os.path.isdir(self.path) is True:
                self.what = "DIR"
            else:
                self.what = "FILE"

        if self.what == "FILE":
            self.md5 = hashlib.sha224(open(self.path, "rb").read()).hexdigest()

        self.lastMod = os.path.getmtime(self.path) # date de dernière modification
        self.lastAcc = os.path.getatime(self.path) # date de dernier accès

        print(self.what.ljust(4), " : ", self.path)
        if self.what == "FILE":
            print("md5sum = ", self.md5)

        #print("Last Acces : ", self.lastAcc)
        #print("Last Modif : ", self.lastMod)


    def inspect(self):
        return 0

    def addToIndex(self):
        return 0




