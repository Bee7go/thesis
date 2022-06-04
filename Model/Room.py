class Room:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def GetId(self):
        return self.id

    def GetName(self):
        return self.name

    def __str__(self):
        return self.id + ' --- ' + self.name
