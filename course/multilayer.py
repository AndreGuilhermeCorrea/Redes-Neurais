# multilayer.py
# Implementação de uma rede neural com múltiplas camadas
import numpy as np

# Operador lógico XOR

# Entradas
entradas = np.array([[0,0],[0,1],[1,0],[1,1]])

# Saídas
saidas = np.array([[0],[1],[1],[0]])

# Sinapse entre a camada de entrada e a camada oculta
#pesos0 = np.array([[-0.424, -0.740, -0.961], [-0.358, -0.577, -0.469]])
# Sinapse entre a camada oculta e a camada de saída
#peso1 = np.array([[-0.017], [-0.893], [0.148]])

# Pesos da camada de entrada
pesos0 = 2*np.random.random((2,3)) - 1

# Pesos da camada oculta
peso1 = 2*np.random.random((3,1)) - 1

# Função de ativação
def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

# Derivada da função de ativação
def sigmoidDerivada(sig):
    return sig * (1 - sig)

# Teste da função de ativação
a = sigmoid(0.5)
b = sigmoidDerivada(a)

# Número de épocas
epocas = 1000

# Momento
momento = 1

# Taxa de aprendizagem
taxaAprendizagem = 0.6

# Treinamento da rede neural
for j in range(epocas):

    # Camada de entrada
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada, pesos0)
    #print("somaSinapse0")
    #print(somaSinapse0)
    
    camadaOculta = sigmoid(somaSinapse0)
    #print("camadaOculta")
    #print(camadaOculta)
    
    somaSinapse1 = np.dot(camadaOculta, peso1)
    #print("somaSinapse1")
    #print(somaSinapse1)
    
    camadaSaida = sigmoid(somaSinapse1)
    #print("camadaSaida")
    #print(camadaSaida)
    
    erroCamadaSaida = saidas - camadaSaida
    #print("erroCamadaSaida")
    #print(erroCamadaSaida)
    
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))
    #print("mediaAbsoluta")
    #print(mediaAbsoluta)
    print("Erro: " + str(mediaAbsoluta))
    
    derivadaSaida = sigmoidDerivada(camadaSaida)
    #print("derivadaSaida")
    #print(derivadaSaida)
    
    deltaSaida = erroCamadaSaida * derivadaSaida
    #print("deltaSaida")
    #print(deltaSaida)
    
    #Matriz transposta
    pesoCamadaOcultaTransposta = peso1.T
    deltaSaidaXPeso = deltaSaida.dot(pesoCamadaOcultaTransposta)
    #print("deltaSaidaXPeso")
    #print(deltaSaidaXPeso)
    
    deltaCamadaOculta = deltaSaidaXPeso * sigmoidDerivada(camadaOculta)
    #print("deltaCamadaOculta")
    #print(deltaCamadaOculta)
    
    camadaOcultaTransposta = camadaOculta.T
    pesosCamadaOcultaNovo = camadaOcultaTransposta.dot(deltaSaida)
    #print("pesosCamadaOculta")
    #print(pesosCamadaOcultaNovo)
    
    peso1 = (momento * peso1) + (pesosCamadaOcultaNovo * taxaAprendizagem)
    #print("Peso 1")
    #print(peso1)
    
    camadaEntradaTransposta = camadaEntrada.T    
    #print("camadaEntradaTransposta")
    #print(camadaEntradaTransposta)

    pesosNovo0 = camadaEntradaTransposta.dot(deltaCamadaOculta)
    #print("pesosNovo0")
    #print(pesosNovo0)
    
    pesos0 = (momento * pesos0) + (pesosNovo0 * taxaAprendizagem)
    #print("pesos0")
    #print(pesos0)
    
    

'''
inicializa os pesos
calcula a saída <-------|
calcula os erros        |
calcula os pesos        |
atualiza os pesos       |
                        |
erro é pequeno?         |
sim: fim                |
nao: calcula a saída -->|
'''

#Gradiente: Encontrar a combinação de pesos que o erro é o menor possível
#Força bruta: testar todas as combinações de pesos
#Simmulated annealing: técnica de otimização
#Algoritmo genético: técnica de otimização
#minimo local: encontrar o mínimo local
#minimo global: encontrar o mínimo global
#Backpropagation: técnica de otimização

#Função de ativação: função que determina a saída da rede neural
#Deriada da função: derivada de uma variável(resultado da função sigmoide * (1 - resultado da função sigmoide))
#Delta da saída: erro da saída * derivada da função de ativação
#Delta da camada oculta: delta da saída * pesos da camada oculta * derivada da função de ativação
#gradiente: ajuste dos pesos

#Pesos: pesos da rede neural
#Taxa de aprendizagem: ajuste dos pesos
#Momento(Momentum): ajuste dos pesos
#Função de ativação: função que determina a saída da rede neural
#Derivada da função de ativação: derivada da função de ativação
#Taxa de aprendizagem(Learning rate): ajuste dos pesos

# Fim do código