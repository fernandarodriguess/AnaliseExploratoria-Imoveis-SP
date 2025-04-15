# Linear Regression Machine Learning - Imóveis em São Paulo

Esse projeto tem o intuito de mapear os principais bairros das zonas administrativas da cidade de São Paulo, a fim de treinar um modelo de Regressão Linear que possa prever os valores de aluguel.

Até o momento, foi realizada a etapa de análise exploratória, na qual foram examinadas as distribuições das variáveis presentes na base de dados bruta, além da criação de visualizações gráficas para apoiar a compreensão dos padrões. Todo o processo está documentado no notebook: [Análise Exploratória de Dados](notebooks/01_data_exploration.ipynb).

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


