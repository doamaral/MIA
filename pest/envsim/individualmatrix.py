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
    birth_rate = 0
    death_rate = 0
    it_infected = 0
    it_death_accident = 0
    environmental_immunity = random.randint(0, 9)

    def __init__(self, dim):
        self.dim = dim
        self.mtx = [[Individual(self.environmental_immunity) for count in range(self.dim)] for k in range(self.dim)]
        self.insertVirus()

    def parseMatrix(self, iteration, res):
        self.infected = 0
        self.healthy = 0
        self.imune = 0
        self.pimune = 0
        self.dead = 0
        for i in range(self.dim):
            for j in range(self.dim):
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
        print("Total de Individuos Pseudo-imunes: %d" % self.pimune)
        print("Total de Individuos Doentes: %d" % self.infected)
        print("Total de Infectantes Gerados: %d" % self.it_infected)
        print("Total de Individuos Mortos: %d" % self.dead)
        print("Total de Individuos Acidentados: %d" % self.it_death_accident)
        print("Total de Individuos Nasceram: %d" % self.birth_rate)
        print("Total de Individuos Morreram [acidentes + idade]: %d" % self.death_rate)
        print("Total de Individuos População: %d" % (self.dim * self.dim))
        print("-------------------")
        res.write('%d;%d;%d;%d;%d;%d;%d;%d;%d;%d;%d\n' % (iteration, self.healthy, self.imune, self.pimune, self.infected, self.it_infected, self.dead, self.it_death_accident, self.birth_rate, self.death_rate, (self.dim * self.dim)))

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
        self.it_infected = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if self.mtx[i][j].health == 'O' and self.mtx[i][j].infectionAbility:
                    if i-1 >= 0:
                        #Tenta infectar o de cima se existir
                        #print("Tenta infectar o de cima")
                        if self.mtx[i][j].infectIndividual(self.mtx[i-1][j]):
                            self.it_infected += 1
                    if i+1 < self.dim:
                        #Tenta infectar o de baixo se existir
                        #print("Tenta infectar o de baixo")
                        if self.mtx[i][j].infectIndividual(self.mtx[i+1][j]):
                            self.it_infected += 1
                    if j-1 >= 0:
                        #Tenta infectar o da esquerda se existir
                        #print("Tenta infectar o da esquerda")
                        if self.mtx[i][j].infectIndividual(self.mtx[i][j-1]):
                            self.it_infected += 1
                    if j+1 < self.dim:
                        #Tenta infectar o da direita se existir
                        #print("Tenta infectar o da direita")
                        if self.mtx[i][j].infectIndividual(self.mtx[i][j+1]):
                            self.it_infected += 1

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

    def updateLifeCycle(self):
        """
        Atualizar idade de cada elemento
        :return:
        """
        self.death_rate = 0
        for i in range(self.dim):
            for j in range(self.dim):
                self.mtx[i][j].decayLife()
                if self.mtx[i][j].health == 'X':
                    print("Morreu de Idade: posição [%d][%d]" % (i, j))
                    self.death_rate += 1

    def birthControl(self):
        """
        :return:
        """
        self.birth_rate = 0
        for i in range(self.dim):
            for j in range(self.dim):
                newborn_rate = random.randint(0, 9)
                if self.mtx[i][j].health == 'X' and newborn_rate >= 2:
                    #Parametro True indica que esse individuo pode nascer infectado
                    newborn = Individual(self.environmental_immunity, True)
                    self.mtx[i][j] = newborn
                    self.birth_rate += 1
                    print("Nasceu: posição [%d][%d] um [%s L:%d P:%d I:%d]" % (i, j, self.mtx[i][j].health, self.mtx[i][j].life, self.mtx[i][j].power, self.mtx[i][j].infectionAbility))

    def submitFatalAccident(self):
        """
        :return:
        """
        self.it_death_accident = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if random.randint(0,9) < 1:
                    self.mtx[i][j].killIndividual()
                    self.death_rate += 1
                    self.it_death_accident += 1
                    print("Morreu por acidente: posição [%d][%d]" % (i, j))