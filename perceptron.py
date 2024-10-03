# perceptron.py
# Calculo com uma unica camada de perceptron

# Title: Implementação de um perceptron para operadores lógicos AND, OR e XOR
import numpy as np # Importa a biblioteca numpy

# Operador lógico AND
entradas = np.array([[0, 0],[0,1],[1,0],[1,1]])  # Valores de entrada 
saidas = np.array([0, 0, 0, 1])  # Valores de saída

# Operador lógico OR
#entradas = np.array([[0, 0],[0,1],[1,0],[1,1]])  # Valores de entrada
#saidas = np.array([0, 1, 1, 1])  # Valores de saída

# Operador lógico XOR
#entradas = np.array([[0, 0],[0,1],[1,0],[1,1]])  # Valores de entrada
#saidas = np.array([0, 1, 1, 0])  # Valores de saída

pesos = np.array([0.0, 0.0])  # Pesos aleatórios
taxaAprendizagem = 0.1  # Taxa de aprendizagem

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

# Função de treinamento dos pesos
def treinar():
    erroTotal = 1
    while erroTotal != 0:
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.array(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print('Peso atualizado: ' + str(pesos[j]))
        print('Total erros: ' + str(erroTotal))
        
treinar()
print('Rede neural treinada')
print(calculaSaida(entradas[0]))
print(calculaSaida(entradas[1]))
print(calculaSaida(entradas[2]))    
print(calculaSaida(entradas[3]))

# Fim do código