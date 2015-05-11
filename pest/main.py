__author__ = 'Lucas Amaral'

import libwork
import random

tamanho = random.randint(10, 10)
mat = [[" " for j in range(tamanho)] for i in range(tamanho)]
print(tamanho)
libwork.init_matrix(mat)
iteration = 0
print("initial state Iteration = %d" % iteration)
libwork.print_matrix(mat)
print("Quantidade de Infectados = %d" % libwork.num_infected(mat))
print("--------------------------")
goon = input("Este é o estado inicial, deseja iniciar? (s/n): ")

while goon == "s":
    iteration = iteration + 1
    print("Iteration = %d" % iteration)
    #libwork.infecting_neighbors(mat)

    libwork.walk(mat)

    libwork.print_matrix(mat)
    print("Quantidade de Infectados = %d" % libwork.num_infected(mat))
    print("--------------------------")
    goon = input("Deseja prosseguir?: ")
print("Simulations terminated, Thanks")