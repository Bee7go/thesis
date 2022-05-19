import copy
import csv
import pickle
import random
import time

from Model.AcademicYear import AcademicYear
from Model.Course import Course
from Model.DayOfTheWeek import DayOfTheWeek
from Model.Group import Group
from Model.History import History
from Model.Population import Population
from Model.Professor import Professor
from Model.Room import Room
from Model.SemiGroup import SemiGroup
from Model.TimeInterval import TimeInterval
from Model.User import User
from Model.UserType import UserType
from Model.ValidResult import ValidResult

history = History(10)


def csvFile():
    # file = open('Data/possible_courses.csv')
    # rows = csv.reader(file)
    # courses = []
    # courses_name = []
    #
    # for course in rows:
    #     courseProfessors = []
    #     courses.append(Course(course[0], course[1], courseProfessors))
    #     courses_name.append(course[1])
    # print(course[1])

    # professors
    file = open('Data/possible_professors.csv')
    rows = csv.reader(file)
    professors = []
    professors_name = []
    for professor in rows:
        professors.append(Professor(professor[0], professor[1]))
        professors_name.append(professor[1])

    print(professors_name)

    # ------------------------

    file2 = open('Data/possible_courses.csv', 'w', newline='')
    writer = csv.writer(file2)

    file3 = open('Data/possible_academicYears.csv', 'w', newline='')
    writer3 = csv.writer(file3)
    idAcademicYears = 0

    file5 = open('Data/possible_semigroups.csv', 'w', newline='')
    writer5 = csv.writer(file5)
    idSemigroups = 0

    # file4 = open('Data/possible_groups.csv', 'w', newline='')
    # writer4 = csv.writer(file4)
    # idGroups = 0

    file4 = open('Data/possible_groups.csv')
    rows = csv.reader(file4)
    groups = []
    groups_name = []

    for group in rows:
        groups.append(Group(group[0], group[1], []))
        groups_name.append(group[1])

    file = open('Data/aux_possible_professors.csv', 'r+')
    # fileUpdated = open('Data/possible_professors.csv', 'w',newline='')
    # writer = csv.writer(fileUpdated)
    rows = csv.reader(file)

    id = 0
    academicYears = []
    academicYears_name = []
    # groups = []
    semigrups = []
    semigrups_name = []
    currentAcademicYear = -1
    currentgroup = -1
    for all_data in rows:
        formatii = all_data[10][:-1]
        if len(formatii) in (3, 4) and formatii.lower().islower():
            all_profs_name = set()
            profs_ids = []
            for prof in all_data[9].split(';'):
                if prof != '' and prof not in all_profs_name:
                    profs_ids.append(professors_name.index(prof))
                    all_profs_name.add(prof)

            if profs_ids:
                writer.writerow([id, all_data[2] + ' curs', ','.join(str(e) for e in profs_ids)])
                # print(all_data[2] + ' curs') # cursuri

                academic_year = formatii
                if academic_year not in academicYears_name:
                    academicYears.append(AcademicYear(idAcademicYears, academic_year, [id]))
                    academicYears_name.append(academic_year)
                    currentAcademicYear = idAcademicYears
                    idAcademicYears += 1
                else:
                    academicYears[academicYears_name.index(academic_year)].courseClasses.append(id)

                id += 1



        elif "/" in formatii:
            # print("semigrupa " + formatii)

            all_profs_name = set()
            profs_ids = []
            for prof in all_data[9].split(';'):
                if prof != '' and prof not in all_profs_name:
                    profs_ids.append(professors_name.index(prof))
                    all_profs_name.add(prof)

            if profs_ids:
                writer.writerow([id, all_data[2] + ' lab', ','.join(str(e) for e in profs_ids)])
                for semi_grupa in formatii.split(';'):

                    if semi_grupa not in semigrups_name:
                        semigrups.append(
                            SemiGroup(idSemigroups, semi_grupa, currentAcademicYear,
                                      groups[groups_name.index(semi_grupa.split('/')[0])].id, [id]))
                        semigrups_name.append(semi_grupa)
                        idSemigroups += 1
                    else:
                        semigrups[semigrups_name.index(semi_grupa)].courseClasses.append(id)

                    print(semi_grupa + ' groupId ' + str(
                        groups[groups_name.index(semi_grupa.split('/')[0])].id) + ' academicYearID: ' + str(
                        currentAcademicYear) + " lab " + str(id))  # laburi

                id += 1



        elif len(formatii) > 2:
            all_profs_name = set()
            profs_ids = []
            for prof in all_data[9].split(';'):
                if prof != '' and prof not in all_profs_name:
                    profs_ids.append(professors_name.index(prof))
                    all_profs_name.add(prof)

            if profs_ids:
                writer.writerow([id, all_data[2] + ' seminar', ','.join(str(e) for e in profs_ids)])
                # print(all_data[2] + ' seminar')  # seminare

                id += 1

    for academicYear in academicYears:
        writer3.writerow([academicYear.id, academicYear.name, ','.join(str(e) for e in academicYear.courseClasses)])

    for semi_grupa in semigrups:
        writer5.writerow([semi_grupa.id, semi_grupa.name, semi_grupa.academicYearId, semi_grupa.groupId,
                          ','.join(str(e) for e in semi_grupa.courseClasses)])

    # print (" ----- got here: ")
    # idGroups = 0
    # for group in groups:
    #     for group_name in group.name.split(';'):
    #         writer4.writerow([idGroups, group_name, ','.join(str(e) for e in group.courseClasses)])
    #         idGroups += 1

    # --------------------------------
    # id = 0
    # for professor in rows:
    #     # print(professor[2] + ' ' + professor[10])
    #     if professor[2] in courses_name:
    #         index = courses_name.index(professor[2])
    #         if index:
    #             for elem in professor[9].split(';'):
    #                 if elem != '':
    #                     p = professors[professors_name.index(elem)]
    #                     courses[index].professors.append(p)
    #         print(courses[index])
    #         # for elem in professor[9].split(';'):
    #         #     if elem not in professors_name and elem != '':
    #         #         professors_name.add(elem)
    #         #
    #         #         writer.writerow([id, elem])
    #         #         id+=1
    #         #         print(elem)


#csvFile()


def saveCurrentVariablesToPickle(N, C, M, K, G, currentSol):
    filename = 'currentVariables.pk'

    with open(filename, 'wb') as fi:
        # dump your data into the file
        pickle.dump([N, C, M, K, G, currentSol], fi)


def loadCurrentVariablesFromPickle():
    filename = 'currentVariables.pk'

    with open(filename, 'rb') as fi:
        return pickle.load(fi)


def BETAfindNewBestTimetable(academicYears, groups, semigroups, rooms, workingDays, timeIntervals, currentN, currentC,
                             currentM, currentK, currentG):
    # currentN = 10
    # currentM = 1

    # currentG = 70

    print('currentN')
    print(currentN)
    print('currentC')
    print(currentC)
    print('currentM')
    print(currentM)
    print('currentK')
    print(currentK)
    print('currentG')
    print(currentG)

    fitnessTotal = -1
    groupFitness = -1
    courseFitness = -1

    start_time = time.time()
    print('searching started ....')
    while fitnessTotal != 0:
        while groupFitness != 0:
            while courseFitness != 0:
                nr_of_generations = currentG
                p1 = Population(currentN, academicYears, rooms, workingDays, timeIntervals)
                p1.generatePopulationForCourses()
                while nr_of_generations and p1.bestFitness != 0:
                    nrOfParents = currentC
                    while nrOfParents:
                        parent1 = p1.chromosomes[random.randint(0, currentN - 1)]
                        parent2 = p1.chromosomes[random.randint(0, currentN - 1)]
                        offsprings = p1.crossover(parent1, parent2, 1, 2)
                        p1.addChromosome(offsprings[0])
                        p1.addChromosome(offsprings[1])
                        nrOfParents -= 1

                    mutatedChromosomes = currentM
                    while mutatedChromosomes:
                        mc = p1.chromosomes[random.randint(0, currentN - 1)]
                        # mc.mutationOnRoom(4)
                        mc.mutationOnWorkingDay(3)
                        mc.mutationOnTimeInterval(2)
                        # mc.mutationOnProfessor(5)
                        p1.addChromosome(mc)
                        mutatedChromosomes -= 1

                    p1.getBestKChromosomes(currentK, [], semigroups)
                    p1.preparePopulationForNextGenerationCourses()

                    nr_of_generations -= 1
                    print('setting courses ....')
                    print('- best so far: ', p1.bestFitness)

                p1toSemiGroups = p1.bestChromosome.transformToSemiGroups(semigroups)
                courseFitness = p1.bestFitness
                # print('best solution is:\n', p1.bestChromosome)
                # print('best fitness is: ', p1.bestFitness)

            currentN = 80
            currentC = 10
            currentM = 90
            currentK = 80
            currentG = 200
            nr_of_generations = currentG
            p2 = Population(currentN, groups, rooms, workingDays, timeIntervals)
            p2.generatePopulationForSeminars(p1toSemiGroups.sections)
            while nr_of_generations and p2.bestFitness != 0:
                nrOfParents = currentC
                while nrOfParents:
                    r = random.randint(0, currentN - 1)
                    parent1 = copy.deepcopy(p2.chromosomes[r])
                    r = random.randint(0, currentN - 1)
                    parent2 = copy.deepcopy(p2.chromosomes[r])
                    offsprings = p2.crossover(parent1, parent2, 2, 7)
                    p2.addChromosome(offsprings[0])
                    p2.addChromosome(offsprings[1])
                    nrOfParents -= 1

                mutatedChromosomes = currentM
                while mutatedChromosomes:
                    mc = copy.deepcopy(p2.chromosomes[random.randint(0, currentN - 1)])
                    # mc.mutationOnRoom(4)
                    mc.mutationOnWorkingDay(4)
                    mc.mutationOnTimeInterval(4)
                    # mc.mutationOnProfessor(5)
                    p2.addChromosome(mc)
                    mutatedChromosomes -= 1

                p2.getBestKChromosomes(currentK, p1toSemiGroups.sections, semigroups)
                p2.preparePopulationForNextGenerationSeminars(p1toSemiGroups.sections)
                nr_of_generations -= 1
                print('setting seminars ....')
                print('- best so far: ', p2.bestFitness)


            # print('best solution is:\n', p2.bestChromosome)
            p2toSemiGroups = p2.bestChromosome.transformToSemiGroups(semigroups)
            groupFitness = p2.bestFitness
            courseFitness = -1

        # --------------------------

        currentN = 300
        currentC = 20
        currentM = 200
        currentK = 80
        currentG = 2000
        print("got to labs")

        nr_of_generations = currentG
        p3 = Population(currentN, semigroups, rooms, workingDays, timeIntervals)
        p3.generatePopulationForSeminars(p1toSemiGroups.sections + p2toSemiGroups.sections)

        while nr_of_generations and p3.bestFitness != 0:
            nrOfParents = currentC
            while nrOfParents:
                parent1 = copy.deepcopy(p3.chromosomes[random.randint(0, currentN - 1)])
                parent2 = copy.deepcopy(p3.chromosomes[random.randint(0, currentN - 1)])
                offsprings = p3.crossover(parent1, parent2, 2, 7)
                p3.addChromosome(offsprings[0])
                p3.addChromosome(offsprings[1])
                nrOfParents -= 1

            mutatedChromosomes = currentM
            while mutatedChromosomes:
                mc = copy.deepcopy(p3.chromosomes[random.randint(0, currentN - 1)])
                # mc.mutationOnRoom(4)
                mc.mutationOnWorkingDay(10)
                mc.mutationOnTimeInterval(12)
                # mc.mutationOnProfessor(5)
                p3.addChromosome(mc)
                mutatedChromosomes -= 1

            p3.getBestKChromosomes(currentK, p1toSemiGroups.sections + p2toSemiGroups.sections, semigroups)
            # p3.preparePopulationForNextGenerationCourses()
            p3.preparePopulationForNextGenerationSeminars(p1toSemiGroups.sections + p2toSemiGroups.sections)

            nr_of_generations -= 1
            print('setting labs ....')
            print('- best so far: ', p3.bestFitness)

        fitnessTotal = p3.bestFitness
        groupFitness = -1
        courseFitness = -1

    print('best solution is:\n', p3.bestChromosome)
    print(p2.bestChromosome)
    print(p1.bestChromosome)

    # p3.bestChromosome = p3.bestChromosome.transformToSemiGroups(semigroups)
    # print('best solution is:\n', p3.bestChromosome)
    # print(p1.bestChromosome)
    print('best fitness is: ', p3.bestFitness)

    vR = ValidResult(currentN, currentC, currentM, currentK, currentG, 0, time.time() - start_time)

    if history.updateResultIfBetter(vR):
        print("--> New solution is in top!\n")
    else:
        print("--> New solution found is not in top!\n")
    history.showTable()
    return {"bestSolution": p3.bestChromosome, "bestFitness": p3.bestFitness, "solving time": time.time() - start_time}


def findNewBestTimetable(groups, rooms, workingDays, timeIntervals, currentN, currentC, currentM, currentK, currentG):
    print('currentN')
    print(currentN)
    print('currentC')
    print(currentC)
    print('currentM')
    print(currentM)
    print('currentK')
    print(currentK)
    print('currentG')
    print(currentG)

    nr_of_generations = currentG
    start_time = time.time()

    p = Population(currentN, groups, rooms, workingDays, timeIntervals)

    while nr_of_generations and p.bestFitness != 0:
        nrOfParents = currentC
        while nrOfParents:
            parent1 = copy.deepcopy(p.chromosomes[random.randint(0, currentN - 1)])
            parent2 = copy.deepcopy(p.chromosomes[random.randint(0, currentN - 1)])
            offsprings = p.crossover(parent1, parent2, 7, 17)
            p.addChromosome(offsprings[0])
            p.addChromosome(offsprings[1])
            nrOfParents -= 1

        mutatedChromosomes = currentM
        while mutatedChromosomes:
            mc = copy.deepcopy(p.chromosomes[random.randint(0, currentN - 1)])
            mc.mutationOnRoom(4)
            mc.mutationOnWorkingDay(3)
            mc.mutationOnTimeInterval(2)
            mc.mutationOnProfessor(5)
            p.addChromosome(mc)
            mutatedChromosomes -= 1

        p.getBestKChromosomes(currentK)
        p.preparePopulationForNextGeneration()

        nr_of_generations -= 1

    # print('solution found in: ', time.time() - start_time)
    # print('best fitness is: ', p.bestFitness)
    # print('best solution is:\n', p.bestChromosome)

    vR = ValidResult(currentN, currentC, currentM, currentK, currentG, p.bestFitness, time.time() - start_time)

    if history.updateResultIfBetter(vR):
        print("--> New solution is in top!\n")
    else:
        print("--> New solution found is not in top!\n")
    # history.showTable()
    return {"bestSolution": p.bestChromosome, "bestFitness": p.bestFitness, "solving time": time.time() - start_time}


def adminMenu():
    print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
    print("Hello admin! Select an option listed below: ")
    print("1. Changes on algorithm")
    print("2. See results")
    print("3. Manage accounts")


def timetableResponsibleMenu():
    print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
    print("Hello timetable responsible! Select an option listed below: ")
    print("1. Changes on dataset")
    print("2. See results")


def studentsMenu():
    print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
    print("Hello student! Select an option listed below: ")
    print("1. See results")


def professorsMenu():
    print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
    print("Hello professor! Select an option listed below: ")
    print("1. See results")
    print("2. Set preferences ???")


def changesOnAlgorithmMenu():
    print("1. Set the number of individuals in the population (N)")
    print("2. Set the number of new offsprings (C)")
    print("3. Set the number of individuals to perform mutations on (M)")
    print("4. Set the number of solutions to be passed to the next generation on selection (K)")
    print("5. Set the number of generations (G)")
    print("6. Go back")

def changesOnDataSetMenu():
    print("1. Modify rooms list")
    print("2. Modify professors list")
    print("3. Modify courses list")
    print("4. Modify academic years list")
    print("5. Modify groups list")
    print("6. Modify semi-groups list")
    print("7. Go back")

def operationsOnEachDataSetMenu(element):
    print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
    print("1. Add a new " + element)
    print("2. Update an existing " + element)
    print("3. Delete an existing " + element)
    print("4. Show list of all " + element + "s")
    print("5. Go back")



def main():
    # setup
    currentVariables = loadCurrentVariablesFromPickle()
    # currentN = currentVariables[0]
    # currentC = currentVariables[1]
    # currentM = currentVariables[2]
    # currentK = currentVariables[3]
    # currentG = currentVariables[4]
    # currentSol = currentVariables[5]

    # foarte ok pt seminare:
    # currentN = 100
    # currentC = 10
    # currentM = 90
    # currentK = 90
    # currentG = 200


    currentN = 100
    currentC = 10
    currentM = 90
    currentK = 90
    currentG = 200
    currentSol = currentVariables[5]

    # time intervals
    file = open('Data/timeIntervals.csv')
    rows = csv.reader(file)
    timeIntervals = []
    for timeInterval in rows:
        timeIntervals.append(TimeInterval(timeInterval[0], timeInterval[1], timeInterval[2]))
        # print(str(timeIntervals[len(timeIntervals) - 1]))

    # working days
    file = open('Data/workingDaysOfTheWeek.csv')
    rows = csv.reader(file)
    workingDays = []
    for dayOfTheWeek in rows:
        workingDays.append(DayOfTheWeek(dayOfTheWeek[0], dayOfTheWeek[1]))


    # professors
    file = open('Data/professors.csv')
    rows = csv.reader(file)
    professors = []
    for professor in rows:
        professors.append(Professor(professor[0], professor[1]))
        # print(str(professors[len(professors) - 1]))
    professors[2].addPreferences({'dayOfTheWeek': workingDays[1].id, 'timeIntervals': [timeIntervals[0].id, timeIntervals[1].id]})
    professors[2].addPreferences({'dayOfTheWeek': workingDays[3].id, 'timeIntervals': [timeIntervals[2].id, timeIntervals[4].id]})
    print(professors[2])


    # courses
    file = open('Data/courses.csv')
    rows = csv.reader(file)
    courses = []

    for course in rows:
        courseProfessors = []
        for professor in course[2:]:
            for p in professors:
                if p.id == professor:
                    courseProfessors.append(p)

        courses.append(Course(course[0], course[1], courseProfessors))
        # print(str(courses[len(courses) - 1]))

    # academic years
    file = open('Data/academicYears.csv')
    rows = csv.reader(file)
    academicYears = []

    for academicYear in rows:
        academicYearCourses = []
        for course in academicYear[2:]:
            for c in courses:
                if c.id == course:
                    academicYearCourses.append(c)

        academicYears.append(AcademicYear(academicYear[0], academicYear[1], academicYearCourses))
        # print(str(academicYears[len(academicYears) - 1]))

    # groups
    file = open('Data/groups.csv')
    rows = csv.reader(file)
    groups = []
    for group in rows:
        groupCourses = []
        for course in group[1:]:
            for c in courses:
                if c.id == course:
                    groupCourses.append(c)

        groups.append(Group(group[0], group[1], groupCourses))

        print(str(groups[len(groups) - 1]))

    # semi-groups
    file = open('Data/semigroups.csv')
    rows = csv.reader(file)
    semigroups = []
    for semigroup in rows:
        semigroupCourses = []
        for course in semigroup[4:]:
            for c in courses:
                if c.id == course:
                    semigroupCourses.append(c)

        semigroups.append(SemiGroup(semigroup[0], semigroup[1], semigroup[2], semigroup[3], semigroupCourses))
        # print(str(semigroupCourses[0]))

    # rooms
    file = open('Data/rooms.csv')
    rows = csv.reader(file)
    rooms = []
    for room in rows:
        rooms.append(Room(room[0], room[1], room[2]))
        # print(str(rooms[len(rooms) - 1]))



    # user types
    file = open('Data/userTypes.csv')
    rows = csv.reader(file)
    userTypes = []
    for userType in rows:
        userTypes.append(UserType(userType[0], userType[1]))

    # users
    file = open('Data/users.csv')
    rows = csv.reader(file)
    users = []
    for user in rows:
        users.append(User(user[0], user[1], user[2], user[3]))
        # print(str(users[len(users) - 1]))

    # --------------------------------------------------------------------

    # p = Population(N, groups, rooms, workingDays, timeIntervals)
    # print(str(p))
    # p.calculateFitnessScores()
    # p.getBestKChromosomes(3)
    # print(str(p))

    # c1 = Chromosome(groups, rooms, workingDays, timeIntervals)
    # print(str(c1))

    # c2 = Chromosome(groups, rooms, workingDays, timeIntervals)
    # print(str(c2))

    # res = p.crossover(c1, c2, 7, len(c1.sections))
    # res = p.crossover(c1, c2, 7, 15)
    # print(str(res[0]))
    # print(str(res[1]))

    # ---------------------------------------------

    # findNewBestTimetable(groups, rooms, workingDays, timeIntervals, currentN, currentC, currentM, currentK, currentG)
    # BETAfindNewBestTimetable(academicYears, groups, semigroups, rooms, workingDays, timeIntervals, currentN, currentC,
    #                            currentM, currentK, currentG)
    # history = History(3)
    # vR = ValidResult(120, "one-point", 11, 44, 54, 0, 0.22)
    # history.updateResultIfBetter(vR)
    # history.showTable()

    # ---------------------------------------------
    # menu:
    print("\nWelcome to the timetable application! Please provide your userName and password in order to login:")

    # login:
    currentUser = ""
    while currentUser == "":
        userName = input("userId: ")
        userPassword = input("password: ")
        for user in users:
            if user.userName == userName and user.password == userPassword:
                currentUser = user
        if currentUser == "":
            print("User not found! Please try again to login!")

    # system admin:
    if currentUser.type == "1":
        while True:
            adminMenu()
            adminUserChoice = int(input("=> choice: "))
            if adminUserChoice == 1:
                while True:
                    print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                    print("Select an option listed below: ")
                    changesOnAlgorithmMenu()
                    changesOnAlgorithmUserChoice = int(input("=> choice: "))
                    print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                    if changesOnAlgorithmUserChoice == 1:
                        N = int(input("N = "))
                        print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                        currentN = N
                        currentSol = \
                            BETAfindNewBestTimetable(academicYears, groups, semigroups, rooms, workingDays,
                                                     timeIntervals,
                                                     currentN, currentC,
                                                     currentM, currentK, currentG)["bestSolution"]
                        saveCurrentVariablesToPickle(currentN, currentC, currentM, currentK, currentG,
                                                     currentSol)

                    if changesOnAlgorithmUserChoice == 2:
                        C = int(input("C = "))  # check if smaller than N
                        print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                        currentC = C
                        currentSol = \
                            BETAfindNewBestTimetable(academicYears, groups, semigroups, rooms, workingDays,
                                                     timeIntervals,
                                                     currentN, currentC,
                                                     currentM, currentK, currentG)["bestSolution"]
                        saveCurrentVariablesToPickle(currentN, currentC, currentM, currentK, currentG,
                                                     currentSol)

                    if changesOnAlgorithmUserChoice == 3:
                        M = int(input("M = "))
                        print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                        currentM = M
                        currentSol = \
                            BETAfindNewBestTimetable(academicYears, groups, semigroups, rooms, workingDays,
                                                     timeIntervals,
                                                     currentN, currentC,
                                                     currentM, currentK, currentG)["bestSolution"]
                        saveCurrentVariablesToPickle(currentN, currentC, currentM, currentK, currentG,
                                                     currentSol)

                    if changesOnAlgorithmUserChoice == 4:
                        K = int(input("K = "))
                        print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                        currentK = K
                        currentSol = \
                            BETAfindNewBestTimetable(academicYears, groups, semigroups, rooms, workingDays,
                                                     timeIntervals,
                                                     currentN, currentC,
                                                     currentM, currentK, currentG)["bestSolution"]
                        saveCurrentVariablesToPickle(currentN, currentC, currentM, currentK, currentG,
                                                     currentSol)

                    if changesOnAlgorithmUserChoice == 5:
                        G = int(input("G = "))
                        print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                        currentG = G
                        currentSol = \
                            BETAfindNewBestTimetable(academicYears, groups, semigroups, rooms, workingDays,
                                                     timeIntervals,
                                                     currentN, currentC,
                                                     currentM, currentK, currentG)["bestSolution"]
                        saveCurrentVariablesToPickle(currentN, currentC, currentM, currentK, currentG,
                                                     currentSol)

                    if changesOnAlgorithmUserChoice == 6:
                        break

            if adminUserChoice == 2:
                print(currentSol)
            if adminUserChoice == 3:
                while True:
                    operationsOnEachDataSetMenu("account")
                    operationOnAccount = int(input("=> choice: "))
                    print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                    if operationOnAccount == 1:  # add
                        accountNewName = input("=> new username to be set: ")
                        accountPassword = input("=> new password to be set: ")
                        accountType = input("=> new account type (1 System Administrator, 2 Timetable responsible, 3 Student, 4 Professor): ")
                        print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                        idToAdd = int(users[len(users) - 1].id) + 1

                        users.append(User(str(idToAdd), accountNewName, accountPassword, accountType))
                        print("User created successfully!")

                    if operationOnAccount == 2:  # update
                        idToUpdate = input("=> userId to be updated: ")
                        accountNewName = input("=> new username to be set: ")
                        accountPassword = input("=> new password to be set: ")
                        accountType = input("=> new account type (1 System Administrator, 2 Timetable responsible, 3 Student, 4 Professor): ")
                        print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                        for user in users:
                            if user.id == idToUpdate:
                                user.userName = accountNewName
                                user.password = accountPassword
                                user.type = accountType
                                break
                        print("User updated successfully!")

                    if operationOnAccount == 3:  # delete
                        idToDelete = input("=> userId to be deleted: ")
                        print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                        for user in users:
                            if user.id == idToDelete:
                                users.remove(user)
                                break
                        print("User deleted successfully!")

                    if operationOnAccount == 4:  # show
                        for user in users:
                            print(str(user))
                    if operationOnAccount == 5:
                        break



    # timetable responsible:
    if currentUser.type == "2":
        while True:
            timetableResponsibleMenu()
            timetableResponsibleChoice = int(input("=> choice: "))
            if timetableResponsibleChoice == 1:
                while True:
                    print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                    print("Select an option listed below: ")
                    changesOnDataSetMenu()
                    changesOnDataSetChoice = int(input("=> choice: "))
                    if changesOnDataSetChoice == 1:
                        while True:
                            operationsOnEachDataSetMenu("room")
                            operationOnRoom = int(input("=> choice: "))
                            print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                            if operationOnRoom == 1: #add
                                roomNewName = input("=> new name to be set: ")
                                print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                                idToAdd = int(rooms[len(rooms)-1].id) + 1

                                rooms.append(Room(str(idToAdd), roomNewName, '0'))
                                print("Room created successfully!")

                            if operationOnRoom == 2: #update
                                idToUpdate = input("=> roomId to be updated: ")
                                roomNewName = input("=> new name to be set: ")
                                print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                                for room in rooms:
                                    if room.id == idToUpdate:
                                        room.name = roomNewName
                                        break
                                print("Room updated successfully!")


                            if operationOnRoom == 3: #delete
                                idToDelete = input("=> roomId to be deleted: ")
                                print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                                for room in rooms:
                                    if room.id == idToDelete:
                                        rooms.remove(room)
                                        break
                                print("Room deleted successfully!")

                            if operationOnRoom == 4: #show
                                for room in rooms:
                                    print(str(room))
                            if operationOnRoom == 5:
                                break


                    if changesOnDataSetChoice == 2:
                        while True:
                            operationsOnEachDataSetMenu("professor")
                            operationOnProfessor = int(input("=> choice: "))
                            print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                            if operationOnProfessor == 1:  # add
                                professorNewName = input("=> new name to be set: ")
                                print(
                                    "< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                                idToAdd = int(professors[len(professors) - 1].id) + 1

                                professors.append(Professor(str(idToAdd), professorNewName))
                                users.append(User(str(int(users[len(users)-1].id) + 1), professorNewName, "1234", '3'))
                                print("Professor created successfully!")

                            if operationOnProfessor == 2:  # update
                                idToUpdate = input("=> professorId to be updated: ")
                                professorNewName = input("=> new name to be set: ")
                                print(
                                    "< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                                for professor in professors:
                                    if professor.id == idToUpdate:
                                        for user in users:
                                            if user.userName == professor.name:
                                                user.userName = professorNewName
                                        professor.name = professorNewName
                                        break

                                print("Professor updated successfully!")

                            if operationOnProfessor == 3:  # delete
                                idToDelete = input("=> professorId to be deleted: ")
                                print(
                                    "< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                                for professor in professors:
                                    if professor.id == idToDelete:
                                        for user in users:
                                            if user.userName == professor.name:
                                                users.remove(user)
                                        professors.remove(professor)
                                        break
                                print("Professor deleted successfully!")

                            if operationOnProfessor == 4:  # show
                                for professor in professors:
                                    print(str(professor))
                            if operationOnProfessor == 5:
                                break

                    if changesOnDataSetChoice == 3:
                        while True:
                            operationsOnEachDataSetMenu("course")
                            operationOnCourse = int(input("=> choice: "))
                            print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                            if operationOnCourse == 1: #add
                                courseNewName = input("=> new name to be set: ")
                                courseNewProfessors = input("=> professors id to be set: (separated by ','): ")
                                print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                                idToAdd = int(courses[len(courses)-1].id) + 1
                                profs = []
                                for prof in professors:
                                    if prof.id in courseNewProfessors.split(','):
                                        profs.append(prof)
                                courses.append(Course(str(idToAdd), courseNewName, profs))
                                print("Course created successfully!")

                            if operationOnCourse == 2: #update
                                idToUpdate = input("=> courseId to be updated: ")
                                courseNewName = input("=> new name to be set: ")
                                courseNewProfessors = input("=> professors id to be set: (separated by ','): ")
                                print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                                for course in courses:
                                    if course.id == idToUpdate:
                                        course.name = courseNewName
                                        course.professors = []
                                        for prof in professors:
                                            if prof.id in courseNewProfessors.split(','):
                                                course.professors.append(prof)
                                        break
                                print("Course updated successfully!")


                            if operationOnCourse == 3: #delete
                                idToDelete = input("=> courseId to be deleted: ")
                                print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                                for course in courses:
                                    if course.id == idToDelete:
                                        courses.remove(course)
                                        break
                                print("Course deleted successfully!")

                            if operationOnCourse == 4: #show
                                for course in courses:
                                    print(str(course))
                            if operationOnCourse == 5:
                                break
                    if changesOnDataSetChoice == 4:
                        while True:
                            operationsOnEachDataSetMenu("academic year")
                            operationOnAcademicYear = int(input("=> choice: "))
                            print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                            if operationOnAcademicYear == 1:  # add
                                academicYearNewName = input("=> new name to be set: ")
                                academicYearCourses = input("=> courses id to be held: (separated by ','): ")
                                print(
                                    "< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                                idToAdd = int(academicYears[len(academicYears) - 1].id) + 1
                                crs = []
                                for course in courses:
                                    if course.id in academicYearCourses.split(','):
                                        crs.append(course)
                                academicYears.append(AcademicYear(str(idToAdd), academicYearNewName, crs))
                                print("Academic Year created successfully!")

                            if operationOnAcademicYear == 2:  # update
                                idToUpdate = input("=> academicYearId to be updated: ")
                                academicYearNewName = input("=> new name to be set: ")
                                academicYearCourses = input("=> courses id to be held: (separated by ','): ")
                                print(
                                    "< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                                for academicYear in academicYears:
                                    if academicYear.id == idToUpdate:
                                        academicYear.name = academicYearNewName
                                        academicYear.courseClasses = []
                                        for course in courses:
                                            if course.id in academicYearCourses.split(','):
                                                academicYear.courseClasses.append(course)
                                        break
                                print("Academic Year updated successfully!")

                            if operationOnAcademicYear == 3:  # delete
                                idToDelete = input("=> academicYearId to be deleted: ")
                                print(
                                    "< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                                for academicYear in academicYears:
                                    if academicYear.id == idToDelete:
                                        academicYears.remove(academicYear)
                                        break
                                print("Academic Year deleted successfully!")

                            if operationOnAcademicYear == 4:  # show
                                for academicYear in academicYears:
                                    print(str(academicYear))
                            if operationOnAcademicYear == 5:
                                break
                    if changesOnDataSetChoice == 5:
                        while True:
                            operationsOnEachDataSetMenu("group")
                            operationOnGroup = int(input("=> choice: "))
                            print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                            if operationOnGroup == 1:  # add
                                groupNewName = input("=> new name to be set: ")
                                groupCourses = input("=> courses id to be held: (separated by ','): ")
                                print(
                                    "< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                                idToAdd = int(groups[len(groups) - 1].id) + 1
                                crs = []
                                for course in courses:
                                    if course.id in groupCourses.split(','):
                                        crs.append(course)
                                groups.append(Group(str(idToAdd), groupNewName, crs))
                                print("Group created successfully!")

                            if operationOnGroup == 2:  # update
                                idToUpdate = input("=> groupId to be updated: ")
                                groupNewName = input("=> new name to be set: ")
                                groupCourses = input("=> courses id to be held: (separated by ','): ")
                                print(
                                    "< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                                for group in groups:
                                    if group.id == idToUpdate:
                                        group.name = groupNewName
                                        group.courseClasses = []
                                        for course in courses:
                                            if course.id in groupCourses.split(','):
                                                group.courseClasses.append(course)
                                        break
                                print("Group updated successfully!")

                            if operationOnGroup == 3:  # delete
                                idToDelete = input("=> groupId to be deleted: ")
                                print(
                                    "< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                                for group in groups:
                                    if group.id == idToDelete:
                                        groups.remove(group)
                                        break
                                print("Group deleted successfully!")

                            if operationOnGroup == 4:  # show
                                for group in groups:
                                    print(str(group))
                            if operationOnGroup == 5:
                                break

                    if changesOnDataSetChoice == 6:
                        while True:
                            operationsOnEachDataSetMenu("semi-group")
                            operationOnSemigroup = int(input("=> choice: "))
                            print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                            if operationOnSemigroup == 1:  # add
                                semigroupNewName = input("=> new name to be set: ")
                                semigroupNewAcademicYearId = input("=> academic year id that the new semigroup is part of: ")
                                semigroupNewGroupId = input("=> group id that the new semigroup is part of: ")
                                semigroupCourses = input("=> courses id to be held: (separated by ','): ")
                                print(
                                    "< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                                idToAdd = int(semigroups[len(semigroups) - 1].id) + 1
                                crs = []
                                for course in courses:
                                    if course.id in semigroupCourses.split(','):
                                        crs.append(course)
                                semigroups.append(SemiGroup(str(idToAdd), semigroupNewName,semigroupNewAcademicYearId,semigroupNewGroupId, crs))
                                print("Semigroup created successfully!")

                            if operationOnSemigroup == 2:  # update
                                idToUpdate = input("=> semigroupId to be updated: ")
                                semigroupNewName = input("=> new name to be set: ")
                                semigroupNewAcademicYearId = input(
                                    "=> academic year id that the new semigroup is part of: ")
                                semigroupNewGroupId = input("=> group id that the new semigroup is part of: ")
                                semigroupCourses = input("=> courses id to be held: (separated by ','): ")
                                print(
                                    "< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                                for semigroup in semigroups:
                                    if semigroup.id == idToUpdate:
                                        semigroup.name = semigroupNewName
                                        semigroup.academicYearId = semigroupNewAcademicYearId
                                        semigroup.groupId = semigroupNewGroupId
                                        semigroup.courseClasses = []
                                        for course in courses:
                                            if course.id in semigroupCourses.split(','):
                                                semigroup.courseClasses.append(course)
                                        break
                                print("Semigroup updated successfully!")

                            if operationOnSemigroup == 3:  # delete
                                idToDelete = input("=> semigroupId to be deleted: ")
                                print(
                                    "< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                                for semigroup in semigroups:
                                    if semigroup.id == idToDelete:
                                        semigroups.remove(semigroup)
                                        break
                                print("Semigroup deleted successfully!")

                            if operationOnSemigroup == 4:  # show
                                for semigroup in semigroups:
                                    print(str(semigroup))
                            if operationOnSemigroup == 5:
                                break
                    # go back
                    if changesOnDataSetChoice == 7:
                        break
            if timetableResponsibleChoice == 2:
                print(currentSol)

    # student:
    if currentUser.type == "3":
        while True:
            studentsMenu()
            studentsChoice = int(input("=> choice: "))
            print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
            if studentsChoice == 1:
                ok = 0
                while ok == 0:
                    ok = 1
                    print("Please provide the semigroup's name that you're interested in:")
                    semigroup = input("semigroup = ")
                    print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                    semigroupSections = []
                    for section in currentSol.sections:
                        if section.group.name == semigroup:
                            semigroupSections.append(section)
                    if len(semigroupSections) == 0:
                        ok = 0
                        print("Wrong input! Semi-group does not exist!")
                    else:
                        #sort by time and weekday
                        semigroupSections.sort(key=lambda x: (x.dayOfTheWeek.id, x.timeInterval.id))

                        for section in semigroupSections:
                            print(str(section))

    # professor:
    if currentUser.type == "4":
        while True:
            professorsMenu()
            professorsChoice = int(input("=> choice: "))
            print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
            if professorsChoice == 1:

                prof = currentUser.userName
                profSections = []
                for section in currentSol.sections:
                    if section.professor.name == prof:
                        profSections.append(section)

                profSections.sort(key=lambda x: (x.dayOfTheWeek.id, x.timeInterval.id))

                for section in profSections:
                    print(str(section))
            if professorsChoice == 2:
                print("Day of the week in which you prefer to work:")
                for day in workingDays:
                    print(day)
                # print("1. Monday")
                # print("2. Tuesday")
                # print("3. Wednesday")
                # print("4. Thursday")
                # print("5. Friday")
                dayOfTheWeek = input("=> day chosen: ")
                print("Time intervals you prefer in that day:")
                for tI in timeIntervals:
                    print(tI)
                # print("1. [8,10]")
                # print("2. [10,12]")
                # print("3. [12-14]")
                # print("4. [14-16]")
                # print("5. [16-18]")
                # print("6. [18-20]")
                currentTimeIntervals = input("=> time intervals chosen (separated by ','): ")

                print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                if currentTimeIntervals == '':
                    currentTimeIntervals = []
                else:
                    currentTimeIntervals = currentTimeIntervals.split(',')
                for prof in professors:
                    if prof.name == currentUser.userName:
                        if dayOfTheWeek in [d['dayOfTheWeek'] for d in prof.preferences]:
                            existingTimeIntervals = prof.preferences[next(
                                (index for (index, d) in enumerate(prof.preferences) if
                                 d["dayOfTheWeek"] == dayOfTheWeek), None)]['timeIntervals']
                            for ct in currentTimeIntervals:
                                if ct not in existingTimeIntervals:
                                    existingTimeIntervals += ct
                        else:
                            prof.addPreferences({'dayOfTheWeek': dayOfTheWeek, 'timeIntervals': currentTimeIntervals})
                        break
                for prof in professors:
                    print(prof.preferences)


if __name__ == "__main__":
    main()
