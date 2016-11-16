import os
import hashlib


class Element:
    """ what = ["FILE" | "DIR"],
        path = str("abs_path_string"),
        md5 = str("current md5sum")
        lastMod = last_modification_date
        """
    def __init__(self, path):
        if os.path.exists(os.path.abspath(path)) is True:
            self.path  = os.path.abspath(path)
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


