from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    # valid request main endpoint
    response = client.get("/api/v1/metrics/usd")
    assert response.status_code == 200

    for object in response.json():
        assert object['currency'] == 'USD'

    # invalid request main endpoint
    invalid_response = client.get("/api/v1/metrics/notCurrency")
    assert invalid_response.status_code == 400
    assert invalid_response.json() == {"detail": "notCurrency - is not currency"}


def test_read_graph():
    # valid request graph endpoint
    response = client.get(
        "/api/v1/metrics/graph/?time_frame=7&underlying_currency=USD"
        "&strategy_type=H&token_name=ETH&protocol=-&pool=-"
    )
    assert response.status_code == 200
    for object in response.json():
        assert 'dateOfRecord' in object.keys()
        assert 'trCum' in object.keys()

    # invalid request graph endpoint
    invalid_response = client.get("/api/v1/metrics/graph/")
    assert invalid_response.status_code == 400
    assert invalid_response.json() == {"detail": "data not found"}


def test_read_token_description():
    # valid request token description endpoint
    response = client.get(
        '/api/v1/description/token/WBTC'
    )
    assert response.status_code == 200
    assert 'tokenDescription' in response.json().keys()

    # invalid request token description endpoint
    invalid_response = client.get("/api/v1/description/token/NotTokenSymbol")
    assert invalid_response.status_code == 400
    assert invalid_response.json() == {"detail": "data not found"}


def test_read_protocol_descriptions():
    # valid request protocol descriptions endpoint
    response = client.get(
        '/api/v1/description/protocol/Aave'
    )
    assert response.status_code == 200
    assert 'protocolDescription' in response.json().keys()

    # invalid request protocol description endpoint
    invalid_response = client.get(
        "/api/v1/description/protocol/NotProtocolName"
    )
    assert invalid_response.status_code == 400
    assert invalid_response.json() == {"detail": "data not found"}
