class Professor:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.preferences = []

    def GetId(self):
        return self.id

    def GetName(self):
        return self.name

    def addPreferences(self, preference):
        self.preferences.append(preference)

    def __eq__(self, otherProfessor):
        return self.id == otherProfessor.id

    def __str__(self):
        return self.id + ' --- ' + self.name
