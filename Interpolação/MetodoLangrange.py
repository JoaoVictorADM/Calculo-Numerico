'''
                    João Victor Alves 
                    Cálculo Numérico
            Interpolação - Método de Lagrange
'''

def interpLagrange(xp, x, y, grau):
    yp = 0
    for k in range(0, grau + 1):
        p = 1
        for j in range(0, grau + 1):
            if k != j:
                p = p * (xp - x[j]) / (x[k] - x[j])
        yp = yp + p * y[k]
    return yp

# Pontos de exemplo
x = [2, 3, 4, 5]
y = [8, 27, 64, 125]

# Grau do polinômio interpolador
n = len(x) - 1

# Ponto a ser interpolado
xp = 8
yp = interpLagrange(xp, x, y, n)

# Resultado da interpolação
print(f'O valor interpolado para xp = {xp} é yp = {yp:.2f}')
