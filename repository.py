import requests
import token_store
from fastapi import HTTPException

class BonosRepository:
    REMARKETS_URL = "https://api.remarkets.primary.com.ar/rest/instruments/detail"

    def obtener_precio_bono(self, codigo_bono: str) -> float:
        """
        Obtiene el precio actual del bono desde ReMarkets.
        """
        if token_store.auth_token is None:
            raise HTTPException(status_code=500, detail="Token de autenticación no disponible.")
        
        params = {'symbol': codigo_bono, 'marketId': 'ROFX'}
        headers = {'X-Auth-Token': f'{token_store.auth_token}'}
        response = requests.get(self.REMARKETS_URL, params=params, headers=headers)
        
        if response.status_code != 200:
            raise ValueError(f"No se pudo obtener el valor del bono {codigo_bono}. Error: {response.status_code}")

        data = response.json()


        # Obtener los límites de precio
        high_price = data.get("instrument", {}).get("highLimitPrice")
        low_price = data.get("instrument", {}).get("lowLimitPrice")

        if high_price is None or low_price is None:
            raise ValueError(f"No se encontraron límites de precio para el bono {codigo_bono}.")
        

        # Promediar entre highLimitPrice y lowLimitPrice como el precio del bono
        precio_bono = (high_price + low_price) / 2

        
        return precio_bono
    
    

    def comprar(self, monto: float, precio_bono: float) -> int:
        if monto < precio_bono:
            raise ValueError("El monto debe ser mayor al precio del bono.")
        return int(monto / precio_bono)
    


    def vender(self, nominales: int, precio_bono_usd: float) -> float:
        if nominales <= 0:
            raise ValueError("La cantidad de nominales debe ser mayor a 0.")
        return nominales * precio_bono_usd
