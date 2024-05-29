import math

def funcaoMatematica(x):
    return pow(x - 1, 5)

def erro(valorObtido, valorEsperado):
    return abs(valorObtido - valorEsperado)

def metodoSecante(xn, xn1, tol):

    fXn = funcaoMatematica(xn)
    fXn1 = funcaoMatematica(xn1)
    k = 1

    if(fXn == 0):
        return [xn, k]
    
    if(fXn1 == 0):
        return [xn1, k]

    
    while(erro(fXn1, 0) > tol and k < 51):

        k = k + 1
        auxXn1 = xn1

        xn1 = xn1 - (fXn1 * (xn1 - xn)) / (fXn1 - fXn)

        xn = auxXn1
        fXn = fXn1
        fXn1 = funcaoMatematica(xn1)
 
    return [xn1, k]


def main():
    
    xn  = 0
    xn1 = 3

    print(metodoSecante(xn, xn1, 0.0001))


if __name__ == "__main__":
    main() 