__author__ = 'Lucas Amaral'
import random

class Individual:
    health = "S"
    infected = 0
    movestatus = False

    def __init__(self):
        opt = random.randint(0,4)
        if opt <=2:
            self.health = 'S'
        elif opt == 3:
            self.health = '*'
        elif opt == 4:
            self.health = '@'
