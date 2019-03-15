from random import randrange
from random import random

class Rabin_Miller:
    def __init__(self, p, q):
        self.number = p
        self.repeats = q

    def check(self):
        expresion = None
        multiplier = self.number-1
        indicator = 0
        while multiplier % 2 == 0:
            indicator += 1
            multiplier /= 2
        for rep in range(self.repeats):
            base = randrange(2, self.number-2)
            expresion = int(base)**int(multiplier) % self.number
            if expresion == 1 or expresion == self.number-1:
                continue
            iterator = 1
            while iterator < indicator and expresion != self.number-1:
                expresion = expresion**2 % self.number
                if expresion == 1:
                    return False
                iterator += 1
        if expresion != self.number-1:
            return False

        return True

    def change_number(self, p):
        self.number = p