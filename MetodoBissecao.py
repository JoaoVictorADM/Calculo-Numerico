import math

def modulo(x):
    if x < 0:
        x = -x
    return x

def funcaoMatematica(x):
    return pow(x-1, 5)

def erro(valorObtido, valorEsperado):
    return modulo(valorObtido - valorEsperado)


def metodoBissecao(inicio, fim, tol):
    
    fInicio = funcaoMatematica(inicio)
    fMeio = 999999
    k = 1

    while(erro(fMeio, 0) > tol and k < 51):

        k = k + 1
        xMeio = (inicio+fim)/2
        fMeio = funcaoMatematica(xMeio)

        if(fMeio * fInicio < 0):
            fim = xMeio
            
        else:
            inicio = xMeio
            fInicio = fMeio
    return [xMeio, k]


def main():
    
    inicio = 0
    fim = 3

    if(funcaoMatematica(inicio) * funcaoMatematica(fim) > 0):
        print("Não há um zero de função nesse intervalo")
        return
    elif(funcaoMatematica(inicio) * funcaoMatematica(fim) == 0):
        print("0")
    else:
        print(metodoBissecao(inicio, fim, 0.0000001))    

if __name__ == "__main__":
    main() 

