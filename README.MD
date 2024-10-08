# Redes Neurais

As redes neurais são modelos computacionais inspirados no funcionamento do sistema nervoso biológico. Elas são compostas por neurônios artificiais organizados em camadas, conectados por sinapses (as conexões entre os neurônios). Esses neurônios realizam cálculos matemáticos para identificar padrões e fazer previsões com base em dados de entrada. Cada neurônio recebe um conjunto de entradas, realiza um cálculo e gera uma saída, que serve como entrada para outros neurônios. A rede é treinada para aprender padrões e executar tarefas específicas de maneira eficiente.

Com o avanço das tecnologias de computação em nuvem, redes neurais podem ser implementadas de forma escalável e altamente eficiente. Neste projeto, além de servir como base para o estudo das redes neurais, será abordado o uso da AWS para hospedar e gerenciar uma aplicação de reconhecimento de imagens.

## Objetivos do Projeto

O principal objetivo deste projeto é explorar o treinamento e a implementação de redes neurais com suporte da infraestrutura AWS. Além disso, será desenvolvido um frontend simples utilizando HTML e JavaScript para facilitar a inserção de imagens a serem reconhecidas pela inteligência artificial. Esse frontend será integrado à aplicação FastAPI, que será responsável por processar as imagens e realizar o reconhecimento via IA.

### Arquitetura da Solução

* **Treinamento de Redes Neurais**
    - O treinamento das redes neurais será realizado localmente, com os dados resultantes sendo armazenados em um bucket S3 da AWS.
* **Serviço de Reconhecimento de Imagem**
    - O modelo treinado será implantado em um endpoint utilizando o Amazon SageMaker.
    - As imagens para reconhecimento serão enviadas ao endpoint via API, que retornará as previsões.
* **Armazenamento de Dados**
    - Inicialmente, os dados serão armazenados localmente em um banco de dados PostgreSQL.
    - Futuramente, planeja-se migrar os dados para o DynamoDB, aproveitando a escalabilidade e a alta disponibilidade da AWS.
* **Infraestrutura como Código**
    - A infraestrutura será provisionada utilizando o AWS CDK (Cloud Development Kit) e o CloudFormation, garantindo a automação e reprodutibilidade da infraestrutura necessária.
* **Testes de API com Postman**
    Para garantir o funcionamento correto das rotas de API, será utilizado o Postman para realizar testes, como:
    - Envio de imagens para o endpoint de reconhecimento.
    - Verificação das respostas do modelo de rede neural.
    - Testes de integração com o banco de dados para garantir o correto armazenamento dos resultados.

### Passos Futuros

* **Migração para DynamoDB**
    - Planejar e executar a migração dos dados do PostgreSQL para o DynamoDB, ajustando a aplicação para utilizar DynamoDB como banco de dados principal.
* **Automatização da Infraestrutura**
    - Utilizar o AWS CDK para automatizar a criação e configuração de todos os recursos AWS necessários, além de gerenciar e versionar a infraestrutura com CloudFormation.
* **Monitoramento e Escalabilidade**
    - Implementar monitoramento da aplicação utilizando o Amazon CloudWatch para acompanhar seu desempenho.
    - Configurar políticas de auto-scaling para garantir que a aplicação se adapte automaticamente ao aumento de carga.

    ## Tecnologias Utilizadas no Projeto

    * **Python:** Linguagem de programação principal para desenvolvimento da aplicação. [Documentação](https://docs.python.org/3/)
    * **FastAPI:** Framework para construção de APIs rápidas e eficientes. [Documentação](https://fastapi.tiangolo.com/)
    * **PostgreSQL:** Banco de dados relacional utilizado inicialmente para armazenamento de dados. [Documentação](https://www.postgresql.org/docs/)
    * **AWS S3:** Serviço de armazenamento de objetos utilizado para armazenar os dados de treinamento. [Documentação](https://docs.aws.amazon.com/s3/index.html)
    * **Amazon SageMaker:** Serviço utilizado para implantar o modelo treinado em um endpoint. [Documentação](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
    * **HTML e JavaScript:** Tecnologias utilizadas para desenvolver o frontend da aplicação. [HTML Documentação](https://developer.mozilla.org/docs/Web/HTML) | [JavaScript Documentação](https://developer.mozilla.org/docs/Web/JavaScript)
    * **Postman:** Ferramenta utilizada para testar as rotas da API. [Documentação](https://learning.postman.com/docs/getting-started/introduction/)
    * **AWS DynamoDB:** Banco de dados NoSQL planejado para substituir o PostgreSQL, aproveitando a escalabilidade e alta disponibilidade. [Documentação](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
    * **AWS CDK (Cloud Development Kit):** Ferramenta para provisionamento de infraestrutura como código. [Documentação](https://docs.aws.amazon.com/cdk/latest/guide/home.html)
    * **AWS CloudFormation:** Serviço para gerenciar e versionar a infraestrutura. [Documentação](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
    * **Amazon CloudWatch:** Serviço para monitoramento e acompanhamento do desempenho da aplicação. [Documentação](https://docs.aws.amazon.com/cloudwatch/)

## Um Estudo Sobre as Redes Neurais

As redes neurais têm aplicações em diversas áreas, pois são capazes de aprender padrões a partir de grandes volumes de dados.

* **Visão Computacional:** 
    - Utilizando Redes Neurais Convolucionais (CNNs), as redes neurais são usadas para reconhecimento de imagens, classificação de objetos, detecção de rostos e diagnóstico médico com base em imagens radiológicas. 
        - **Como:** Classificação de imagens de gatos e cães, detecção de tumores em imagens de ressonância magnética.

* **Processamento de Linguagem Natural (NLP):** 
    - Redes como as Redes Neurais Recorrentes (RNNs) e Transformers são usadas para tradução automática, geração de texto, chatbots, análise de sentimentos e muito mais.
        - **Como:** Google Translate, assistentes virtuais como Alexa e Siri, análise de sentimentos de comentários em redes sociais.

* **Sistemas de Recomendação:** 
    - Redes neurais são usadas para prever preferências dos usuários, recomendando filmes, músicas, produtos, ou notícias com base no comportamento anterior do usuário. 
        - **Como:**  Sistemas de recomendação da Netflix, Amazon e YouTube.

* **Medicina:** 
    - Redes neurais são aplicadas em diagnóstico médico, descoberta de medicamentos e análise preditiva de doenças. 
        - **Como:** Diagnóstico de câncer, identificação de doenças raras, previsão de evolução de doenças com base em histórico médico.

* **Jogos e Inteligência Artificial:** 
    - Redes neurais são usadas para criar agentes que jogam jogos complexos, como o Go e o xadrez, vencendo até mesmo jogadores humanos profissionais.
        - **Como:** AlphaGo, da DeepMind, e agentes de IA que jogam StarCraft.

## Fluxo das Redes Neurais

O fluxo de uma rede neural é composto por diversas etapas. 

* **Inicialização dos Pesos**: os pesos da rede neural são inicializados de forma aleatória.
* **Forward Propagation**: os dados de entrada são propagados pela rede neural.
* **Cálculo do Erro**: o erro é calculado a partir da diferença entre a saída da rede neural e o valor esperado.
* **Backward Propagation**: (Retro propagação ou backpropagation) o erro é propagado pela rede neural, ajustando os pesos.
* **Atualização dos Pesos**: os pesos da rede neural são atualizados com base no erro calculado.
* **Iteração**: o processo de treinamento, teste e predição é repetido até que a rede neural atinja a precisão desejada.

## Funções de Ativação

As funções de ativação são essenciais para determinar a saída de um neurônio. Elas introduzem não linearidades nos cálculos da rede, permitindo que as redes neurais aprendam padrões complexos.

* **ReLU (Rectified Linear Unit):** Mapeia valores negativos para zero e mantém os valores positivos. É amplamente utilizada em redes neurais profundas.
* **Sigmoide:** Transforma as entradas em valores entre 0 e 1. É usada principalmente para classificações binárias.
* **Tanh:** Mapeia valores para o intervalo entre -1 e 1, sendo útil em problemas que envolvem sinais de entrada positivos e negativos.

## Palavras-Chave

* **Redes Neurais:** modelo computacional inspirado no sistema nervoso biológico.
* **Deep Learning:** subárea de machine learning que utiliza redes neurais profundas.
* **Machine Learning:** área da inteligência artificial que se concentra no desenvolvimento de algoritmos que aprendem a partir de dados.
* **Inteligência Artificial:** campo da ciência da computação que se concentra no desenvolvimento de sistemas inteligentes.
* **Perceptron:** modelo mais simples de rede neural, composto por um único neurônio artificial.
* **Multilayer Perceptron (MLP):** rede neural feedforward composta por múltiplas camadas de neurônios.
* **Redes Neurais Convolucionais (CNN):** redes neurais especializadas em processamento de imagens.
* **Redes Neurais Recorrentes (RNN):** redes neurais com conexões recorrentes, ideais para dados sequenciais.
* **Redes Neurais Generativas Adversariais (GANs):** redes neurais compostas por um gerador e um discriminador que competem entre si.
* **Forward Propagation:** propagação dos dados de entrada pela rede neural.
* **Backward Propagation:** propagação do erro pela rede neural para ajustar os pesos.
* **Treinamento de Redes Neurais:** processo de ajuste dos pesos da rede neural para aprender padrões nos dados.
* **Processamento de Linguagem Natural (NLP):** área da inteligência artificial que se concentra no processamento de texto e linguagem humana.
* **Visão Computacional:** área da inteligência artificial que se concentra no processamento de imagens e vídeos.
* **Reconhecimento de Padrões:** área da inteligência artificial que se concentra na identificação de padrões em dados.
* **Sigmoide:** função de ativação que mapeia valores reais para o intervalo [0, 1].
* **Neuronio:** unidade básica de processamento em uma rede neural, que recebe entradas, aplica pesos e produz uma saída.
* **Função de Ativação:** função matemática que determina a saída de um neurônio com base em suas entradas.
* **Mean Squared Error (MSE):** métrica de erro que calcula a média dos quadrados das diferenças entre a saída da rede e o valor esperado.
* **Root Mean Squared Error (RMSE):** métrica de erro que calcula a raiz quadrada da média dos quadrados das diferenças entre a saída da rede e o valor esperado.
* **Backpropagation:** algoritmo de treinamento de redes neurais que ajusta os pesos com base no erro calculado.
* **Gradient Descent:** algoritmo de otimização que ajusta os pesos da rede neural para minimizar o erro.
* **Overfitting:** problema em que a rede neural se ajusta demais aos dados de treinamento e não generaliza bem para novos dados.
* **Underfitting:** problema em que a rede neural não se ajusta adequadamente aos dados de treinamento e não consegue aprender padrões.
* **Regularização:** técnica utilizada para evitar overfitting, adicionando termos de penalização aos pesos da rede neural.

## Tipos de Redes Neurais

Existem diversos tipos de redes neurais, cada uma com características e aplicações específicas. 

* **Perceptron**: o perceptron é o modelo mais simples de rede neural, composto por um único neurônio artificial.
* **Multilayer Perceptron (MLP)**: o MLP é uma rede neural feedforward composta por múltiplas camadas de neurônios.
* **Redes Neurais Convolucionais (CNN)**: as CNNs são redes neurais especializadas em processamento de imagens, que utilizam camadas convolucionais para extrair características.
* **Redes Neurais Recorrentes (RNN)**: as RNNs são redes neurais que possuem conexões recorrentes, permitindo que informações sejam propagadas ao longo do tempo.
* **Redes Neurais Generativas Adversariais (GANs)**: as GANs são redes neurais compostas por um gerador e um discriminador, que são treinados de forma adversarial para gerar dados realistas.

## 1. Perceptron Simples

O Perceptron é o modelo mais básico de rede neural, composto por um único neurônio. Ele realiza tarefas de classificação binária, onde a saída é 0 ou 1. O perceptron aplica uma função de ativação (geralmente uma função degrau) à soma ponderada das entradas para produzir uma saída.

* **Aplicações:** Classificação de dados linearmente separáveis.
* **Limitações:** Não consegue resolver problemas que envolvem dados não linearmente separáveis, como o problema do XOR.

## 2. Multilayer Perceptron (MLP)

O MLP é uma rede neural composta por múltiplas camadas de neurônios, com uma ou mais camadas ocultas entre a camada de entrada e a camada de saída. Essa estrutura permite que o MLP resolva problemas mais complexos que o perceptron simples.

* **Aplicações:** Reconhecimento de padrões, classificação de imagens, regressão.
* **Vantagens:** Capacidade de resolver problemas não linearmente separáveis.
* **Desvantagens:** Requer grandes volumes de dados e poder computacional.

## 3. Redes Neurais Convolucionais (CNNs)

As CNNs são especializadas em processamento de dados em grade, como imagens. Elas utilizam camadas convolucionais para extrair características locais da imagem e camadas de pooling para reduzir a dimensionalidade. As CNNs são usadas amplamente em tarefas de visão computacional.

* **Aplicações:** Classificação de imagens, detecção de objetos, segmentação de imagens.
* **Vantagens:** Capacidade de extrair características complexas, redução de dimensionalidade, eficiente em imagens.
* **Desvantagens:** Necessidade de grandes volumes de dados e alta demanda computacional.

### Estrutura de uma CNN:

* **Camadas Convolucionais:** Extrai características locais da imagem (bordas, texturas, etc.).
* **Camadas de Pooling:** Reduz a dimensionalidade das características, preservando a informação mais importante.
* **Camadas Densas:** Realiza a classificação final com base nas características extraídas.

## 4. Redes Neurais Recorrentes (RNNs)

As RNNs são adequadas para dados sequenciais. Elas possuem conexões que permitem que informações anteriores influenciem a saída atual, tornando-as ideais para tarefas como séries temporais, processamento de texto e reconhecimento de fala. No entanto, as RNNs sofrem de problemas de vanishing gradient, o que limita sua capacidade de capturar dependências de longo prazo.

* **Aplicações:** Tradução automática, reconhecimento de fala, análise de séries temporais.
* **Vantagens:** Capacidade de capturar dependências temporais em dados sequenciais.
* **Desvantagens:**  Sofrem de problemas de vanishing gradient, dificultando o aprendizado de longas dependências temporais.

### Variações de RNNs: ###

* **LSTM (Long Short-Term Memory):** Introduz uma estrutura de "portas" que controla o fluxo de informação, permitindo que a rede capture dependências de longo prazo.
* **GRU (Gated Recurrent Unit):** Simples como o LSTM, mas com menos parâmetros, também resolve o problema de vanishing gradient.

## 5. Redes Neurais Generativas Adversariais (GANs)

As GANs são compostas por duas redes que competem entre si: um gerador e um discriminador. O gerador tenta criar dados falsos (por exemplo, imagens) que se parecem com dados reais, enquanto o discriminador tenta distinguir entre os dados reais e os gerados. Essa competição melhora continuamente a qualidade dos dados gerados.

* **Aplicações:** Geração de imagens realistas, criação de arte, aumento de resolução de imagens.
* **Vantagens:** Capacidade de gerar dados sintéticos altamente realistas.
* **Desvantagens:** Difícil de treinar, instabilidade durante o treinamento.


## Fontes e Referências

1. [Deep Learning](https://en.wikipedia.org/wiki/Deep_learning)
2. [Machine Learning](https://en.wikipedia.org/wiki/Machine_learning)
3. [Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence)
4. [Perceptron](https://en.wikipedia.org/wiki/Perceptron)
5. [Multilayer Perceptron](https://en.wikipedia.org/wiki/Multilayer_perceptron)
6. [Convolutional Neural Network](https://en.wikipedia.org/wiki/Convolutional_neural_network)
7. [Recurrent Neural Network](https://en.wikipedia.org/wiki/Recurrent_neural_network)
8. [Generative Adversarial Network](https://en.wikipedia.org/wiki/Generative_adversarial_network)
9. [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
10. [Understanding GRU Networks](https://towardsdatascience.com/understanding-gru-networks-2ef37df6c9be)
11. [GANs in Action](https://www.manning.com/books/gans-in-action)
12. [Deep Learning with Python](https://www.manning.com/books/deep-learning-with-python)
13. [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/)
14. [Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning)
15. [GANs Specialization](https://www.coursera.org/specializations/generative-adversarial-networks-gans)
16. [Deep Learning Book](https://www.deeplearningbook.org/)
17. [Neural Networks and Learning Machines](https://www.amazon.com/Neural-Networks-Learning-Machines-3rd/dp/0131471392)
18. [Pattern Recognition and Machine Learning](https://www.amazon.com/Pattern-Recognition-Learning-Information-Statistics/dp/0387310738)
19. [Introduction to the Theory of Neural Computation](https://www.amazon.com/Introduction-Theory-Neural-Computation-Volume/dp/0201515601)
20. [Neural Networks for Pattern Recognition](https://www.amazon.com/Neural-Networks-Pattern-Recognition-Christopher/dp/0198538642)

### Referências Adicionais

1. [AWS CDK Documentation](https://docs.aws.amazon.com/cdk/latest/guide/home.html)
2. [Amazon SageMaker Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
3. [Amazon DynamoDB Documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
4. [Postman Documentation](https://learning.postman.com/docs/getting-started/introduction/)
5. [CloudFormation Documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)