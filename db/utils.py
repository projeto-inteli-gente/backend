from intelligentedb.indicators import read_data as dbrd
import pandas as pd

def get_city_indicator(indicator_name: str, municipio_id: int):
    response = dbrd.get_datapoints_values(indicator_name)
    df = response[response['municipio_id'] == municipio_id].reset_index(drop=True)

    return df


def get_state_mean_indicator(indicator_name: str, sigla_uf: str):
    city_dimensions = dbrd.get_city_dimension_values()
    response = dbrd.get_datapoints_values(indicator_name)
    
    joined = pd.merge(city_dimensions,response,on='municipio_id',how='inner') # fazer o join
    df = joined[joined['sigla_uf'] == sigla_uf][['ano','valor']] # Filtrar os valores pelo estado
    df = df.groupby('ano').mean()

    return df

def get_region_mean_indicator(indicator_name: str, nome_regiao: str):
    city_dimensions = dbrd.get_city_dimension_values()
    response = dbrd.get_datapoints_values(indicator_name)
    
    joined = pd.merge(city_dimensions,response,on='municipio_id',how='inner') # fazer o join
    df = joined[joined['nome_regiao_nacional'] == nome_regiao][['ano','valor']] # Filtrar os valores pelo estado
    df = df.groupby('ano').mean()

    return df


def get_brazil_mean_indicator(indicator_name: str):
    response = dbrd.get_datapoints_values(indicator_name)[['ano','valor']]
    df = response.groupby('ano').mean()

    return df