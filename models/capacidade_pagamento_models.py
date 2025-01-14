from pydantic import BaseModel

class CapagResponse(BaseModel):
    year: int
    capag: float