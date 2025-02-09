import pandas as pd
import unicodedata

def map_district_to_zone(df, column_name="district"):
    """
    Adiciona uma coluna 'zone' com base no mapeamento de bairros.
    Caso o bairro não esteja no mapeamento, define a zona como 'Outro'.
    """
    zona_mapping = {
        # Centro
        "Bela Vista": "Centro", "Bom Retiro": "Centro", "Cambuci": "Centro",
        "Consolação": "Centro", "Higienópolis": "Centro", "Liberdade": "Centro",
        "República": "Centro", "Santa Cecília": "Centro", "Sé": "Centro",
        # Leste
        "Água Rasa": "Leste", "Aricanduva": "Leste", "Belenzinho": "Leste",
        "Carrão": "Leste", "Vila Carrão": "Leste", "Vila Formosa": "Leste",
        "Ermelino Matarazzo": "Leste", "Ponte Rasa": "Leste", "Lajeado": "Leste",
        "Vila Curuçá": "Leste", "Itaquera": "Leste", "Cidade Líder": "Leste",
        "José Bonifácio": "Leste", "Parque do Carmo": "Leste", "Mooca": "Leste",
        "Belém": "Leste", "Brás": "Leste", "Moóca": "Leste", "Pari": "Leste",
        "Tatuapé": "Leste", "Penha": "Leste", "Artur Alvim": "Leste",
        "Cangaíba": "Leste", "Vila Matilde": "Leste", "São Mateus": "Leste",
        "São Rafael": "Leste", "São Miguel": "Leste", "Jardim Helena": "Leste",
        "Vila Jacuí": "Leste", "Sapopemba": "Leste", "Vila Prudente": "Leste",
        "São Lucas": "Leste",
        # Norte
        "Casa Verde": "Norte", "Cachoeirinha": "Norte", "Limão": "Norte",
        "Brasilândia": "Norte", "Freguesia do Ó": "Norte", "Jaçanã": "Norte",
        "Tremembé": "Norte", "Perus": "Norte", "Anhanguera": "Norte",
        "Pirituba": "Norte", "Jaraguá": "Norte", "São Domingos": "Norte",
        "Santana": "Norte", "Tucuruvi": "Norte", "Mandaqui": "Norte",
        "Vila Maria": "Norte", "Vila Guilherme": "Norte", "Vila Medeiros": "Norte",
        "Vila Nova Cachoeirinha": "Norte",
        # Oeste
        "Butantã": "Oeste", "Morumbi": "Oeste", "Raposo Tavares": "Oeste",
        "Rio Pequeno": "Oeste", "Vila Sônia": "Oeste", "Vila Jaguara": "Oeste",
        "Lapa": "Oeste", "Barra Funda": "Oeste", "Jaguara": "Oeste",
        "Jaguaré": "Oeste", "Perdizes": "Oeste", "Vila Leopoldina": "Oeste",
        "Pinheiros": "Oeste", "Alto do Pinheiros": "Oeste", "Itaim Bibi": "Oeste",
        "Jardim Paulista": "Oeste", "Vila Olímpia": "Oeste",
        # Sul
        "Campo Limpo": "Sul", "Capão Redondo": "Sul", "Vila Andrade": "Sul",
        "Cidade Dutra": "Sul", "Grajaú": "Sul", "Socorro": "Sul",
        "Cidade Ademar": "Sul", "Pedreira": "Sul", "Ipiranga": "Sul",
        "Sacomã": "Sul", "Jabaquara": "Sul", "M'Boi Mirim": "Sul",
        "Jardim Ângela": "Sul", "Jardim São Luís": "Sul", "Parelheiros": "Sul",
        "Marsilac": "Sul", "Santo Amaro": "Sul", "Campo Belo": "Sul",
        "Campo Grande": "Sul", "Moema": "Sul", "Saúde": "Sul",
        "Vila Mariana": "Sul", "Paraíso": "Sul"
    }
    df["zone"] = df[column_name].map(zona_mapping).fillna("Outro")
    return df

def group_rare_districts(df, column="district", threshold=20, new_value="Outros"):
    """
    Substitui distritos com menos de 'threshold' ocorrências por 'Outros'.
    """
    counts = df[column].value_counts()
    df[column] = df[column].apply(lambda x: new_value if counts[x] < threshold else x)
    return df

def remove_accented_chars(text):
    """
    Remove acentos de um texto.
    """
    return unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')

def limpar_nome(nome):
    """
    Remove espaços extras do nome.
    """
    return ' '.join(nome.split())

def create_dummies(df, column="type"):
    """
    Cria variáveis dummies para a coluna 'type'.
    """
    dummies = pd.get_dummies(df[column], prefix=column)
    df = pd.concat([df, dummies], axis=1)
    df.drop(columns=[column], inplace=True)
    return df

if __name__ == "__main__":
    pd.set_option('display.max_rows', 200)

    # Carregar dados brutos
    df_raw = pd.read_csv("data/raw/dataset_imoveis_sp.csv")

    # Normalização de nomes
    df_raw["district"] = df_raw["district"].apply(remove_accented_chars).apply(limpar_nome)
    df_raw["address"] = df_raw["address"].apply(remove_accented_chars).apply(limpar_nome)

    # Agrupar distritos raros
    df_raw = group_rare_districts(df_raw)

    # Mapear zona
    df_mapped = map_district_to_zone(df_raw)

    # Criar variáveis dummies para 'type'
    df_processed = create_dummies(df_mapped)

    # Salvar dataset processado
    df_processed.to_csv("data/processed/dataset_imoveis_sp_clean.csv", index=False)

    print(df_processed.head())
