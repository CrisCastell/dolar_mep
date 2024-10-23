import requests
from datetime import datetime
from fastapi import HTTPException
from dotenv import load_dotenv
import os

load_dotenv()

def obtener_token_remarkets():

    try:

        login_headers = {
            'X-Username' : os.getenv('REMARKETS_USERNAME'),
            'X-Password' : os.getenv('REMARKETS_PASSWORD')
        }
        response = requests.post("https://api.remarkets.primary.com.ar/auth/getToken", headers=login_headers)
        
        if response.status_code == 200:
            auth_token = response.headers.get('X-Auth-Token')
            return auth_token
        else:
            raise HTTPException(status_code=400, detail=f"No se pudo obtener el token.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error durante la solicitud al obtener el token de ReMarkets: {e}")
