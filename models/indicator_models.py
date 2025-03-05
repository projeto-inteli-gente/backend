from pydantic import BaseModel

class IndicatorResponse(BaseModel):
    year: int
    value: int | float | str | bool