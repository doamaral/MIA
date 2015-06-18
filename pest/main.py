__author__ = 'Lucas Amaral'
from random import randint
import time
from envsim.individualmatrix import IndividualsMatrix

dimensao = int(input("Qual a dimensão da Matriz? (Sugestão: 5 a 10): "))

ciclos = int(input("Quantos ciclos deve ter a simulação? (Sugestão: > 10): "))

inicio = time.time()
#Prepara arquivo de log a ser utilizado
f = open('result.csv', 'w')
f.write('Iteraçao;Saudios;Imunes;Pseudo-Imunes;Doentes;Infectantes Gerados;Mortos;Acidentados;Nasceram;Morreram;Total\n')

#Criação do Ambiente no seu estado inicial
mat = IndividualsMatrix(dimensao)
iteration = 0

#Imprimir a Ambiente no seu estado inicial
print("-------------------")
print("### Iteration = %d ###" % iteration)
mat.parseMatrix(iteration, f)

goon = input("Este é o estado inicial, deseja iniciar? (s/n): ")

#iteration < 1000

while iteration < ciclos:
    iteration = iteration + 1
    print("-------------------")
    print("### Iteration = %d ###" % iteration)

    #Realizar nascimentos
    print("Giving birth...")
    mat.birthControl()
    print("")

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

fim = time.time()
print('Tempo de Execução: %s' % (fim - inicio))
print("Simulations terminated, Thanks")
out = input("Press any key to  leave.")
f.close()