from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app
import pytest


client = TestClient(app)

# Mock de una respuesta de ReMarkets
mock_response = {
    "status": "OK",
    "instrument": {
        "highLimitPrice": 750.00,
        "lowLimitPrice": 700.00,
    }
}

@patch('repository.requests.get')
def test_compra_bonos(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    response = client.post("/compra/", json={"monto": 1500.00})
    assert response.status_code == 200
    assert response.json() == {"nominales_comprados": 2}


@patch('repository.requests.get')
def test_compra_bonos_monto_insuficiente(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    response = client.post("/compra/", json={"monto": 500.00})
    assert response.status_code == 400
    assert response.json() == {"detail": "El monto debe ser mayor al precio del bono."}


@patch('repository.requests.get')
def test_venta_bonos(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    response = client.post("/venta/", json={"nominales": 2})
    assert response.status_code == 200
    assert response.json() == {"monto_obtenido": pytest.approx(1450)}


@patch('repository.requests.get')
def test_venta_bonos_nominales_invalidos(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    response = client.post("/venta/", json={"nominales": 0})
    assert response.status_code == 400
    assert response.json() == {"detail": "La cantidad de nominales debe ser mayor a 0."}
