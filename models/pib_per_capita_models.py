from pydantic import BaseModel

class PIBResponse(BaseModel):
    year: int
    pib_per_capita: float