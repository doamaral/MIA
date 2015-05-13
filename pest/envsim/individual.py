__author__ = 'Lucas Amaral'
import random

class Individual:
    health = " "
    power = 100
    movestatus = False
    infectionAbility = 0
    life = 0

    def __init__(self):
        opt = random.randint(0, 4)
        if opt <= 2:
            self.health = 'S'
            self.life = 10
            self.power = 0
        elif opt == 3:
            self.health = '*'
            self.life = 10
            self.power = 100
        elif opt == 4:
            self.health = '@'
            self.life = 10
            self.power = random.randint(0, 100)

    def killIndividual(self):
        self.setLife(0)
        self.health = 'X'

    def setLife(self, newage):
        self.life = newage

    def infectIndividual(self, target):
        infectionPower = random.randint(1, 100)
        if self.infectionAbility:
            if self.power < infectionPower:
                target.health = 'O'
                target.infectionAbility = 0
                if target.age > 4:
                    target.setLife(4)

    def decayLife(self):
        if self.life > 0:
            self.setLife(self.life - 1)
        if self.life == 0:
            self.killIndividual()
