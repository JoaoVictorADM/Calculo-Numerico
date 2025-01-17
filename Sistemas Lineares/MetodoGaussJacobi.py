'''
                    João Victor Alves 
                    Cálculo Numérico
        Sistemas Lineares - Método de Gauss Jacobi
'''

# Função para calcular o erro relativo entre duas respostas sucessivas
def calcularErro(respostaAnt, novaResposta, tamLinha):
    numerador = 0
    denominador = 0

    # Calcula o erro usando a norma Euclidiana
    for i in range(tamLinha):
        numerador += (respostaAnt[i] - novaResposta[i]) ** 2
        denominador += novaResposta[i] ** 2
    
    erro = (numerador ** 0.5) / (denominador ** 0.5)
    return erro

# Implementação do método de Gauss-Jacobi para resolver sistemas lineares
def MetodoGaussJacobi(matriz, tamLinha, tol):
    resposta = []

    # Recebe o chute inicial para cada variável do sistema
    for i in range(tamLinha):
        resposta.append(int(input(f"Insira o chute inicial para x{i+1}: ")))

    erro = 9876543  # Valor inicial arbitrário para o erro
    k = 0  # Contador de iterações

    novaResposta = resposta[:]  # Cria uma cópia inicial das respostas

    # Loop principal para iterar até convergência ou limite de iterações
    while erro > tol and k < 50:
        k += 1

        # Calcula as novas respostas para cada variável
        for i in range(tamLinha):
            soma = matriz[i][tamLinha]  # Inicializa com o valor do termo independente
            for j in range(tamLinha):
                if j != i:
                    soma -= matriz[i][j] * resposta[j]  # Subtrai os termos já calculados
            novaResposta[i] = soma / matriz[i][i]  # Divide pelo coeficiente da variável atual
        
        # Calcula o erro relativo entre as respostas antigas e as novas
        erro = calcularErro(resposta, novaResposta, tamLinha)

        # Atualiza as respostas com as novas respostas calculadas
        resposta = novaResposta[:]

    # Retorna a resposta final e o número de iterações realizadas
    return [resposta, k]

# Função principal para executar o método de Gauss-Jacobi
def main():
    while True:
        tamLinha = int(input("Insira o número de linhas da matriz: "))

        if tamLinha >= 2:
            break

    matriz = []

    # Preenche a matriz do sistema linear com os valores fornecidos pelo usuário
    for i in range(tamLinha):
        linha = []
        for j in range(tamLinha + 1):
            novoElemento = int(input(f"Insira M[{i+1}][{j+1}]: "))
            linha.append(novoElemento)
        matriz.append(linha)

    # Chama o método de Gauss-Jacobi para resolver o sistema
    print(MetodoGaussJacobi(matriz, tamLinha, 0.00001))

# Verifica se este arquivo está sendo executado diretamente
if __name__ == "__main__":
    main()
