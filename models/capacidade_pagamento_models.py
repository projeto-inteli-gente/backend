from pydantic import BaseModel

class CapagResponse(BaseModel):
    year: int
    capacidade_pagamento: float