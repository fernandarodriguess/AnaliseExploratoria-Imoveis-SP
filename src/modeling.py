__all__ = [
    'split_data',
    'train_model',
    'evaluate_model',
    'predicted_rent',
    'save_metrics'
]

import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def split_data(df, target, test_size=0.2, random_state=42):
    """
    Divide os dados em conjuntos de treinamento e teste.

    Parâmetros:
        df (DataFrame): Dataset completo.
        target (str): Nome da coluna alvo.
        test_size (float): Proporção de dados para teste.
        random_state (int): Semente para reprodução.

    Retorna:
        tuple: X_train, X_test, y_train, y_test
    """
    X = df.drop(columns=[target])
    y = df[target]
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def train_model(X_train, y_train):
    """
    Treina o modelo de regressão linear.

    Parâmetros:
        X_train (DataFrame): Dados de treinamento.
        y_train (Series): Alvos de treinamento.

    Retorna:
        model (LinearRegression): Modelo treinado.
    """
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    """
    Avalia o modelo usando métricas de regressão.

    Parâmetros:
        model (LinearRegression): Modelo treinado.
        X_test (DataFrame): Dados de teste.
        y_test (Series): Valores reais dos alvos.

    Retorna:
        dict: Métricas de avaliação (MAE, RMSE, R²).
    """
    y_pred = model.predict(X_test)
    metrics = {
        "MAE": mean_absolute_error(y_test, y_pred),
        "RMSE": np.sqrt(mean_squared_error(y_test, y_pred)),
        "R2": r2_score(y_test, y_pred)
    }
    return metrics


def predicted_rent(model, new_data):
    """
    Faz previsões do aluguel para novos dados.

    Parâmetros:
        model (LinearRegression): Modelo treinado.
        new_data (DataFrame): Novos dados com as mesmas features usadas no treinamento.

    Retorna:
        np.array: Previsões dos aluguéis.
    """
    return model.predict(new_data)


def save_metrics(metrics, output_path):
    """
    Salva as métricas em um arquivo de texto.

    Parâmetros:
        metrics (dict): Métricas de avaliação.
        output_path (str): Caminho do arquivo para salvar.

    Retorna:
        None
    """
    with open(output_path, "w") as f:
        for metric, value in metrics.items():
            f.write(f"{metric}: {value:.4f}\n")