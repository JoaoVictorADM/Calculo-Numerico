'''
                João Victor Alves 
                Cálculo Numérico
        Zero de Função - Método de Newton Raphson
'''

# Definição da função matemática cujo zero queremos encontrar
def funcaoMatematica(x):
    return pow(x - 1, 5)

# Definição da derivada da função para usar no método de Newton-Raphson
def derivadaFuncao(x):
    return 5 * pow(x - 1, 4)

# Função para calcular o erro entre o valor obtido e o valor esperado
def erro(valorObtido, valorEsperado):
    return abs(valorObtido - valorEsperado)

# Implementação do método de Newton-Raphson para encontrar o zero da função
def metodoNewtonR(inicio, tol):

    x = inicio  # Valor inicial para a iteração
    fX = funcaoMatematica(x)  # Valor da função no ponto inicial
    k = 1  # Contador de iterações

    while erro(fX, 0) > tol and k < 51:  # Condições de parada: erro menor que a tolerância ou máximo de iterações
        x = x - (fX / derivadaFuncao(x))  # Fórmula do método de Newton-Raphson
        fX = funcaoMatematica(x)  # Atualiza o valor da função no novo ponto
        k = k + 1  # Incrementa o contador de iterações

    return [x, k]  # Retorna o valor aproximado do zero e o número de iterações realizadas

# Função principal para executar o método de Newton-Raphson
def main():
    inicio = 3  # Valor inicial para a busca do zero da função

    print(metodoNewtonR(inicio, 0.0001))  # Chama o método de Newton-Raphson com a tolerância desejada

if __name__ == "__main__":
    main()
