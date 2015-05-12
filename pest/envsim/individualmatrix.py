import random
from envsim.individual import Individual

__author__ = 'Lucas Amaral'

class IndividualsMatrix:
    dim = 0
    mtx = 0
    infected = 0
    healthy = 0
    imune = 0
    pimune = 0

    def __init__(self, dim):
        self.dim = dim
        self.mtx = [[Individual() for count in range(self.dim)] for k in range(self.dim)]
        self.insertVirus()

    def phantomParseMatrix(self):
        self.infected = 0
        self.healthy = 0
        self.imune = 0
        self.pimune = 0

        for i in range(self.dim):
            for j in range(self.dim):
                if self.mtx[i][j].health == 'S':
                    self.healthy += 1
                elif self.mtx[i][j].health == 'O':
                    self.infected += 1
                elif self.mtx[i][j].health == '*':
                    self.imune += 1
                elif self.mtx[i][j].health == '@':
                    self.pimune += 1

    def parseMatrix(self, res):
        self.infected = 0
        self.healthy = 0
        self.imune = 0
        self.pimune = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if self.mtx[i][j].health == 'S':
                    self.healthy = self.healthy + 1
                elif self.mtx[i][j].health == 'O':
                    self.infected = self.infected + 1
                elif self.mtx[i][j].health == '*':
                    self.imune = self.imune + 1
                elif self.mtx[i][j].health == '@':
                    self.pimune = self.pimune + 1
                print(self.mtx[i][j].health, sep='', end='  ')
            print('',sep='',end='\n')
        print("-------------------")
        print("Total de Individuos: %d" % (self.dim * self.dim))
        print("Total de Individuos Sadios: %d" % self.healthy)
        print("Total de Individuos Imunes: %d" % self.imune)
        print("Total de Individuos Pseudo: %d" % self.pimune)
        print("Total de Individuos Infect: %d" % self.infected)
        print("-------------------")
        res.write('%d;%d;%d;%d;%d\n' % (self.healthy, self.imune, self.pimune, self.infected, (self.dim * self.dim)))

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

    def insertVirus(self):
        """
        Infecta algum Individuo saudavel
        :return:
        """
        inf = False
        while inf == False:
            i = random.randint(0, self.dim-1)
            j = random.randint(0, self.dim-1)
            if self.mtx[i][j].health == 'S':
                self.mtx[i][j].health = 'O'
                self.updateNumberOfInfected()
                inf = True

    def infectNeighborhood(self):
        """
        :param i: Linha do Indivíduo infectado
        :param j: Coluna do Indivíduo infectado
        :return: VOID
        """
        for i in range(self.dim):
            for j in range(self.dim):
                if self.mtx[i][j].health == 'O':
                    if i-1 >= 0:
                        #Tenta infectar o de cima se existir
                        #print("Tenta infectar o de cima")
                        self.mtx[i][j].infectIndividual(self.mtx[i-1][j])
                    if i+1 < self.dim:
                        #Tenta infectar o de baixo se existir
                        #print("Tenta infectar o de baixo")
                        self.mtx[i][j].infectIndividual(self.mtx[i+1][j])
                    if j-1 >= 0:
                        #Tenta infectar o da esquerda se existir
                        #print("Tenta infectar o da esquerda")
                        self.mtx[i][j].infectIndividual(self.mtx[i][j-1])
                    if j+1 < self.dim:
                        #Tenta infectar o da direita se existir
                        #print("Tenta infectar o da direita")
                        self.mtx[i][j].infectIndividual(self.mtx[i][j+1])

    def moveInfected(self):
        """
        :return:
        """
        #TODO

