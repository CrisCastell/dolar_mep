from fastapi import FastAPI
from routers import bonos
from utils import obtener_token_remarkets
import token_store
app = FastAPI()

@app.on_event("startup")
async def startup_event():
    token_store.auth_token = obtener_token_remarkets()


# Incluir las rutas de bonos
app.include_router(bonos.router)
