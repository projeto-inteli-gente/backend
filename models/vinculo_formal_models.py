from pydantic import BaseModel

class VinculoFormalResponse(BaseModel):
    year: int
    vinculo_formal: float