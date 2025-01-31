# Linear Regression Machine Learning - Imóveis em São Paulo

Esse projeto tem o intuito de mapear os principais bairros das zonas administrativas da cidade de São Paulo, a fim de treinar um modelo de Regressão Linear que possa prever os valores de aluguel.

## Arquitetura do projeto

```
LinearRegression-ML-Imoveis-SaoPaulo/
│
├── data/                              # Dados do projeto
│   ├── raw/                           # Dados originais (não processados)
│   │   └── dataset_imoveis_sp.csv     # Arquivo bruto do dataset
│   ├── processed/                     # Dados prontos (tratados e limpos)
│       └── dataset_imoveis_sp_clean.csv # Dados finais prontos para análise
│
├── notebooks/               # Notebooks
│   ├── 01_data_exploration.ipynb  # Análise exploratória
│   ├── 02_linear_regression.ipynb # Modelo de regressão linear
│
├── src/                     # Scripts auxiliares (usado para funções)
│   ├── data_cleaning.py     # Funções para limpeza de dados
│   ├── visualizations.py    # Funções para gráficos
│   ├── modeling.py          # Funções para treinar o modelo
│
├── outputs/                 # Resultados e saídas do modelo
│   ├── charts/              # Gráficos gerados durante o projeto
│   │   └── linear_regression_model.pkl  # Modelo de regressão linear gerado
│   └── metrics.txt          # Métricas do modelo
│
└── README.md                # Documentação do projeto
```

## Tecnologias
- **Python 3**: para a programação do projeto.
- **Pandas**: para leitura e análise dos dados.
- **NumPy**: para computação científica com arrays.
- **Scikit-Learn**: para construção do modelo de machine learning.

## Dataset
O conjunto de dados brutos possui informações de 11.658 imóveis de diversas regiões do estado de São Paulo, com as seguintes colunas:

- **address**: o endereço do imóvel
- **district**: o bairro onde o imóvel está localizado
- **area**: a área do imóvel em metros quadrados
- **bedrooms**: o número de quartos na propriedade
- **garage**: o número de vagas de estacionamento disponíveis na propriedade
- **type**: o tipo do imóvel (apartamento, casa, etc.)
- **rent**: o aluguel mensal do imóvel
- **total**: o custo total do imóvel, incluindo aluguel, impostos e outras taxas

Após a realização da limpeza e tratamento dos dados, foi possível obter um dataset com 3.913 registros de imóveis, contendo as seguintes colunas:

- **area**: a área do imóvel em metros quadrados
- **bedrooms**: o número de quartos na propriedade
- **garage**: o número de vagas de estacionamento disponíveis na propriedade
- **rent**: o aluguel mensal do imóvel
- **zone_Centro**
- **zone_Leste**
- **zone_Norte**
- **zona_Oeste**
- **zona_Sul**
- **type_Apartamento**
- **type_Casa**
- **type_Casa em condomínio**
- **type_Studio e kitnet**

## Treinamento
No processo de treinamento, o código está modularizado e conta com as seguintes funções:

- **split_data**: Divide os dados em treinamento e teste.
- **train_model**: Treina o modelo de regressão linear.
- **evaluate_model**: Calcula métricas de desempenho.
- **predicted_rent**: Faz previsões com base em novos dados.
- **save_metrics**: Salva métricas em um arquivo.

## Avaliação das Métricas
- **MAE** (Mean Absolute Error): 1102.0627
- **RMSE** (Root Mean Squared Error): 1640.7997
- **R²** (Coeficiente de Determinação): 0.5705

