
class Course:
    def __init__(self, id, name, professors):
        self.id = id
        self.name = name
        self.professors = professors
        # self.numberOfParticipants = numberOfParticipants

    def GetId(self):
        return self.id

    def GetName(self):
        return self.name

    def GetProfessors(self):
        return self.professors

    def __str__(self):
        result = self.id + ' --- ' + self.name + ' --- '
        for prof in self.professors:
            result += str(prof) + ' '
        return result

    # def GetNumberOfParticipants(self):
    #     return self.numberOfParticipants