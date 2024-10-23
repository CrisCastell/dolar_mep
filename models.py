from pydantic import BaseModel

class CompraBonoRequest(BaseModel):
    monto: float

class CompraBonoResponse(BaseModel):
    nominales_comprados: int

class VentaBonoRequest(BaseModel):
    nominales: int

class VentaBonoResponse(BaseModel):
    monto_obtenido: float