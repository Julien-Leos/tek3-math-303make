import sys
import numpy as np
import copy

class Core:
    command = []
    recipe = []
    files = []
    matrix = []
    buildCommands = []

    def __init__(self, recipe, command):
        self.command = command
        self.recipe = recipe
        self.getFiles()
        self.files.sort()
        self.buildMatrix()

    def getFiles(self):
        for i in self.recipe:
            file = i.split(" ")
            file[0] = file[0][:-1]
            for j in file:
                if j not in self.files:
                    self.files.append(j)

    def buildMatrix(self):
        for i in range(len(self.files)):
            line = []
            for j in range(len(self.files)):
                line.append(0)
            self.matrix.append(line)

        for l in range(len(self.files)):
            for i in self.recipe:
                file = i.split(" ")
                file[0] = file[0][:-1]
                if (file[0] == self.files[l]):
                    for j in file[1:]:
                        self.matrix[self.files.index(j)][l] = 1

    def displayMatrix(self):
        for i in self.matrix:
            print("[", end = "")
            for j in range(len(self.matrix)):
                print(i[j], end = "")
                if j != len(self.matrix) - 1:
                    print(" ", end = "")
            print("]")

    def readMatrix(self):
        for i in range (len(self.matrix)):
            self.readLine(i, [])
    
    def readLine(self, index, links):
        links = links + [(self.files[index])]
        try:
            self.matrix[index].index(1)
        except:
            self.displayLinks(links)
            return
        for i in range(len(self.matrix)):
            if self.matrix[index][i] == 1:
                self.readLine(i, links)

    def displayLinks(self, links):
        if len(links) == 1:
            return
        for i in range(len(links)):
            print(links[i], end = "")
            if i != len(links) - 1:
                print(" -> ", end = "")
        print("")

    def completeBuild(self, toBuild):
        try:
            index = self.files.index(toBuild)
        except:
            sys.exit(84)

        for (matrix_index, i) in enumerate(self.matrix[index]):
            if i == 1:
                recipe_index = [i.split(':')[0] for i in self.recipe].index(self.files[matrix_index])
                self.buildCommands.append(self.command[recipe_index])
                self.completeBuild(self.files[matrix_index])

    def displayBuild(self):
        self.buildCommands.reverse()
        self.buildCommands = list(dict.fromkeys(self.buildCommands))
        self.buildCommands.reverse()
        for i in self.buildCommands:
            print(i)
        if len(self.buildCommands) == 0:
            print("")
