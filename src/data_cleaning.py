import pandas as pd

def map_district_to_zone(df, column_name="district"):
    """
    Adiciona uma coluna de zona com base no mapeamento de bairros.

    Args:
        df (pd.DataFrame): O DataFrame contendo os dados.
        column_name (str): O nome da coluna com os bairros (distritos).

    Returns:
        pd.DataFrame: O DataFrame atualizado com a coluna 'zone'.
    """
    # Mapeia as zonas administrativas
    zona_mapping = {
    # CENTRO
    "Bela Vista": "Centro",
    "Bom Retiro": "Centro",
    "Cambuci": "Centro",
    "Consolação": "Centro",
    "Higienópolis": "Centro",
    "Liberdade": "Centro",
    "República": "Centro",
    "Santa Cecília": "Centro",
    "Sé": "Centro",
    # LESTE
    "Água Rasa": "Leste",
    "Aricanduva": "Leste",
    "Belenzinho": "Leste",
    "Carrão": "Leste",
    "Vila Carrão": "Leste",
    "Vila Formosa": "Leste",
    "Ermelino Matarazzo": "Leste",
    "Ponte Rasa": "Leste",
    "Lajeado": "Leste",
    "Vila Curuçá": "Leste",
    "Itaquera": "Leste",
    "Cidade Líder": "Leste",
    "José Bonifácio": "Leste",
    "Parque do Carmo": "Leste",
    "Mooca": "Leste",
    "Belém": "Leste",
    "Brás": "Leste",
    "Moóca": "Leste",
    "Pari": "Leste",
    "Tatuapé": "Leste",
    "Penha": "Leste",
    "Artur Alvim": "Leste",
    "Cangaíba": "Leste",
    "Penha": "Leste",
    "Vila Matilde": "Leste",
    "São Mateus": "Leste",
    "São Rafael": "Leste",
    "São Miguel": "Leste", 
    "Jardim Helena": "Leste",
    "Vila Jacuí": "Leste",
    "Sapopemba": "Leste",
    "Vila Prudente": "Leste",
    "São Lucas": "Leste",
    # NORTE
    "Casa Verde": "Norte",
    "Cachoeirinha": "Norte",
    "Limão": "Norte",
    "Brasilândia": "Norte",
    "Freguesia do Ó": "Norte",
    "Jaçanã": "Norte",
    "Tremembé": "Norte",
    "Perus": "Norte",
    "Anhanguera": "Norte",
    "Pirituba":"Norte",
    "Jaraguá": "Norte",
    "São Domingos": "Norte",
    "Santana": "Norte", 
    "Tucuruvi": "Norte",
    "Mandaqui": "Norte",
    "Vila Maria": "Norte",
    "Vila Guilherme": "Norte",
    "Vila Medeiros": "Norte",
    "Vila Nova Cachoeirinha": "Norte",
    # OESTE
    "Butantã": "Oeste",
    "Morumbi": "Oeste",
    "Raposo Tavares": "Oeste",
    "Rio Pequeno": "Oeste",
    "Vila Sônia": "Oeste",
    "Vila Jaguara": "Oeste",
    "Lapa": "Oeste",
    "Barra Funda": "Oeste",
    "Jaguara": "Oeste",
    "Jaguaré": "Oeste",
    "Perdizes": "Oeste",
    "Vila Leopoldina": "Oeste",
    "Pinheiros": "Oeste",
    "Alto do Pinheiros": "Oeste",
    "Alto de Pinheiros": "Oeste",
    "Itaim Bibi": "Oeste",
    "Jardim Paulista": "Oeste",
    "Pinheiros": "Oeste",
    "Vila Olímpia": "Oeste",
    # SUL
    "Campo Limpo": "Sul",
    "Capão Redondo": "Sul",
    "Vila Andrade": "Sul",
    "Cidade Dutra": "Sul",
    "Grajaú": "Sul",
    "Socorro": "Sul",
    "Cidade Ademar": "Sul",
    "Pedreira": "Sul",
    "Ipiranga": "Sul",
    "Sacomã": "Sul",
    "Jabaquara": "Sul",
    "M'Boi Mirim'": "Sul",
    "Jardim Ângela": "Sul",
    "Jardim São Luís": "Sul",
    "Parelheiros": "Sul",
    "Marsilac": "Sul",
    "Santo Amaro": "Sul",
    "Campo Belo": "Sul",
    "Campo Grande": "Sul",
    "Santo Amaro": "Sul",
    "Moema": "Sul",
    "Saúde": "Sul",
    "Vila Mariana": "Sul", 
    "Paraíso": "Sul",   
}

    # Mapear os bairros para zonas
    df["zone"] = df[column_name].map(zona_mapping)

    # Remover a coluna rua(address) e bairro(district)
    df.drop(columns=["address", column_name, "total"], inplace=True)

    return df

def clean_data_basic(df):
    """
    Limpeza básica dos dados: remoção de outliers, conversão de variáveis categóricas e
    remoção de linhas que contém valores 'False' em todos as colunas de zones.

    Args:
        df (pd.DataFrame): O DataFrame contendo os dados.

    Returns:
        pd.DataFrame: O DataFrame limpo.
    """
    # Remove os outliers baseado na área e no preço de aluguel
    df = df[(df['area'] > 20) & (df['area'] < 400) & (df['rent'] > 549) & (df['rent'] < 15001)]

    # Converte as variáveis categóricas para numéricas
    df = pd.get_dummies(df, columns=['zone', 'type'])

    # Seleciona apenas as colunas com relação a zona
    zone_columns = [col for col in df.columns if 'zone_' in col]
    
    # Remove as linhas que são 'False' para todas as colunas de zonas
    df = df.loc[~(df[zone_columns] == 0).all(axis=1)]
    return df

# Fluxo de processamento integrado
df_raw = pd.read_csv('data/raw/dataset_imoveis_sp.csv')

# Aplica mapeamento e limpeza
df_mapped = map_district_to_zone(df_raw)
df_clean = clean_data_basic(df_mapped)

# Salva o dataset limpo
df_clean.to_csv('data/processed/dataset_imoveis_sp_clean.csv', index=False)
