from sklearn.neural_network import MLPClassifier
from sklearn import datasets

# Importa a base de dados iris
iris = datasets.load_iris()

entradas = iris.data
saidas = iris.target

# Cria a rede neural
redeNeural = MLPClassifier(verbose=True, max_iter=1000, tol=0.00001, activation='logistic', learning_rate_init=0.01, )

# Treina a rede neural
print(redeNeural.fit(entradas, saidas))

# Faz a previsão com as respectivas entradas
print(redeNeural.predict([[5, 7.2, 5.1, 2.2]]))