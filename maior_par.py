__author__ = 'Usuário'

vetor = [[1, 2, 3], [4, 5, 6], [7, 38, 9], [41, 11, 12]]

maior = 0

for i in range(len(vetor)):
    for j in range(len(vetor[0])):
        if vetor[i][j] % 2 == 0 and vetor[i][j] > maior:
            maior = vetor[i][j]
print(maior)