from pydantic import BaseModel

class GiniResponse(BaseModel):
    year: int
    gini: float