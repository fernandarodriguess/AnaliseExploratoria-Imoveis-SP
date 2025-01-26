import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/processed/dataset_imoveis_sp_clean.csv')

def plot_area_vs_rent(df):

    sns.scatterplot(data=df, x='area', y='rent')
    
    plt.title('Área vs Aluguel')
    plt.xlabel('Área (m²)')
    plt.ylabel('Aluguel (R$)')
    
    plt.show()

plot_area_vs_rent(df)
