from unittest.mock import patch
from repository import BonosRepository
import pytest

repo = BonosRepository()

# Mock de una respuesta de ReMarkets para un bono específico
mock_response = {
    "status": "OK",
    "instrument": {
        "highLimitPrice": 2000.00,
        "lowLimitPrice": 1000.00,
    }
}

@patch('repository.requests.get')
def test_obtener_precio_bono(mock_get):
    # Configuracion del mock
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    precio_bono = repo.obtener_precio_bono('AL30')
    assert precio_bono == 1500  # Promedio esperado entre highLimitPrice y lowLimitPrice

def test_comprar_bono():
    precio_bono = 1500
    monto = 1500.00
    nominales = repo.comprar(monto, precio_bono)
    assert nominales == 1  # Puede comprar 1 nominales

def test_comprar_bono_monto_insuficiente():
    precio_bono = 1500
    monto = 500.00
    with pytest.raises(ValueError, match="El monto debe ser mayor al precio del bono."):
        repo.comprar(monto, precio_bono)

def test_vender_bono():
    precio_bono_usd = 0.6167
    nominales = 2
    monto_usd = repo.vender(nominales, precio_bono_usd)
    assert monto_usd == pytest.approx(1.2334)  # Monto en USD

def test_vender_bono_nominales_invalidos():
    precio_bono_usd = 0.6167
    with pytest.raises(ValueError, match="La cantidad de nominales debe ser mayor a 0."):
        repo.vender(0, precio_bono_usd)
