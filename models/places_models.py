from pydantic import BaseModel

class PlaceName(BaseModel):
    id: int
    name: str

class Region(BaseModel):
    id: int
    name: str
    idh: float
    gini: float
    pib_per_capita: float
    porcentagem_vinculo_formal: float
    capag: float
    level: int

class State(BaseModel):
    id: int
    name: str
    region_id: int
    idh: float
    gini: float
    pib_per_capita: float
    porcentagem_vinculo_formal: float
    capag: float
    level: int

class City(BaseModel):
    id: int
    name: str
    state_id: int
    region_id: int
    idh: float
    gini: float
    pib_per_capita: float
    porcentagem_vinculo_formal: float
    capag: float
    level: int
