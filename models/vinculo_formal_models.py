from pydantic import BaseModel

class VinculoFormalResponse(BaseModel):
    year: int
    porcentagem_vinculo_formal: float