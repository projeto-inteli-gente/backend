from pydantic import BaseModel

class Region(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class State(BaseModel):
    id: int
    name: str
    region: str

    class Config:
        orm_mode = True

class City(BaseModel):
    id: int
    name: str
    state: str
    region: str

    class Config:
        orm_mode = True
