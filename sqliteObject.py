class sqliteObj:
    IDCOUNTER = 1

    def __init__(self):
        self.ID = sqliteObj.IDCOUNTER
        self.NAME = "NULL"
        self.Univ = "NULL"
        self.MAJOR = "NULL"
        self.GPA = "NULL"
        sqliteObj.IDCOUNTER += 1

    def setName(self, name):
        self.NAME = name

    def setUniv(self, univ):
        self.Univ = univ

    def setMAJOR(self, major):
        self.MAJOR = major

    def setGPA(self, gpa):
        self.GPA = gpa

    def getID(self):
        return self.ID

    def getNAME(self):
        return self.NAME

    def getUniv(self):
        return self.Univ

    def getMAJOR(self):
        return self.MAJOR

    def getGPA(self):
        return self.GPA
