
class User:
    def __init__(self, id, userName, password, type):
        self.id = id
        self.userName = userName
        self.password = password
        self.type = type

    def GetId(self):
        return self.id

    def GetUserName(self):
        return self.userName

    def GetPassword(self):
        return self.password

    def GetType(self):
        return self.type

    def __str__(self):
        name = ""
        if self.type == "1": name = "System Administrator"
        if self.type == "2": name = "Timetable responsible"
        if self.type == "3": name = "Student"
        if self.type == "4": name = "Professor"
        return self.id + '. ' + self.userName + " -  " + name