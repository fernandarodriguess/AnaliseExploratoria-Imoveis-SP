import pandas as pd
import numpy as np

def clean_data(df):

    # Remover outliers baseado na área e no preço de aluguel
    df = df[(df['area'] > 20) & (df['area'] < 400) & (df['rent'] > 549) & (df['rent'] < 15001)]

    # Conversão de variáveis categóricas para numéricas
    df = pd.get_dummies(df, columns=['district', 'type'], drop_first=True)
    
    return df

df_clean = clean_data(pd.read_csv('data/raw/dataset_imoveis_sp.csv'))
df_clean.to_csv('data/processed/dataset_imoveis_sp_clean.csv', index=False)
