__author__ = 'Lucas Amaral'
import random
from pest.envsim.individualmatrix import IndividualsMatrix

#Prepara arquivo de log a ser utilizado
f = open('result.csv', 'w')
f.write('Saudaveis;Imunes;Pseudo-Imunes;Infectados;Mortos;Total\n')

#Criação do Ambiente no seu estado inicial
mat = IndividualsMatrix(10)
iteration = 0

#Imprimir a Ambiente no seu estado inicial
print("-------------------")
print("### Iteration = %d ###" % iteration)
mat.parseMatrix(f)

goon = input("Este é o estado inicial, deseja iniciar? (s/n): ")


while goon == "s":
    iteration = iteration + 1
    print("-------------------")
    print("### Iteration = %d ###" % iteration)

    #Busca Infectantes e Move
    print("Moving...")
    mat.moveInfected()
    print("")

    #Busca Infectantes e Infecta Vizinhança. Lembrando que Indivíduos infectados nessa Iteração não tem capacidade de infectar
    print("Infecting...")
    mat.infectNeighborhood()
    print("")

    #Ativar Virus em Indivíduos infectados nesta iteração
    mat.activateVirus()

    #Subtrair idades
    mat.updateLifeCycle()

    #Realizar Acidentes
    mat.submitFatalAccident()

    #Realizar nascimentos
    mat.birthControl()

    #Imprimir a Matriz após Movimentação e Infecção
    print("New Configuration...")
    mat.parseMatrix(f)

    #Controle de Continuação do Jogo
    goon = input("Deseja prosseguir?: ")
print("Simulations terminated, Thanks")
f.close()