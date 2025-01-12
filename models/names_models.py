from pydantic import BaseModel

class NameResponse(BaseModel):
    id: int
    name: str