__author__ = 'Lucas Amaral'

def print_matrix(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

def set_matrix(matriz, tamanho):
    matriz = [["@" for j in range(tamanho)] for i in range(tamanho)]