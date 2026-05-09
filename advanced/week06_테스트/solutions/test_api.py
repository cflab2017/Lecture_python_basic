import pytest
from unittest.mock import patch, MagicMock

def get_weather(city):
    import requests
    r = requests.get(f"https://api.example.com/weather?city={city}")
    if r.status_code == 200:
        return r.json()
    return None

def test_get_weather_success():
    with patch("requests.get") as m:
        m.return_value = MagicMock(
            status_code=200,
            json=MagicMock(return_value={"temp": 20}),
        )
        assert get_weather("seoul") == {"temp": 20}

def test_get_weather_not_found():
    with patch("requests.get") as m:
        m.return_value = MagicMock(status_code=404)
        assert get_weather("xxx") is None

def test_get_weather_network_error():
    with patch("requests.get", side_effect=ConnectionError("network down")):
        with pytest.raises(ConnectionError):
            get_weather("seoul")
