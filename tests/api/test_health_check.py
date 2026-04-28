import requests


def test_backend_health_check():
    response = requests.get("http://localhost:8000/api/v1/utils/health-check/")

    assert response.status_code == 200
    assert response.json() is True