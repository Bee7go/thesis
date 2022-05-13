import copy
import random

from Model.Section import Section


class Chromosome:

    def __init__(self, groups, rooms, workingDays, timeIntervals):
        self.sections = []  # chromosome
        self.groups = groups
        self.rooms = rooms
        self.workingDays = workingDays
        self.timeIntervals = timeIntervals
        self.generateChromosome()

    def GetSections(self):
        return self.sections

    def generateChromosome(self):
        for group in self.groups:
            for course in group.courseClasses:
                self.sections.append(
                    Section(course, group, course.professors[random.randint(0, len(course.professors) - 1)],
                            self.rooms[random.randint(0, len(self.rooms) - 1)],
                            self.workingDays[random.randint(0, len(self.workingDays) - 1)],
                            self.timeIntervals[random.randint(0, len(self.timeIntervals) - 1)]))

    def calculateFitness(self, previousSections):
        score = 0
        gdts = set()
        rdts = set()
        pdts = set()
        currentSections = self.sections
        # print("len is:")
        # if previousSections:
        #     for currentSection in currentSections:
        #         print(currentSection)
        #     print (" ------------------------------------------------ ")
        if previousSections:
            # print("previousSections")

            for section1 in currentSections:
                gdt1 = (section1.group.id, section1.dayOfTheWeek.id, section1.timeInterval.id)
                rdt1 = (section1.room.id, section1.dayOfTheWeek.id, section1.timeInterval.id)
                pdt1 = (section1.professor.id, section1.dayOfTheWeek.id, section1.timeInterval.id)

                for section2 in previousSections:
                    gdt2 = (section2.group.id, section2.dayOfTheWeek.id, section2.timeInterval.id)
                    rdt2 = (section2.room.id, section2.dayOfTheWeek.id, section2.timeInterval.id)
                    pdt2 = (section2.professor.id, section2.dayOfTheWeek.id, section2.timeInterval.id)

                    if gdt1 == gdt2:
                        # print("G")
                        score += 1
                    if rdt1 == rdt2:
                        # print("R")
                        score += 1
                    if pdt1 == pdt2:
                        # print("P")
                        score += 1

            return score
        for section in currentSections:
            gdt = (section.group.id, section.dayOfTheWeek.id, section.timeInterval.id)
            if gdt in gdts:
                score += 1
            else:
                gdts.add((section.group.id, section.dayOfTheWeek.id, section.timeInterval.id))

            rdt = (section.room.id, section.dayOfTheWeek.id, section.timeInterval.id)
            if rdt in rdts:
                score += 1
            else:
                rdts.add((section.group.id, section.dayOfTheWeek.id, section.timeInterval.id))

            pdt = (section.professor.id, section.dayOfTheWeek.id, section.timeInterval.id)
            if pdt in pdts:
                score += 1
            else:
                pdts.add((section.group.id, section.dayOfTheWeek.id, section.timeInterval.id))
        return score

    # one function for room/working day/time interval

    def mutationOnRoom(self, k):
        # random??
        for _ in range(k):
            r = random.randint(0, len(self.sections) - 1)
            old = self.sections[r].room
            new = self.rooms[random.randint(0, len(self.rooms) - 1)]
            while old == new:
                new = self.rooms[random.randint(0, len(self.rooms) - 1)]
            # print('before:')
            # print(self.sections[r].room)
            self.sections[r].room = new
            # print('after')
            # print(self.sections[r].room)

    def mutationOnWorkingDay(self, k):
        for _ in range(k):
            self.sections[random.randint(0, len(self.sections) - 1)].dayOfTheWeek = self.workingDays[
                                                                                                      random.randint(0,
                                                                                                                     len(self.workingDays) - 1)]

    def mutationOnTimeInterval(self, k):
        for _ in range(k):
            self.sections[random.randint(0, len(self.sections) - 1)].timeInterval = self.timeIntervals[
                                                                                                      random.randint(0,
                                                                                                                     len(self.timeIntervals) - 1)]

    def mutationOnProfessor(self, k):
        for _ in range(k):
            r = random.randint(0, len(self.sections) - 1)
            old = self.sections[r].professor
            # print('before:')
            # print(self.sections[r].professor)
            new = self.sections[r].course.professors[
                                    random.randint(0, len(self.sections[r].course.professors) - 1)]
            while old == new and len(self.sections[r].course.professors) - 1 > 1:
                new = self.sections[r].course.professors[
                                        random.randint(0, len(self.sections[r].course.professors) - 1)]
            self.sections[r].professor = new
            # print('after')
            # print(self.sections[r].professor)

    def __str__(self):
        result = ''
        for section in self.sections:
            result += str(section) + '\n'
        return result
