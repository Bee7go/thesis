class AcademicYear:

    def __init__(self, id, name, courseClasses):
        self.id = id
        self.name = name
        self.courseClasses = courseClasses

    def AddClass(self, courseClass):
        self.courseClasses.append(courseClass)

    def GetId(self):
        return self.id

    def GetName(self):
        return str(self.name)

    def GetCourseClasses(self):
        return self.courseClasses

    def transformToSemiGroups(self, allSemiGroups):
        semigroups = []
        for semigroup in allSemiGroups:
            if semigroup.academicYearId == self.id:
                semigroups.append(semigroup)
        return semigroups

    def __eq__(self, otherGroup):
        return self.id == otherGroup.id

    def __str__(self):
        result = 'id: ' + self.id + ' --- ' + self.name + ' --- Courses: '
        for c in self.courseClasses:
            result += c.id + '. ' + c.name + ', '
        return result
