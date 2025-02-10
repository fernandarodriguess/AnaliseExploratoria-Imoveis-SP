import os
import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def train_and_save_models(file_path="data/processed/dataset_imoveis_sp_clean.csv", output_dir="outputs/models"):
    # Carregar dataset
    df = pd.read_csv(file_path)
    print(f"Dataset carregado com {len(df)} registros.")
    
    # Criar diretório de saída se não existir
    os.makedirs(output_dir, exist_ok=True)
    print(f"Diretório de saída: {output_dir}")
    
    # Variáveis preditoras e alvo
    features = ['area', 'bedrooms', 'garage', 'type_Apartamento', 'type_Casa', 'type_Casa em condomínio', 'type_Studio e kitnet']
    alvo = 'rent'
    
    # Dicionário para armazenar métricas
    metrics_dict = {}
    
    # Loop sobre os bairros únicos
    districts = df['district'].unique()
    print(f"Encontrados {len(districts)} bairros únicos.")
    
    for district in districts:
        print(f"Processando bairro: {district}")
        df_district = df[df['district'] == district]
        
        # Remover registros duplicados
        df_district = df_district.drop_duplicates()
        
        # Separar em treino e teste (removendo "Outros" apenas do treino)
        df_train = df_district[df_district['district'] != 'Outros']
        df_test = df_district.copy()
        
        print(f"Tamanho do treino para {district}: {len(df_train)}")
        print(f"Tamanho do teste para {district}: {len(df_test)}")
        
        # Garantir que há dados suficientes
        if len(df_train) < 10:
            print(f"Poucos dados para o bairro {district}, pulando...")
            continue
        
        X_train, y_train = df_train[features], df_train[alvo]
        X_test, y_test = df_test[features], df_test[alvo]
        
        # Treinar o modelo
        model = LinearRegression()
        model.fit(X_train, y_train)
        print(f"Modelo treinado para {district}.")
        
        # Avaliar o modelo
        y_pred = model.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        mae = mean_absolute_error(y_test, y_pred)
        
        # Armazenar métricas
        metrics_dict[district] = {'R²': r2, 'RMSE': rmse, 'MAE': mae}
        print(f"Métricas para {district}: R²={r2:.4f}, RMSE={rmse:.2f}, MAE={mae:.2f}")
        
        # Salvar o modelo
        model_filename = os.path.join(output_dir, f'model_{district}.joblib')
        joblib.dump(model, model_filename)
        print(f"Modelo salvo em {model_filename}")

    # Calcular a média das métricas dos modelos treinados
    if metrics_dict:
        avg_r2 = np.mean([m['R²'] for m in metrics_dict.values()])
        avg_rmse = np.mean([m['RMSE'] for m in metrics_dict.values()])
        avg_mae = np.mean([m['MAE'] for m in metrics_dict.values()])

    print("\nMédias das métricas dos modelos treinados:")
    print(f"R² médio: {avg_r2:.4f}")
    print(f"RMSE médio: {avg_rmse:.2f}")
    print(f"MAE médio: {avg_mae:.2f}")

    # Adicionar as médias no arquivo CSV
    metrics_dict['Média Geral'] = {'R²': avg_r2, 'RMSE': avg_rmse, 'MAE': avg_mae}

    
    # Salvar métricas
    metrics_df = pd.DataFrame.from_dict(metrics_dict, orient='index')
    metrics_df.to_csv(os.path.join(output_dir, 'model_metrics.csv'))
    print("Métricas salvas em outputs/model_metrics.csv")

if __name__ == "__main__":
    train_and_save_models()
