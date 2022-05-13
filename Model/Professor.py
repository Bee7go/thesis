class Professor:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        # self.courseClasses = courseClasses

    def GetId(self):
        return self.id

    def GetName(self):
        return self.name


    # def AddCourseClass(self, courseClass):
    #     self.courseClasses.append(courseClass)
    #
    # def GetCourseClasses(self):
    #     return self.courseClasses

    def __eq__(self, otherProfessor):
        return self.id == otherProfessor.id

    def __str__(self):
        return self.id + ' --- ' + self.name
