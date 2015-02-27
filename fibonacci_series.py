__author__ = 'Lucas'
import time
def fibonacci_iterativo(n):
    n1 = 1
    n2 = 1
    termo = 1
    if n > 2:
        for x in range(3, n + 1, 1):
            termo = n1 + n2
            n1 = n2
            n2 = termo
    return termo


def fibonacci_recursivo(n):
    n1 = 1
    n2 = 1
    termo = 1
    if n > 2:
        termo = fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
    return termo

# print("Fibonacci de 4")
#print(fibonacci_iterativo(4))
num = 30

print("Abordagem Iterativa")
for i in range(1, num, 1):
    ini = time.time()
    rec = fibonacci_iterativo(i)
    fim = time.time()
    print('%d;%s' % (i, fim - ini))

print("Abordagem Recursiva")
for i in range(1, num, 1):
    ini = time.time()
    rec = fibonacci_recursivo(i)
    fim = time.time()
    print('%d;%s' % (i, fim - ini))

