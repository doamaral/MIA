__author__ = 'Lucas Amaral'
import random
import time
from pest.envsim.individualmatrix import IndividualsMatrix

inicio = time.time()
#Prepara arquivo de log a ser utilizado
f = open('result.csv', 'w')
f.write('Iteraçao;Saudaveis;Imunes;Pseudo-Imunes;Infectados;Mortos;Total\n')

#Criação do Ambiente no seu estado inicial
mat = IndividualsMatrix(100)
iteration = 0

#Imprimir a Ambiente no seu estado inicial
print("-------------------")
print("### Iteration = %d ###" % iteration)
mat.parseMatrix(iteration, f)

goon = input("Este é o estado inicial, deseja iniciar? (s/n): ")

#iteration < 1000

while goon == "s":
    iteration = iteration + 1
    print("-------------------")
    print("### Iteration = %d ###" % iteration)

    #Realizar nascimentos
    mat.birthControl()

    #Busca Infectantes e Infecta Vizinhança. Indivíduos infectados nessa Iteração não tem capacidade de infectar
    print("Infecting...")
    mat.infectNeighborhood()
    print("")

    #Busca Infectantes e Move
    print("Moving...")
    mat.moveInfected()
    print("")

    #Ativar Virus em Indivíduos infectados nesta iteração
    mat.activateVirus()

    #Subtrair idades
    mat.updateLifeCycle()

    #Realizar Acidentes
    mat.submitFatalAccident()

    #Imprimir a Matriz após Movimentação e Infecção
    print("New Configuration...")
    mat.parseMatrix(iteration, f)

    #Controle de Continuação do Jogo
    goon = input("Deseja prosseguir?: ")
fim = time.time()
print('Tempo de Execução: %s' % (fim - inicio))
print("Simulations terminated, Thanks")
f.close()