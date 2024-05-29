import math

def funcaoMatematica(x):
    return pow(x, 3) - x - 1

def calcularNovoX(x):
    return pow(x + 1, 1/3)

def erro(valorObtido, valorEsperado):
    return abs(valorObtido - valorEsperado)

def metodoPontoFixo(x, tol):
    
    fX = funcaoMatematica(x)
    k = 1

    while(erro(fX, 0) > tol and k < 51):

        k = k + 1
        x = calcularNovoX(x)
        fX = funcaoMatematica(x)
 
    return [x, k]

def main():
    
    inicio = 3

    print(metodoPontoFixo(inicio, 0.0001))


if __name__ == "__main__":
    main() 