__author__ = 'Lucas Amaral'
import random

from envsim.individualmatrix import IndividualsMatrix

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