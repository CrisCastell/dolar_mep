from fastapi import APIRouter, HTTPException
from models import CompraBonoRequest, CompraBonoResponse, VentaBonoRequest, VentaBonoResponse
from repository import BonosRepository

router = APIRouter()

repo = BonosRepository()

@router.post("/compra/", response_model=CompraBonoResponse)
async def comprar_bonos(request: CompraBonoRequest):
    try:
        precio_bono = repo.obtener_precio_bono('AL30 - 24hs')
        nominales = repo.comprar(request.monto, precio_bono)

        return CompraBonoResponse(nominales_comprados=nominales)
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))



@router.post("/venta/", response_model=VentaBonoResponse)
async def vender_bonos(request: VentaBonoRequest):
    try:
        
        precio_bono_usd = repo.obtener_precio_bono('AL30D - 24hs')
        monto_usd = repo.vender(request.nominales, precio_bono_usd)

        return VentaBonoResponse(monto_obtenido=monto_usd)
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
