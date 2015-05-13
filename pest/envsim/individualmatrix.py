import random
from pest.envsim.individual import Individual

__author__ = 'Lucas Amaral'

class IndividualsMatrix:
    dim = 0
    mtx = 0
    infected = 0
    healthy = 0
    imune = 0
    pimune = 0
    dead = 0

    def __init__(self, dim):
        self.dim = dim
        self.mtx = [[Individual() for count in range(self.dim)] for k in range(self.dim)]
        self.insertVirus()

    def parseMatrix(self, res):
        self.infected = 0
        self.healthy = 0
        self.imune = 0
        self.pimune = 0
        self.dead = 0
        for i in range(self.dim):
            for j in range(self.dim):
                self.mtx[i][j].decayLife()
                self.mtx[i][j].movestatus = False
                if self.mtx[i][j].health == 'S':
                    self.healthy = self.healthy + 1
                elif self.mtx[i][j].health == 'O':
                    self.infected = self.infected + 1
                elif self.mtx[i][j].health == '*':
                    self.imune = self.imune + 1
                elif self.mtx[i][j].health == '@':
                    self.pimune = self.pimune + 1
                elif self.mtx[i][j].health == 'X':
                    self.dead = self.dead + 1
                print("[(%s) L:%d P:%d I: %d]" % (self.mtx[i][j].health, self.mtx[i][j].life, self.mtx[i][j].power, self.mtx[i][j].infectionAbility), sep='', end='  ')
            print('', sep='', end='\n')
        print("-------------------")
        print("Total de Individuos Sadios: %d" % self.healthy)
        print("Total de Individuos Imunes: %d" % self.imune)
        print("Total de Individuos Pseudo: %d" % self.pimune)
        print("Total de Individuos Infect: %d" % self.infected)
        print("Total de Individuos Mortos: %d" % self.dead)
        print("Total de Individuos: %d" % (self.dim * self.dim))
        print("-------------------")
        res.write('%d;%d;%d;%d;%d;%d\n' % (self.healthy, self.imune, self.pimune, self.infected, self.dead, (self.dim * self.dim)))

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
        while not inf:
            i = random.randint(0, self.dim-1)
            j = random.randint(0, self.dim-1)
            if self.mtx[i][j].health == 'S':
                self.mtx[i][j].health = 'O'
                self.mtx[i][j].infectionAbility = 1
                self.mtx[i][j].setLife(4)
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
                if self.mtx[i][j].health == 'O' and self.mtx[i][j].infectionAbility:
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

    def activateVirus(self):
        for i in range(self.dim):
            for j in range(self.dim):
                if self.mtx[i][j].health == 'O' and not self.mtx[i][j].infectionAbility:
                    self.mtx[i][j].infectionAbility += 1

    def moveIndividual(self, i, j, newx, newy):
        aux = self.mtx[i][j]
        self.mtx[i][j] = self.mtx[newx][newy]
        self.mtx[newx][newy] = aux

    def moveInfected(self):
        """
        :return:
        """
        for i in range(self.dim):
            for j in range(self.dim):
                if self.mtx[i][j].health == "O" and not self.mtx[i][j].movestatus:
                    #0 = move na vertical / 1 = move na horizontal
                    moveopt = random.randint(0,1)
                    step = random.randint(-1,1)
                    print("Step: %d " % step, end=" ")
                    if moveopt == 0:
                        print("Vertical", end=" ")
                        if i + step >= 0 and i + step < self.dim:
                            newx = i + step
                        else:
                            newx = i
                        newy = j
                    else:
                        print("Horizontal", end=" ")
                        if j + step >= 0 and j + step < self.dim:
                            newy = j + step
                        else:
                            newy = j
                        newx = i
                    self.moveIndividual(i, j, newx, newy)
                    self.mtx[newx][newy].movestatus = True
                    print("[%d, %d] -> [%d, %d]" % (i, j, newx, newy))