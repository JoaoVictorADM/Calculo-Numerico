'''
                    João Victor Alves 
                    Cálculo Numérico
    Problema do Valor Inicial - Método Runge Kutta 3 Ordem
'''

# Importa a biblioteca math para usar funções matemáticas como sin e cos
import math

# Define a função que será usada na equação diferencial
def funcao(t, y):
    return y + math.sin(t) + 5 * math.cos(t)

# Implementa o método de Runge Kutta de 3ª ordem para resolver o problema do valor inicial
def rungeKutta3(tIncial, yT, inicioIntervalo, fimIntervalo, numeroIteracoes):

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

    # Loop para realizar as iterações do método de Runge Kutta de 3ª ordem
    for _ in range(numeroIteracoes):

        # Calcula os coeficientes k1, k2 e k3 para o método de Runge Kutta de 3ª ordem
        k1 = funcao(t, y)
        k2 = funcao(t + abs(passo) / 2, y + (abs(passo) / 2) * k1)
        k3 = funcao(t + abs(passo), y - abs(passo) * k1 + 2 * abs(passo) * k2)

        # Imprime os valores de t, y, k1, k2 e k3 para cada iteração
        print(f'y = {y}  t = {t} k1 = {k1} k2 = {k2} k3 = {k3} ')

        # Atualiza o valor de t somando o passo
        t += passo
        # Atualiza o valor de y usando a média ponderada dos coeficientes k1, k2 e k3
        y = y + (abs(passo) / 6) * (k1 + 4 * k2 + k3)

        # Imprime o valor atualizado de y após cada iteração
        print(f'yi+1 = {y}')

        print()
        
    # Retorna o valor final de y após todas as iterações
    return y

# Executa a função rungeKutta3 com os parâmetros fornecidos e imprime o resultado final

# rungeKutta3(tIncial: Valor inicial de t,  yT: Valor inicial de y, inicioIntervalo: Início do intervalo de integração, fimIntervalo: Fim do intervalo de integração,  
# numeroIteracoes: Número de iterações (ou passos) a serem realizados)

print(rungeKutta3(0, 0, 0, 1, 4))
print("Runge Kutta 3 Ordem")