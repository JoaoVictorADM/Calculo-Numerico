import math

def funcaoMatematica(x):
    return pow(x - 1, 5)

def derivadaFuncao(x):
    return 5 * pow(x - 1, 4)

def erro(valorObtido, valorEsperado):
    return abs(valorObtido - valorEsperado)

def metodoNewtonR(inicio, tol):

    x = inicio
    fX = funcaoMatematica(x)
    k = 1

    while(erro(fX, 0) > tol and k < 51):

        x = x - (fX / derivadaFuncao(x))
        fX = funcaoMatematica(x)
        k = k + 1
    return [x, k]


def main():
    
    inicio = 3

    print(metodoNewtonR(inicio, 0.0001))


if __name__ == "__main__":
    main() 