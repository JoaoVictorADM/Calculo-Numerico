'''
                João Victor Alves 
                Cálculo Numérico
        Zero de Função - Método da Bisseção
'''

import math

# Função auxiliar para calcular o módulo de um número
def modulo(x):
    if x < 0:
        x = -x
    return x

# Definição da função matemática cujo zero queremos encontrar
def funcaoMatematica(x):
    return pow(x - 1, 5)

# Função para calcular o erro entre o valor obtido e o valor esperado
def erro(valorObtido, valorEsperado):
    return modulo(valorObtido - valorEsperado)

# Implementação do método da bisseção para encontrar o zero da função
def metodoBissecao(inicio, fim, tol):
    fInicio = funcaoMatematica(inicio)
    fMeio = 999999  # Valor inicial alto para garantir a entrada no loop
    k = 1  # Contador de iterações

    while erro(fMeio, 0) > tol and k < 51:  # Condições de parada: erro menor que a tolerância ou máximo de iterações
        k += 1
        xMeio = (inicio + fim) / 2
        fMeio = funcaoMatematica(xMeio)

        if fMeio * fInicio < 0:  # Se o produto for negativo, o zero está no intervalo [inicio, xMeio]
            fim = xMeio
        else:  # Caso contrário, o zero está no intervalo [xMeio, fim]
            inicio = xMeio
            fInicio = fMeio

    return [xMeio, k]  # Retorna o valor aproximado do zero e o número de iterações realizadas

# Função principal para execução do método da bisseção
def main():
    inicio = 0
    fim = 3

    # Verifica se há um zero de função no intervalo [inicio, fim]
    if funcaoMatematica(inicio) * funcaoMatematica(fim) > 0:
        print("Não há um zero de função nesse intervalo")
        return
    elif funcaoMatematica(inicio) * funcaoMatematica(fim) == 0:
        print("0")
    else:
        print(metodoBissecao(inicio, fim, 0.0000001))  # Chama o método da bisseção com a tolerância desejada

if __name__ == "__main__":
    main()
