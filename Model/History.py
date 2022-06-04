import csv

from prettytable import PrettyTable

from Model.ValidResult import ValidResult


class History:
    def __init__(self, topRange):
        self.topRange = topRange
        self.top = []
        self.getCurrentHistory()

    def updateResultIfBetter(self, newRes):
        if len(self.top) < self.topRange:
            self.refreshTop(newRes)
            return True
        lastPosElem = self.top[-1]
        if newRes.bestFitness < lastPosElem.bestFitness or (
                newRes.bestFitness == lastPosElem.bestFitness and newRes.timeSpend < lastPosElem.timeSpend):
            self.top.remove(lastPosElem)
            self.refreshTop(newRes)
            return True
        return False

    def refreshTop(self, betterRes):
        self.top.append(betterRes)
        self.top.sort(key=lambda x: (x.bestFitness, x.timeSpend))
        self.updateHistoryFile()

    def updateHistoryFile(self):
        file = open(r'Data\history.csv', "w")
        for rec in self.top:
            file.write(
                str(rec.N) + ',' + str(rec.crossover) + ',' + str(rec.M) + ',' + str(rec.K) + ',' + str(
                    rec.G) + ',' + str(
                    rec.bestFitness) + ',' + str(rec.timeSpend))
            file.write('\n')

        return

    def getCurrentHistory(self):
        file = open(r'Data\history.csv', "r")
        rows = csv.reader(file)
        for top in rows:
            self.top.append(
                ValidResult(int(top[0]), top[1], int(top[2]), int(top[3]), int(top[4]), int(top[5]), float(top[6])))

    def GetTopResults(self):
        return self.top

    def showTable(self):
        table = PrettyTable(['N',
                             'C',
                             'M',
                             'K',
                             'G',
                             'Best fitness',
                             'Solving time'])
        for rec in self.top:
            table.add_row([rec.N, rec.crossover, rec.M, rec.K, rec.G, rec.bestFitness, rec.timeSpend])
        print("Top results:")
        print(table)
        print("Legend:")
        print("N: number of individuals in the starting population")
        print("C: number of individuals to suffer mutations")
        print("M: number of individuals to suffer mutations")
        print(
            "K: number of best solutions extracted from the current population used to be part of the next generation")
        print("G: number of generations")
