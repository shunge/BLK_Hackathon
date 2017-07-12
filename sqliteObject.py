class sqliteObj:
    IDCOUNTER = 1
    def __init__(self):
        self.ID = sqliteObj.IDCOUNTER
        self.NAME = None
        self.Univ = None
        self.MAJOR = None
        self.GPA = None
        sqliteObj.IDCOUNTER += 1

    def setName(self, name):
        self.NAME = name

    def setUniv(self, univ):
        self.Univ = univ

    def setMAJOR(self, major):
        self.MAJOR = major

    def setGPA(self, gpa):
        self.GPA = gpa
