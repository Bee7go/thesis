class TimeInterval:
    def __init__(self, id, startTime, endTime):
        self.id = id
        self.startTime = startTime
        self.endTime = endTime

    def GetId(self):
        return self.id

    def GetStartTime(self):
        return self.startTime

    def GetEndTime(self):
        return self.endTime

    def __str__(self):
        return self.id + '. [' + self.startTime + ' - ' + self.endTime + ']'