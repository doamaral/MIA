__author__ = 'Lucas Amaral'
import random
from envsim.individualmatrix import IndividualsMatrix

f = open('result.csv', 'w')
f.write('Saudaveis;Imunes;Pseudo-Imunes;Infectados;Total\n')

#Criação do Ambiente
mat = IndividualsMatrix(10)
#Imprimir a Matriz
mat.parseMatrix(f)

goon = input("Este é o estado inicial, deseja iniciar? (s/n): ")

iteration = 0

while goon == "s":
    iteration = iteration + 1
    #Imprimir a Matriz
    mat.parseMatrix(f)
    mat.infectNeighborhood()
    print("Iteration = %d" % iteration)
    goon = input("Deseja prosseguir?: ")
print("Simulations terminated, Thanks")
f.close()