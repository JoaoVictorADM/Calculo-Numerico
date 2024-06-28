'''
                    João Victor Alves 
                    Cálculo Numérico
        Integração Numérica - Método de Simpson
'''

def funcaoMatematica(x):
    return x**2

# A função calculaArea utiliza o método de integração numérica de Simpson
def calculaArea():
    
    # Recebe os limites de integração a e b do usuário
    a = int(input("Insira o primeiro limite: "))
    b = int(input("Insira o segundo limite: "))
    
    # Se a for maior que b, troca os valores para garantir a <= b
    if(a > b):
        a, b = b, a
    
    # Recebe o número de intervalos desejados do usuário
    c = int(input("Insira um número par de intervalos que deseja: "))

    # Verifica se o número de intervalos é par, caso contrário, incrementa em 1
    if(c % 2 != 0):
        c += 1
    
    # Calcula o tamanho de cada subintervalo
    h = (b - a) / c
    
    # Inicializa a soma com os valores da função nos extremos a e b
    soma = funcaoMatematica(a) + funcaoMatematica(b)
    
    # Variável auxiliar para iteração
    contador = a
    
    # Itera c-1 vezes para calcular os valores intermediários
    for i in range (c - 1):
        
        contador += h
        
        # Se o índice for par, multiplica por 4 e adiciona à soma
        if(i % 2 == 0):
            soma += 4 * funcaoMatematica(contador)
        # Se o índice for ímpar, multiplica por 2 e adiciona à soma
        else:
            soma += 2 * funcaoMatematica(contador)

    # Ajusta a soma final multiplicando pelo tamanho do intervalo h/3
    soma *= h / 3   
    return soma
    

# Laço infinito para calcular a área repetidamente
while(True):
    print(f"A área aproximada é: {calculaArea()}")
