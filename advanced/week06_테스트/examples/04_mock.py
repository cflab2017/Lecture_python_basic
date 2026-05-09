from unittest.mock import patch, MagicMock

def get_weather(city):
    import requests
    return requests.get(f"https://api/{city}").json()

def test_get_weather():
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(
            json=MagicMock(return_value={"temp": 20})
        )
        assert get_weather("seoul") == {"temp": 20}
        mock_get.assert_called_once_with("https://api/seoul")
