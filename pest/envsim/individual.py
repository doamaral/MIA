__author__ = 'Lucas Amaral'
import random

class Individual:
    health = "S"
    infected = 0
    movestatus = False
    age = 0

    def __init__(self):
        opt = random.randint(0,4)
        if opt <=2:
            self.health = 'S'
            self.age = 10
        elif opt == 3:
            self.health = '*'
            self.age = 10
        elif opt == 4:
            self.health = '@'
            self.age = 10

    def killIndividual(self):
        self.setAge(0)
        self.health = 'D'

    def setAge(self, newage):
        self.age = newage

    def infectIndividual(self, target):
        if self.health == 'O':
            if target.health == 'S':
                target.health = 'O'
                if target.age > 4:
                    target.setAge(4)
            elif target.health == '@':
                if random.randint(0, 2) == 0:
                    target.health = 'O'
                    if target.age > 4:
                        target.setAge(4)

    def decayAge(self):
        if self.age > 0:
            self.setAge(self.age - 1)
        if self.age == 0:
            self.killIndividual()
