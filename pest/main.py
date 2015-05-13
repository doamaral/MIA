__author__ = 'Lucas Amaral'
import random
from pest.envsim.individualmatrix import IndividualsMatrix

f = open('result.csv', 'w')
f.write('Saudaveis;Imunes;Pseudo-Imunes;Infectados;Mortos;Total\n')

#Criação do Ambiente
mat = IndividualsMatrix(5)

#Imprimir a Matriz
mat.parseMatrix(f)

goon = input("Este é o estado inicial, deseja iniciar? (s/n): ")

iteration = 0

while goon == "s":
    iteration = iteration + 1

    #Busca Infectantes e tenta infectar os vizinhos
    mat.infectNeighborhood()

    #Imprimir a Matriz
    mat.parseMatrix(f)

    #Ativa Virus em Infectados nesta iteração
    mat.activateVirus()

    print("Iteration = %d" % iteration)

    #Controle de Continuação do Jogo
    goon = input("Deseja prosseguir?: ")
print("Simulations terminated, Thanks")
f.close()