from pydantic import BaseModel

class RegionResponse(BaseModel):
    name: str

class StateResponse(BaseModel):
    nome_uf: str
    sigla_uf: str

class CityResponse(BaseModel):
    nome_municipio: str
    municipio_id: int