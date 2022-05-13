class Section:

    def __init__(self, course, group, professor, room, dayOfTheWeek, timeInterval):
        self.professor = professor
        self.course = course
        self.group = group
        self.room = room
        self.dayOfTheWeek = dayOfTheWeek
        self.timeInterval = timeInterval

    def GetCourse(self):
        return self.course

    def GetProfessor(self):
        return self.professor

    def GetGroup(self):
        return self.group

    def GetRoom(self):
        return self.room

    def GetDayOfTheWeek(self):
        return self.dayOfTheWeek

    def GetTimeInterval(self):
        return self.timeInterval

    def __str__(self):
        # return 'Group ' + self.group.name + ' will have the course of ' + self.course.name + ' on ' +\
        #        self.dayOfTheWeek.name + ' in time interval [' + self.timeInterval.startTime + '-' + self.timeInterval.endTime +\
        #        '] with professor ' + self.professor.name + ' in room ' + self.room.name

        return self.group.name + ' | course:' + self.course.name + ' | day: ' + \
               self.dayOfTheWeek.name + ' | [' + self.timeInterval.startTime + '-' + self.timeInterval.endTime + \
               '] | professor: ' + self.professor.name + ' | room: ' + self.room.name
