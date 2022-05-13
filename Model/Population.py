import copy

from Model.Chromosome import Chromosome
from Model.Section import Section


class Population:

    def __init__(self, length, groups, rooms, workingDays, timeIntervals):
        self.length = length
        self.groups = groups
        self.rooms = rooms
        self.workingDays = workingDays
        self.timeIntervals = timeIntervals
        self.chromosomes = []
        self.fitnessScores = []
        self.generatePopulation()
        self.bestFitness = 300000
        # self.bestChromosome = []

    def generatePopulation(self):
        for _ in range(self.length):
            c = Chromosome(self.groups, self.rooms, self.workingDays, self.timeIntervals)
            self.chromosomes.append(c)

    def calculateFitnessScores(self, previousSections, allSemiGroups):
        print("===> goes in here!!!")
        self.fitnessScores = []
        for chromosome in self.chromosomes:
            chromosomeTransformed = copy.deepcopy(chromosome)
            if previousSections:
                calculatedFitness = chromosome.calculateFitness([])
                chromosomeTransformed = copy.deepcopy(self.transformToSemiGroups(chromosome, allSemiGroups))
                calculatedFitness += chromosomeTransformed.calculateFitness(previousSections)
            else:
                calculatedFitness = copy.deepcopy(chromosomeTransformed.calculateFitness([]))
            self.fitnessScores.append(calculatedFitness)
        print(self.fitnessScores)

    def getBestKChromosomes(self, k, previousSections, allSemiGroups):
        self.calculateFitnessScores(previousSections, allSemiGroups)
        bestPositions = sorted(range(len(self.fitnessScores)), key=lambda i: self.fitnessScores[i])[:k]
        # print(bestPositions)
        self.bestFitness = self.fitnessScores[bestPositions[0]]
        self.bestChromosome = self.chromosomes[bestPositions[0]]
        bestChromosomes = []
        # print('bestPositions')
        # print(bestPositions)
        # print('best fitnesses ===>')
        for pos in bestPositions:
            bestChromosomes.append(self.chromosomes[pos])
            # print(str(self.chromosomes[pos].sections[0] + ' + ' + self.chromosomes[pos].calculateFitness([]))

        self.chromosomes = bestChromosomes
        # self.length = len(self.chromosomes)

    def preparePopulationForNextGeneration(self):
        while len(self.chromosomes) < self.length:
            self.addChromosome(Chromosome(self.groups, self.rooms, self.workingDays, self.timeIntervals))

    # singlePoint: crossover(c1, c2, x, len(c1.sections))
    # twoPoint: crossover(c1, c2, x, y)
    def crossover(self, c1, c2, x, y):
        for i in range(x, y):
            c1.sections[i], c2.sections[i] = c2.sections[i], c1.sections[i]
        return c1, c2

    def addChromosome(self, c):
        self.chromosomes.append(c)

    def GetChromosomes(self):
        return self.chromosomes

    def transformToSemiGroups(self, chromosome, allSemiGroups):
        newBestChromosome = copy.deepcopy(chromosome)
        newBestChromosome.sections = []
        for section in chromosome.sections:
            for semigroup in section.group.transformToSemiGroups(allSemiGroups):
                newBestChromosome.sections.append(
                    Section(section.course, semigroup, section.professor, section.room, section.dayOfTheWeek,
                            section.timeInterval))
        return newBestChromosome

    def __str__(self):
        result = ''
        for c in self.chromosomes:
            result += str(c) + '--------------------\n'
        return result
