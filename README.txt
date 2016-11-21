Yet Another Backup Assistant:
-----------------------------

- Language : Dans une optique d'apprentissage, le projet sera réalisé dans 2 langages afin de bien en saisir leurs subtilités ainsi que leurs différences de manière concrète. Dans un premier temps en Python3 puis en C++

- Fonctionnement:
    La principale difficulté sera de déterminer le fonctionnement global du soft. Toute idée sera la bienvenue!
    Il faut pouvoir sauvegarder plusieurs racines. Ces racines seront séparées dans la racine de stockage des sauvegardes
    Exemple: Pour sauver les racines /home/toto sous le nom NAME1 et /var/mail/ sous le nom NAME2, 2 dossiers seront créés en racine de sauvegarde (/backup dans l'exemple), et un fichier d'index y sera placé.On aura donc l'arborescence ci-dessous :
    /backup
    /backup/NAME1/index.yaba
    /backup/NAME1/NAME1.tar.gz
    /backup/NAME2/index.yaba
    /backup/NAME2/NAME2.tar.gz

- Compression des fichiers sauvegardés:
    Les fichiers sauvegardés seront archivés au format .tar.bz2
    LA lib tarfile permet de compresser les éléments directement.

- Détection des fichiers modifiés ou non (sommes de hachage)

- Un index de fichiers qui gère les ajouts/modifications sous la forme :
    PATH:taille:MD5:DATE

    PATH sera le chemin absolu du fichier en partant de la racine à sauvegarder.
    exemple:
        Si l'on sauvegarde le dossier /home/toto/docs/,
        pour le fichier : /home/toto/docs/musique/dead_chickens.ogg sera :
        PATH = /musique/dead_chickens.ogg

- Fichier de conf : -> /etc/yaba/yaba.conf (à terme... En attendant il sera dans le rep courant du script). Il contiendra les informations ci-dessous :
    - l'emplacement de stockage par défaut des sauvegardes
    - Une ou plusieurs sauvegardes pour lesquels apparaitront les informations ci-dessous:
        - Chemins vers les répertoires à sauvegarder
        - Chemin vers la sauvegarde
        - Fichiers à ignore
        - Nom de la sauvegarde

- Que faire des liens symboliques??


