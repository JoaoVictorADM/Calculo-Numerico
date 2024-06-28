'''
                    João Victor Alves 
                    Cálculo Numérico
        Integração Numérica Método dos Trapézios
'''

# Define a função matemática que será integrada
def funcaoMatematica(x):
    return x**2
   
# Função para calcular a área usando o método dos trapézios
def calculaArea():
    
    # Recebe os limites de integração a e b do usuário
    a = int(input("Insira o primeiro limite: "))
    b = int(input("Insira o segundo limite: "))
    
    # Troca os valores de a e b se a for maior que b para garantir a <= b
    if(a > b):
        a, b = b, a
    
    # Recebe o número de trapézios (intervalos) desejados do usuário
    c = int(input("Insira o número de trapézios que deseja: "))
    
    # Calcula o tamanho de cada subintervalo (largura de cada trapézio)
    h = (b - a) / c
    
    # Inicializa a soma com os valores da função nos extremos a e b
    soma = funcaoMatematica(a) + funcaoMatematica(b)
    
    # Variável auxiliar para iteração
    contador = a
    
    # Itera sobre cada subintervalo, somando os valores intermediários
    for i in range (c - 1):
        contador += h
        soma += 2 * funcaoMatematica(contador)
        
    # Ajusta a soma final multiplicando pelo tamanho do intervalo h/2
    soma *= h / 2
    
    # Retorna a área aproximada calculada
    return soma
    

# Laço infinito para calcular a área repetidamente até o usuário interromper o programa
while(True):
    print(f"A área aproximada é: {calculaArea()}")
