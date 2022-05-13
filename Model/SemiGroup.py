class SemiGroup:

    def __init__(self, id, name, academicYearId, groupId, labs,):
        self.id = id
        self.name = name
        self.labs = labs
        self.academicYearId = academicYearId
        self.groupId = groupId

    def AddLab(self, lab):
        self.labs.append(lab)

    def GetId(self):
        return self.id

    def GetName(self):
        return str(self.name)

    def Getlabs(self):
        return self.labs

    def __eq__(self, otherSemiGroup):
        return self.id == otherSemiGroup.id

    def __str__(self):
        result = self.id + ' --- ' + self.name + ' --- '
        for c in self.labs:
            result += str(c) + ' '
        return result


