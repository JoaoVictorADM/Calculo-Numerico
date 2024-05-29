def calcularErro(respostaAnt, novaResposta, tamLinha):
    
    numerador = 0
    denominador = 0

    for i in range(tamLinha):
        numerador += pow(respostaAnt[i] - novaResposta[i], 2)
        denominador += pow(novaResposta[i], 2)
    
    numerador = pow(numerador, 1/2)
    denominador = pow(denominador, 1/2)

    return numerador/denominador


def MetodoGaussJacobi(matriz, tamLinha, tol):

    resposta = []

    for i in range(tamLinha):
        resposta.append(int(input(f"Insira o chute inicial para x{i+1}: ")))

    erro = 9876543
    k = 0

    novaResposta = []

    for i in range(tamLinha):
        novaResposta.append(resposta[i])

    while(erro > tol and k < 50):

        k = k + 1

        for i in range(tamLinha):
            soma = matriz[i][tamLinha]
            for j in range(tamLinha):
                if(j != i):
                    soma -= (matriz[i][j] * resposta[j])
            soma /= matriz[i][i]
            novaResposta[i] = soma
        
        erro = calcularErro(resposta, novaResposta, tamLinha)

        for i in range(tamLinha):
            resposta[i] = novaResposta[i]

    return [resposta, k]

def main():
    
    while(True):

        tamLinha = int(input("Insira o número de linhas da matriz: "))

        if(tamLinha >= 2):
            break

    matriz = []

    for i in range(tamLinha):
        linha = []
        for j in range(tamLinha+1):
            novoElemento = int(input(f"Insira M[{i+1}][{j+1}]: "))
            linha.append(novoElemento)
        matriz.append(linha)

    print(MetodoGaussJacobi(matriz, tamLinha, 0.00001))
            
if __name__ == "__main__":
    main() 
