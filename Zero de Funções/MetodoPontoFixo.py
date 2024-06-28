'''
                João Victor Alves 
                Cálculo Numérico
        Zero de Função - Método do Ponto Fixo
'''

# Definição da função matemática cujo zero queremos encontrar
def funcaoMatematica(x):
    return pow(x, 3) - x - 1

# Definição da função que calcula o próximo valor de x no método do ponto fixo
def calcularNovoX(x):
    return pow(x + 1, 1/3)

# Função para calcular o erro entre o valor obtido e o valor esperado
def erro(valorObtido, valorEsperado):
    return abs(valorObtido - valorEsperado)

# Implementação do método do ponto fixo para encontrar o zero da função
def metodoPontoFixo(x, tol):
    
    fX = funcaoMatematica(x)  # Calcula o valor da função no ponto inicial x
    k = 1  # Inicializa o contador de iterações

    while erro(fX, 0) > tol and k < 51:  # Condições de parada: erro menor que a tolerância ou máximo de iterações
        k = k + 1
        x = calcularNovoX(x)  # Calcula o próximo valor de x usando a função calcularNovoX
        fX = funcaoMatematica(x)  # Atualiza o valor da função no novo ponto x

    return [x, k]  # Retorna o valor aproximado do zero e o número de iterações realizadas

# Função principal para executar o método do ponto fixo
def main():
    inicio = 3  # Valor inicial para a busca do zero da função

    print(metodoPontoFixo(inicio, 0.0001))  # Chama o método do ponto fixo com a tolerância desejada

if __name__ == "__main__":
    main()
