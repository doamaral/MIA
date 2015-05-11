__author__ = 'Lucas Amaral'
import random
def print_matrix(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
def init_matrix(matriz):
    #Povoar amostra
    #Inserindo o primeiro infectado
    linha = random.randint(0, len(matriz)-1)
    coluna = random.randint(0, len(matriz[1])-1)
    matriz[linha][coluna] = "O"

    #Inserindo Sadios, Imunes e Pseudo-imunes
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == " ":
                opt = random.randint(0,4)
                if opt <=2:
                    matriz[i][j] = " "
                elif opt == 3:
                    matriz[i][j] = "*"
                elif opt == 4:
                    matriz[i][j] = "@"
def infect(matriz, i, j):
    if matriz[i][j] == " ":
        matriz[i][j] = "O"
    elif matriz[i][j] == "@":
        if random.randint(0,2) == 0:
            matriz[i][j] = "O"
def infecting_neighbors(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == "O":
                if i-1 >= 0:
                    #Tenta infectar o de cima se existir
                    infect(matriz,i-1,j)
                if i+1 < len(matriz):
                    #Tenta infectar o de baixo se existir
                    infect(matriz,i-1,j)
                if j-1 >= 0:
                    #Tenta infectar o da esquerda se existir
                    infect(matriz,i,j-1)
                if j+1 < len(matriz[i]):
                    #Tenta infectar o da direita se existir
                    infect(matriz,i,j+1)
def num_infected(matriz):
    count = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == "O":
                count = count + 1
    return count
def move(matriz, i, j, newx, newy):
    aux = matriz[i][j]
    matriz[i][j] = matriz[newx][newy]
    matriz[newx][newy] = aux
    print("--------------------")
def walk(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == "O":
                print("Está em Matriz[%d][%d]" % (i, j))
                #0 = move na vertical / 1 = move na horizontal
                moveopt = random.randint(0,1)
                step = random.randint(-1,1)
                print("Passo = %d" % step)
                if moveopt == 0:
                    print("Move na Vertical")
                    if i + step >= 0 and i + step < len(matriz):
                        newx = i + step
                    else:
                        newx = i
                    newy = j
                    print("Move para Matriz[%d][%d]" % (newx, newy))
                else:
                    print("Move na Horizontal")
                    if j + step >= 0 and j + step < len(matriz[i]):
                        newy = j + step
                    else:
                        newy = j
                    newx = i
                    print("Move para Matriz[%d][%d]" % (newx, newy))
                move(matriz, i, j, newx, newy)