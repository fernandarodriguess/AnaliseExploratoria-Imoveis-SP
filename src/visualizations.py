import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Carrega o dataset limpo"""
    return pd.read_csv(file_path)

def plot_area_vs_rent(df):
    """Gráfico de disposição entre área e aluguel."""
    sns.scatterplot(data=df, x='area', y='rent')
    plt.title('Área vs Aluguel')
    plt.xlabel('Área (m²)')
    plt.ylabel('Aluguel (R$)')
    plt.show()

def plot_bedrooms_vs_rent(df):
    """"Gráfico de dispersão entre quantidade de quartos e aluguel."""
    sns.scatterplot(data=df,  x='bedrooms', y='rent')
    plt.title('Quartos vs Aluguel')
    plt.xlabel('Quantidade de quartos')
    plt.ylabel('Aluguel (R$)')
    plt.show()

def plot_garage_vs_rent(df):
    """Gráfico de dispersão entre vagas na gareagem e aluguel."""
    sns.scatterplot(data=df, x='garage', y='rent')
    plt.title('Garagem vs Aluguel')
    plt.xlabel('Quantidade de vagas (garagem)')
    plt.ylabel('Aluguel (R$)')
    plt.show()

def plot_area_vs_rent_by_zone(df):
    """Gráfico de dispersão entre área e aluguel, separando por zona."""
    # Identifica as colunas que representam as zonas
    zone_columns = [col for col in df.columns if col.startswith('zone')]
    
    plt.figure(figsize=(10, 6))

    # Loop que adiciona os pontos de cada zona no scatter plot
    for zone in zone_columns:
        zone_name = zone.replace('zone_', '')
        df_zone = df[df[zone] == 1]  
        plt.scatter(
            df_zone['area'],   
            df_zone['rent'],   
            label=zone_name,   
            alpha=0.6,         
        )

    plt.title('Relação entre Área e Aluguel por Zona')
    plt.xlabel('Área (m²)')
    plt.ylabel('Aluguel (R$)')
    plt.legend(title='Zona')
    plt.grid(alpha=0.3)
    plt.show()

def plot_avg_rent_by_zone(df):
    """Gráfico de barras da média do aluguel por zona."""
    zone_columns = [col for col in df.columns if col.startswith('zone_')]

    # Calcula a média do aluguel
    zone_rent_mean = {}
    for zone in zone_columns:
        zone_rent_mean[zone.replace('zone_', '')] = df.loc[df[zone]]

    plt.figure(figsize=(10, 6))
    plt.bar(zone_rent_mean.keys(), zone_rent_mean.values(), color='skyblue')
    plt.title('Média dos Aluguéis por Zona')
    plt.xlabel('Zona')
    plt.ylabel('Média do Aluguel (R$)')
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    df_clean = load_data('data/processed/dataset_imoveis_sp_clean.csv')

    plot_area_vs_rent(df_clean)
    plot_bedrooms_vs_rent(df_clean)
    plot_garage_vs_rent(df_clean)
    plot_area_vs_rent_by_zone(df_clean)
    plot_avg_rent_by_zone(df_clean)



