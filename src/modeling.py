__all__ = [
    'train_model'
]

from sklearn.linear_model import LinearRegression

def train_model(X_train, y_train):
    """
    Treina um modelo de regressão linear com os dados fornecidos.
    
    Parâmetros:
    X_train: DataFrame - Variáveis preditoras para treino
    y_train: Series - Variável alvo para treino
    
    Retorna:
    model: Modelo treinado
    """
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model