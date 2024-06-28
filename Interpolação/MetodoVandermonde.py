'''
                    João Victor Alves 
                    Cálculo Numérico
            Interpolação - Método de Vandermonde
'''

import numpy as np

def sistemaVander(x, y):
    n = len(x)
    A = np.empty((n, n))
    b = np.empty((n))

    # Construindo a matriz de Vandermonde A e o vetor b
    for i in range(n):
        A[i, 0] = 1
        for j in range(1, n):
            A[i, j] = A[i, j-1] * x[i]
        b[i] = y[i]

    return A, b

def interpolacao_vander(x, fx, x_interpolado):
    A, b = sistemaVander(x, fx)
    coeficientes = np.linalg.solve(A, b)

    # Calculando o valor interpolado para x_interpolado
    n = len(coeficientes)
    interpolado = 0
    for i in range(n):
        interpolado += coeficientes[i] * (x_interpolado ** i)

    return interpolado

# Exemplo de entrada com 3 pontos
x = [2, 3, 4, 5]
fx = [8, 27, 64, 125]

# Ponto a ser interpolado
x_interpolado = 8

# Realizando a interpolação
y_interpolado = interpolacao_vander(x, fx, x_interpolado)

print(f"Valor interpolado para x = {x_interpolado}: {y_interpolado}")
