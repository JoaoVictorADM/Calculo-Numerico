'''
                    João Victor Alves 
                    Cálculo Numérico
            Interpolação - Método de Newton
'''

def interpNewton(x, y, xi):
    n = len(x)
    fdd = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        fdd[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            fdd[i][j] = (fdd[i + 1][j - 1] - fdd[i][j - 1]) / (x[i + j] - x[i])

    xterm = 1
    yint = fdd[0][0]

    for order in range(1, n):
        xterm *= (xi - x[order - 1])
        yint += fdd[0][order] * xterm

    return yint

# Exemplo de entrada com 3 pontos
x = [2, 3, 4, 5]
y = [8, 27, 64, 125]

# Ponto a ser interpolado
xi = 9

# Calculando o valor interpolado
yi = interpNewton(x, y, xi)

print(f"Valor interpolado para x = {xi}: {yi}")
