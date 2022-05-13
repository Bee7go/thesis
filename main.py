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

history = History(3)


def saveCurrentVariablesToPickle(N, C, M, K, G, currentSol):
    filename = 'currentVariables.pk'

    with open(filename, 'wb') as fi:
        # dump your data into the file
        pickle.dump([N, C, M, K, G, currentSol], fi)


def loadCurrentVariablesFromPickle():
    filename = 'currentVariables.pk'

    with open(filename, 'rb') as fi:
        return pickle.load(fi)


def BETAfindNewBestTimetable(academicYears, groups, semigroups, rooms, workingDays, timeIntervals, currentN, currentC, currentM, currentK, currentG):
    currentN = 10
    currentM = 1
    currentK = currentN
    currentG = 70

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

    start_time = time.time()

    nr_of_generations = currentG
    p1 = Population(currentN, academicYears, rooms, workingDays, timeIntervals)

    # while nr_of_generations and p1.bestFitness != 0:
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
        mc.mutationOnRoom(4)
        mc.mutationOnWorkingDay(3)
        mc.mutationOnTimeInterval(2)
        mc.mutationOnProfessor(5)
        p1.addChromosome(mc)
        mutatedChromosomes -= 1

    p1.getBestKChromosomes(currentK, [], semigroups)
    p1.preparePopulationForNextGeneration()

        # nr_of_generations -= 1

    p1.bestChromosome = p1.bestChromosome.transformToSemiGroups(semigroups)
    # print('best solution is:\n', p1.bestChromosome)
    print('best fitness is: ', p1.bestFitness)


    nr_of_generations = currentG
    p2 = Population(currentN, groups, rooms, workingDays, timeIntervals)
    while nr_of_generations and p2.bestFitness != 0:
        nrOfParents = currentC
        while nrOfParents:
            parent1 = p2.chromosomes[random.randint(0, currentN - 1)]
            parent2 = p2.chromosomes[random.randint(0, currentN - 1)]
            offsprings = p2.crossover(parent1, parent2, 2, 7)
            p2.addChromosome(offsprings[0])
            p2.addChromosome(offsprings[1])
            nrOfParents -= 1

        mutatedChromosomes = currentM
        while mutatedChromosomes:
            mc = p2.chromosomes[random.randint(0, currentN - 1)]
            mc.mutationOnRoom(4)
            mc.mutationOnWorkingDay(3)
            mc.mutationOnTimeInterval(2)
            mc.mutationOnProfessor(5)
            p2.addChromosome(mc)
            mutatedChromosomes -= 1

        p2.getBestKChromosomes(currentK, p1.bestChromosome.sections, semigroups)
        # p2.preparePopulationForNextGeneration()

        nr_of_generations -= 1
    # print('best solution is:\n', p2.bestChromosome)
    # p2.bestChromosome = p2.transformToSemiGroups(p2.bestChromosome, semigroups)
    # print('best solution is:\n', p2.bestChromosome)
    # print(p1.bestChromosome)
    print('best fitness is: ', p2.bestFitness)
    # TO DO: daca fitness-ul e naspa => reia procesul (inclusiv pt p1)



    # print('solution found in: ', time.time() - start_time)
    # print('best fitness is: ', p1.bestFitness)
    # print('best solution is:\n', p1.bestChromosome)


    # vR = ValidResult(currentN, currentC, currentM, currentK, currentG, p.bestFitness, time.time() - start_time)
    #
    # if history.updateResultIfBetter(vR):
    #     print("--> New solution is in top!\n")
    # else:
    #     print("--> New solution found is not in top!\n")
    # history.showTable()
    # return {"bestSolution": p2.bestChromosome, "bestFitness": p2.bestFitness, "solving time": time.time() - start_time}



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
            parent1 = p.chromosomes[random.randint(0, currentN - 1)]
            parent2 = p.chromosomes[random.randint(0, currentN - 1)]
            offsprings = p.crossover(parent1, parent2, 7, 17)
            p.addChromosome(offsprings[0])
            p.addChromosome(offsprings[1])
            nrOfParents -= 1

        mutatedChromosomes = currentM
        while mutatedChromosomes:
            mc = p.chromosomes[random.randint(0, currentN - 1)]
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
    print("2. Changes on dataset")
    print("3. See results")


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
    print("1. Generate a starting population of n individuals")
    print("2. Generate new individuals by using two-point crossover on two individuals")
    print("3. Apply all types of mutations on random  m individuals")
    print("4. Select the best k solutions according to the fitness")
    print("5. Show the most suitable result found for a population of g generations")
    print("6. Go back")


def changesOnDataSetMenu():
    return


def main():
    # setup
    currentVariables = loadCurrentVariablesFromPickle()
    currentN = currentVariables[0]
    currentC = currentVariables[1]
    currentM = currentVariables[2]
    currentK = currentVariables[3]
    currentG = currentVariables[4]
    currentSol = currentVariables[5]

    # professors
    file = open('Data/professors.csv')
    rows = csv.reader(file)
    professors = []
    for professor in rows:
        professors.append(Professor(professor[0], professor[1]))
        # print(str(professors[len(professors) - 1]))



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
        for course in group[2:]:
            for c in courses:
                if c.id == course:
                    groupCourses.append(c)

        groups.append(Group(group[0], group[1], group[2], groupCourses))
        # print(str(groups[len(groups) - 1]))

    # semi-groups
    file = open('Data/semigroups.csv')
    rows = csv.reader(file)
    semigroups = []
    for semigroup in rows:
        semigroupCourses = []
        for course in semigroup[3:]:
            for c in courses:
                if c.id == course:
                    semigroupCourses.append(c)

        semigroups.append(SemiGroup(semigroup[0], semigroup[1], semigroup[2], semigroup[3], semigroupCourses))
        # print(str(semigroups[len(semigroups) - 1]))

    # rooms
    file = open('Data/rooms.csv')
    rows = csv.reader(file)
    rooms = []
    for room in rows:
        rooms.append(Room(room[0], room[1], room[2], room[3]))
        # print(str(rooms[len(rooms) - 1]))

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
    BETAfindNewBestTimetable(academicYears, groups, semigroups, rooms, workingDays, timeIntervals, currentN, currentC,
                             currentM, currentK, currentG)
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
                        currentSol = findNewBestTimetable(groups, rooms, workingDays, timeIntervals, currentN, currentC,
                                                          currentM, currentK, currentG)["bestSolution"]
                        saveCurrentVariablesToPickle(currentN, currentC, currentM, currentK, currentG,
                                                     currentSol)

                    if changesOnAlgorithmUserChoice == 2:
                        C = int(input("C = "))  # check if smaller than N
                        print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                        currentC = C
                        currentSol = findNewBestTimetable(groups, rooms, workingDays, timeIntervals, currentN, currentC,
                                                          currentM, currentK, currentG)["bestSolution"]
                        saveCurrentVariablesToPickle(currentN, currentC, currentM, currentK, currentG,
                                                     currentSol)

                    if changesOnAlgorithmUserChoice == 3:
                        M = int(input("M = "))
                        print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                        currentM = M
                        currentSol = findNewBestTimetable(groups, rooms, workingDays, timeIntervals, currentN, currentC,
                                                          currentM, currentK, currentG)["bestSolution"]
                        saveCurrentVariablesToPickle(currentN, currentC, currentM, currentK, currentG,
                                                     currentSol)

                    if changesOnAlgorithmUserChoice == 4:
                        K = int(input("K = "))
                        print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                        currentK = K
                        currentSol = findNewBestTimetable(groups, rooms, workingDays, timeIntervals, currentN, currentC,
                                                          currentM, currentK, currentG)["bestSolution"]
                        saveCurrentVariablesToPickle(currentN, currentC, currentM, currentK, currentG,
                                                     currentSol)

                    if changesOnAlgorithmUserChoice == 5:
                        G = int(input("G = "))
                        print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                        currentG = G
                        currentSol = findNewBestTimetable(groups, rooms, workingDays, timeIntervals, currentN, currentC,
                                                          currentM, currentK, currentG)["bestSolution"]
                        saveCurrentVariablesToPickle(currentN, currentC, currentM, currentK, currentG,
                                                     currentSol)

                    if changesOnAlgorithmUserChoice == 6:
                        break

            if adminUserChoice == 3:
                print(currentSol)

    # timetable responsible:
    if currentUser.type == "2":
        while True:
            timetableResponsibleMenu()
            timetableResponsibleChoice = int(input("=> choice: "))
            print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
            if timetableResponsibleChoice == 1:
                while True:
                    print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                    print("Select an option listed below: ")
                    changesOnDataSetMenu()
                    changesOnDataSetChoice = int(input("=> choice: "))
                    print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
                    if changesOnDataSetChoice == 1:
                        return
            if timetableResponsibleChoice == 2:
                print(currentSol)

    # student:
    if currentUser.type == "3":
        while True:
            studentsMenu()
            studentsChoice = int(input("=> choice: "))
            print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
            if studentsChoice == 1:
                print(currentSol)

    # professor:
    if currentUser.type == "4":
        while True:
            professorsMenu()
            professorsChoice = int(input("=> choice: "))
            print("< - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - >")
            if professorsChoice == 1:
                print(currentSol)


if __name__ == "__main__":
    main()
