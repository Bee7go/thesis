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
        # self.generateChromosome()

    def GetSections(self):
        return self.sections

        # print(" -------------------------------- ")

        # print(self.calculateFitness(courseChromosome.sections))

    def generateChromosomeForSeminars(self, previousSections):
        for group in self.groups:
            for course in group.courseClasses:
                ok = 0
                while ok == 0:
                    workingDay = random.randint(0, len(self.workingDays) - 1)
                    timeInterval = random.randint(0, len(self.workingDays) - 1)
                    gdt2 = (group.id, self.workingDays[workingDay].id, self.timeIntervals[timeInterval].id)

                    prof = course.professors[random.randint(0, len(course.professors) - 1)]
                    pdt2 = (prof.id, self.workingDays[workingDay].id, self.timeIntervals[timeInterval].id)

                    room = self.rooms[random.randint(0, len(self.rooms) - 1)]
                    rdt2 = (room.id, self.workingDays[workingDay].id, self.timeIntervals[timeInterval].id)

                    ok = 1
                    for section1 in previousSections:
                        if ok == 0:
                            break
                        gdt1 = (section1.group.id, section1.dayOfTheWeek.id, section1.timeInterval.id)
                        pdt1 = (section1.professor.id, section1.dayOfTheWeek.id, section1.timeInterval.id)
                        rdt1 = (section1.room.id, section1.dayOfTheWeek.id, section1.timeInterval.id)

                        if gdt1 == gdt2 or pdt1 == pdt2 or rdt1 == rdt2:
                            ok = 0

                self.sections.append(
                    Section(course, copy.deepcopy(group), copy.deepcopy(prof), copy.deepcopy(room), self.workingDays[copy.deepcopy(workingDay)], self.timeIntervals[copy.deepcopy(timeInterval)]))
        # print(" -------------------------------- ")

        # print(self.calculateFitness(previousSections))

        # rdt2 = (section1.room.id, section1.dayOfTheWeek.id, section1.timeInterval.id)
        # pdt2 = (section1.professor.id, section1.dayOfTheWeek.id, section1.timeInterval.id)

    def generateChromosome(self):
        for group in self.groups:
            for course in group.courseClasses:
                self.sections.append(
                    Section(course, group, course.professors[random.randint(0, len(course.professors) - 1)],
                            self.rooms[random.randint(0, len(self.rooms) - 1)],
                            self.workingDays[random.randint(0, len(self.workingDays) - 1)],
                            self.timeIntervals[random.randint(0, len(self.timeIntervals) - 1)]))

    def calculateFitness(self, previousSections):
        # previousSections = []
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

        gdtScore = 0
        rdtScore = 0
        pdtScore = 0
        if previousSections:

            for section1 in currentSections:
                gdt1 = (section1.group.id, section1.dayOfTheWeek.id, section1.timeInterval.id)
                rdt1 = (section1.room.id, section1.dayOfTheWeek.id, section1.timeInterval.id)
                pdt1 = (section1.professor.id, section1.dayOfTheWeek.id, section1.timeInterval.id)

                for section2 in previousSections:
                    gdt2 = (section2.group.id, section2.dayOfTheWeek.id, section2.timeInterval.id)
                    rdt2 = (section2.room.id, section2.dayOfTheWeek.id, section2.timeInterval.id)
                    pdt2 = (section2.professor.id, section2.dayOfTheWeek.id, section2.timeInterval.id)

                    if gdt1 == gdt2:
                        # print("-G")
                        score += 1
                        gdtScore += 1
                    if rdt1 == rdt2:
                        # print("--R")
                        score += 1
                        rdtScore += 1

                    if pdt1 == pdt2:
                        # print("---P")
                        score += 1
                        pdtScore += 1

            # print("from prev courses: ",  gdtScore // 2 + rdtScore // 2 + pdtScore // 2)
            return gdtScore // 2 + rdtScore // 2 + pdtScore // 2
        for section in currentSections:
            gdt = (section.group.id, section.dayOfTheWeek.id, section.timeInterval.id)

            if section.professor.preferences:
                if section.dayOfTheWeek.id not in [d['dayOfTheWeek'] for d in section.professor.preferences]:
                    score += 60
                else:
                    timeIntervalsPreferences = section.professor.preferences[next((index for (index, d) in enumerate(section.professor.preferences) if d["dayOfTheWeek"] == section.dayOfTheWeek.id), None)]['timeIntervals']
                    if timeIntervalsPreferences and section.timeInterval.id not in timeIntervalsPreferences:
                        score += 30

            if gdt in gdts:
                # print("G")
                score += 1
            else:
                gdts.add((section.group.id, section.dayOfTheWeek.id, section.timeInterval.id))

            rdt = (section.room.id, section.dayOfTheWeek.id, section.timeInterval.id)
            if rdt in rdts:
                # print("R")
                score += 1
            else:
                rdts.add((section.group.id, section.dayOfTheWeek.id, section.timeInterval.id))

            pdt = (section.professor.id, section.dayOfTheWeek.id, section.timeInterval.id)
            if pdt in pdts:
                # print("P")
                score += 1
            else:
                pdts.add((section.group.id, section.dayOfTheWeek.id, section.timeInterval.id))

        # print("within score: ", score)
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

    def transformToSemiGroups(self, allSemiGroups):
        newBestChromosome = copy.deepcopy(self)
        newBestChromosome.sections = []
        for section in self.sections:
            for semigroup in section.group.transformToSemiGroups(allSemiGroups):
                newBestChromosome.sections.append(
                    Section(section.course, semigroup, section.professor, section.room, section.dayOfTheWeek,
                            section.timeInterval))
        return newBestChromosome

    def __str__(self):
        result = ''
        for section in self.sections:
            result += str(section) + '\n'
        return result
