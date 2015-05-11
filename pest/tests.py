__author__ = 'Usuário'
import random

from env.individualmatrix import IndividualsMatrix

mat = IndividualsMatrix(10)
mat.parseMatrix()
print("--------------------")
mat.insertVirus()
mat.parseMatrix()
print("--------------------")
mat.insertVirus()
mat.parseMatrix()
print("--------------------")
print(mat.getNumberOfInfected())