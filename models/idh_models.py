from pydantic import BaseModel

class IDHResponse(BaseModel):
    year: int
    idh: float