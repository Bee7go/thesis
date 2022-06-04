
class Course:
    def __init__(self, id, name, professors):
        self.id = id
        self.name = name
        self.professors = professors

    def GetId(self):
        return self.id

    def GetName(self):
        return self.name

    def GetProfessors(self):
        return self.professors

    def __str__(self):
        result = self.id + ' --- ' + self.name + ' --- Professors: '
        for prof in self.professors:
            result += prof.id + '. ' + prof.name + ', '
        return result
