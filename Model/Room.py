class Room:

    def __init__(self, id, name, numberOfSeats, isLab):
        self.id = id
        self.name = name
        self.numberOfSeats = numberOfSeats
        self.isLab = isLab


    def GetId(self):
        return self.id

    def GetName(self):
        return self.name

    def checkIfLab(self):
        return self.isLab

    def GetNumberOfSeats(self):
        return int(self.numberOfSeats)

    def __str__(self):
        return self.id + ' --- ' + self.name + ' --- ' + self.numberOfSeats + ' --- ' + self.isLab
