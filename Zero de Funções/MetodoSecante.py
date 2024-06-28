'''
João Victor Alves 
Cálculo Numérico
Zero de Função - Método da Secante
'''

import math

# Definição da função matemática cujo zero queremos encontrar
def funcaoMatematica(x):
    return pow(x - 1, 5)

# Função para calcular o erro entre o valor obtido e o valor esperado
def erro(valorObtido, valorEsperado):
    return abs(valorObtido - valorEsperado)

# Implementação do método da secante para encontrar o zero da função
def metodoSecante(xn, xn1, tol):

    fXn = funcaoMatematica(xn)     # Valor da função no ponto xn
    fXn1 = funcaoMatematica(xn1)   # Valor da função no ponto xn1
    k = 1                          # Contador de iterações

    # Verifica se algum dos pontos iniciais já é raiz
    if fXn == 0:
        return [xn, k]
    
    if fXn1 == 0:
        return [xn1, k]

    # Loop principal do método da secante
    while erro(fXn1, 0) > tol and k < 51:
        k += 1  # Incrementa o contador de iterações
        
        auxXn1 = xn1  # Armazena o valor anterior de xn1
        
        # Atualiza xn1 usando a fórmula do método da secante
        xn1 = xn1 - (fXn1 * (xn1 - xn)) / (fXn1 - fXn)
        
        xn = auxXn1  # Atualiza xn para o próximo cálculo
        fXn = fXn1    # Atualiza fXn para o próximo cálculo de xn1
        fXn1 = funcaoMatematica(xn1)  # Calcula o novo valor de fXn1

    return [xn1, k]  # Retorna o valor aproximado do zero e o número de iterações realizadas

# Função principal para executar o método da secante
def main():
    xn = 0   # Primeiro ponto inicial
    xn1 = 3  # Segundo ponto inicial

    print(metodoSecante(xn, xn1, 0.0001))  # Chama o método da secante com a tolerância desejada

if __name__ == "__main__":
    main()
