class SemiGroup:

    def __init__(self, id, name, academicYearId, groupId, courseClasses):
        self.id = id
        self.name = name
        self.courseClasses = courseClasses
        self.academicYearId = academicYearId
        self.groupId = groupId

    def AddLab(self, lab):
        self.courseClasses.append(lab)

    def GetId(self):
        return self.id

    def GetName(self):
        return str(self.name)

    def Getlabs(self):
        return self.courseClasses

    def transformToSemiGroups(self, allSemiGroups):
        semigroups = []
        for semigroup in allSemiGroups:
            if semigroup.id == self.id:
                semigroups.append(semigroup)
        return semigroups

    def __eq__(self, otherSemiGroup):
        return self.id == otherSemiGroup.id

    def __str__(self):
        result = self.id + ' --- ' + self.name + ' --- Courses: '
        for c in self.courseClasses:
            result += c.id + '. ' + c.name + ', '
        return result


