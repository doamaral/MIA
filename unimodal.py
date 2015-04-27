__author__ = 'Usuário'

def unimodal(v, i, f):
    if i == f-1:
        return f
    meio = int((i+f)/2)
    if v[meio] > v[meio+1]:
        return unimodal(v, i, meio)
    return unimodal(v, meio, f)

vetor = [1, 2, 3, 4, 5, 4, 1]

print(vetor[unimodal(vetor, 0, len(vetor)-1)])