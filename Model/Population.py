import copy

from Model.Chromosome import Chromosome


class Population:

    def __init__(self, length, groups, rooms, workingDays, timeIntervals):
        self.length = length
        self.groups = groups
        self.rooms = rooms
        self.workingDays = workingDays
        self.timeIntervals = timeIntervals
        self.chromosomes = []
        self.fitnessScores = []
        self.bestFitness = 300000

    def generatePopulationForCourses(self):
        for _ in range(self.length):
            c = Chromosome(self.groups, self.rooms, self.workingDays, self.timeIntervals)
            c.generateChromosome()
            self.chromosomes.append(c)

    def generatePopulationForSeminars(self, previousSections):
        for _ in range(self.length):
            c = Chromosome(self.groups, self.rooms, self.workingDays, self.timeIntervals)
            c.generateChromosomeForSeminars(previousSections)
            self.chromosomes.append(c)

    def calculateFitnessScores(self, previousSections, allSemiGroups):
        self.fitnessScores = []
        for chromosome in self.chromosomes:
            chromosomeTransformed = copy.deepcopy(chromosome)
            if previousSections:
                calculatedFitness = chromosome.calculateFitness([])
                chromosomeTransformed = chromosome.transformToSemiGroups(allSemiGroups)
                calculatedFitness += chromosomeTransformed.calculateFitness(previousSections)
            else:
                calculatedFitness = copy.deepcopy(chromosomeTransformed.calculateFitness([]))
            self.fitnessScores.append(calculatedFitness)

    def getBestKChromosomes(self, k, previousSections, allSemiGroups):
        self.calculateFitnessScores(previousSections, allSemiGroups)
        bestPositions = sorted(range(len(self.fitnessScores)), key=lambda i: self.fitnessScores[i])[:k]
        self.bestFitness = self.fitnessScores[bestPositions[0]]
        self.bestChromosome = self.chromosomes[bestPositions[0]]
        bestChromosomes = []
        for pos in bestPositions:
            bestChromosomes.append(self.chromosomes[pos])

        self.chromosomes = bestChromosomes

    def preparePopulationForNextGenerationCourses(self):
        while len(self.chromosomes) < self.length:
            c = Chromosome(self.groups, self.rooms, self.workingDays, self.timeIntervals)
            c.generateChromosome()
            self.addChromosome(c)

    def preparePopulationForNextGenerationSeminars(self, previousSections):
        while len(self.chromosomes) < self.length:
            c = Chromosome(self.groups, self.rooms, self.workingDays, self.timeIntervals)
            c.generateChromosomeForSeminars(previousSections)
            self.addChromosome(c)

    def crossover(self, c1, c2, x, y):
        for i in range(x, y):
            c1.sections[i], c2.sections[i] = c2.sections[i], c1.sections[i]
        return c1, c2

    def addChromosome(self, c):
        self.chromosomes.append(c)

    def GetChromosomes(self):
        return self.chromosomes

    def __str__(self):
        result = ''
        for c in self.chromosomes:
            result += str(c) + '--------------------\n'
        return result
