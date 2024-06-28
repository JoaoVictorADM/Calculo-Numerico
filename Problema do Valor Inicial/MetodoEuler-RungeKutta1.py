'''
                    João Victor Alves 
                    Cálculo Numérico
    Problema do Valor Inicial - Método de Euler / Runge Kutta 1 Ordem
'''

import math

# Define a função que será usada na equação diferencial
def funcao(t, y):
    return y + math.sin(t) + 5 * math.cos(t)

# Implementa o método de Euler para resolver o problema do valor inicial
def euler(tIncial, yT, inicioIntervalo, fimIntervalo, numeroIteracoes):

    # Inicializa as variáveis t e y com os valores iniciais fornecidos
    y = yT
    t = tIncial

    # Garante que inicioIntervalo seja menor ou igual a fimIntervalo
    if inicioIntervalo > fimIntervalo:
        inicioIntervalo, fimIntervalo = fimIntervalo, inicioIntervalo

    # Calcula o tamanho do passo (h) para cada iteração
    passo = (fimIntervalo - inicioIntervalo) / numeroIteracoes

    # Ajusta o sinal do passo se o ponto inicial for igual ao ponto final
    if t == fimIntervalo:
        passo = -passo

    # Loop para realizar as iterações do método de Euler
    for _ in range(numeroIteracoes):
        # Calcula o próximo valor de y usando o método de Euler
        y = y + abs(passo) * (funcao(t, y))

        # Incrementa o valor de t pelo passo
        t += passo

        # Imprime o valor atualizado de y
        print(f'yi+1 = {y}')

    # Retorna o valor final de y após todas as iterações
    return y

# Executa a função euler com os parâmetros fornecidos e imprime o resultado final

# euler(tIncial: Valor inicial de t,  yT: Valor inicial de y, inicioIntervalo: Início do intervalo de integração, fimIntervalo: Fim do intervalo de integração,  
# numeroIteracoes: Número de iterações (ou passos) a serem realizados)

print(euler(0, 0, 0, 1, 4))
print("Euler / Runge Kutta 1 Ordem")
