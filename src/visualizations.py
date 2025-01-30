import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(file_path):
    """Carrega o dataset limpo"""
    return pd.read_csv(file_path)

def plot_area_vs_rent(df):
    """Gráfico de dispersão entre área e aluguel."""
    sns.scatterplot(data=df, x='area', y='rent')
    plt.title('Relação entre Área vs Aluguel')
    plt.xlabel('Área (m²)')
    plt.ylabel('Aluguel (R$)')
    plt.show()

def plot_bedrooms_vs_rent(df):
    """"Gráfico de dispersão entre quantidade de quartos e aluguel."""
    sns.scatterplot(data=df,  x='bedrooms', y='rent')
    plt.title('Relação entre quantidade de Quartos vs Aluguel')
    plt.xlabel('Quantidade de quartos')
    plt.ylabel('Aluguel (R$)')
    plt.show()

def plot_garage_vs_rent(df):
    """Gráfico de dispersão entre vagas na garagem e aluguel."""
    sns.scatterplot(data=df, x='garage', y='rent')
    plt.title('Relação entre vagas na Garagem vs Aluguel')
    plt.xlabel('Quantidade de vagas (garagem)')
    plt.ylabel('Aluguel (R$)')
    plt.show()

def plot_area_vs_rent_by_zone(df):
    """Gráfico de dispersão entre área e aluguel, separado por zona."""
    # Identifica as colunas que representam as zonas
    zone_columns = [col for col in df.columns if col.startswith('zone')]

    plt.figure(figsize=(6, 4))
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
    zone_columns = [col for col in df.columns if col.startswith('zone_')]  # Corrigido para usar 'df'

    zone_rent_mean = {}
    for zone in zone_columns:
        # Multiplica o valor da coluna dummy pelo aluguel e calcula a média
        zone_rent_mean[zone.replace('zone_', '')] = df.loc[df[zone] == 1, 'rent'].mean()

    # Criar o gráfico de barras
    plt.figure(figsize=(6, 4))
    plt.bar(zone_rent_mean.keys(), zone_rent_mean.values(), color='skyblue') 
    plt.title('Média dos Aluguéis por Zona')
    plt.xlabel('Zona')
    plt.ylabel('Média do Aluguel (R$)')
    plt.xticks(rotation=45)
    plt.savefig('outputs/charts/plot_avg_rent_by_zone.png', dpi=300, bbox_inches='tight')
    plt.show()


def plot_avg_rent_by_property_type(df):
    """Gráfico de barras da média do aluguel por tipo de moradia."""
    # Identificar as colunas que representam os tipos de imóveis
    type_columns = [col for col in df.columns if col.startswith('type_')]

    # Calcular a média do aluguel para cada tipo
    property_rent_mean = {}
    for property_type in type_columns:
        property_rent_mean[property_type.replace('type_', '')] = df.loc[df[property_type] == 1, 'rent'].mean()

    # Criar o gráfico de barras
    plt.figure(figsize=(6, 4))
    plt.bar(property_rent_mean.keys(), property_rent_mean.values(), color='skyblue')
    plt.title('Média dos Aluguéis por Tipo de Moradia')
    plt.xlabel('Tipo de Moradia')
    plt.ylabel('Média do Aluguel (R$)')
    plt.xticks(rotation=45)
    plt.savefig('outputs/charts/plot_avg_rent_by_property_type.png', dpi=300, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    df_clean = load_data('data/processed/dataset_imoveis_sp_clean.csv')


def generate_all_plots(df):
    """Gera e salva todos os gráficos."""
    
    plot_area_vs_rent(df, save_path='outputs/charts/area_vs_rent.png')
    plot_bedrooms_vs_rent(df, save_path='outputs/charts/bedrooms_vs_rent.png')
    plot_garage_vs_rent(df, save_path='outputs/charts/garage_vs_rent.png')
    plot_area_vs_rent_by_zone(df, save_path='outputs/charts/area_vs_rent_by_zone.png')
    plot_avg_rent_by_zone(df, save_path='outputs/charts/avg_rent_by_zone.png')

generate_all_plots(df_clean)


