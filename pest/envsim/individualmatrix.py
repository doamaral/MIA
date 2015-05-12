import random
from envsim.individual import Individual

__author__ = 'Lucas Amaral'

class IndividualsMatrix:
    dim = 0
    mtx = 0
    infected = 0

    def __init__(self, dim):
        self.dim = dim
        self.mtx = [[Individual() for count in range(self.dim)] for k in range(self.dim)]
        #self.updateNumberOfInfected()

    def parseMatrix(self):
        for i in range(self.dim):
            for j in range(self.dim):
                print(self.mtx[i][j].health, sep='', end='  ')
            print('',sep='',end='\n')

    def moveIndividual(self, i, j, newx, newy):
        self.mtx[i][j].movestatus = True
        aux = self.mtx[i][j]
        self.mtx[i][j] = self.mtx[newx][newy]
        self.mtx[newx][newy] = aux

    def updateNumberOfInfected(self):
        self.infected = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if self.mtx[i][j].health == 'O':
                    self.infected = self.infected + 1

    def getNumberOfInfected(self):
        return self.infected

    def infectIndividual(self, i, j):
        if self.mtx[i][j].health == 'S':
            self.mtx[i][j].health = 'O'
        elif self.mtx[i][j].health == '@':
            if random.randint(0,2) == 0:
                self.mtx[i][j].health = "O"

    def insertVirus(self):
        inf = False
        while inf == False:
            i = random.randint(0, self.dim-1)
            j = random.randint(0, self.dim-1)
            if self.mtx[i][j].health == 'S':
                self.infectIndividual(i,j)
                self.updateNumberOfInfected()
                inf = True

    def infectNeighborhood(self, i, j):
        print("TODO")

    def moveInfected(self):
        print("TODO")

