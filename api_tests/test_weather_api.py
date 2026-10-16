import requests


BASE_URL = "https://api.open-meteo.com/v1/forecast"


def test_valid_weather_request():
    params = {
        "latitude": -1.286389,
        "longitude": 36.817223,
        "current": "temperature_2m"
    }

    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 200

def test_weather_response_contains_expected_fields():
    params = {
        "latitude": -1.286389,
        "longitude": 36.817223,
        "current": "temperature_2m"
    }

    response = requests.get(BASE_URL, params=params, timeout=10)

    assert response.status_code == 200

    data = response.json()

    assert "latitude" in data
    assert "longitude" in data
    assert "current" in data

    
def test_current_temperature_is_numeric():
    params = {
        "latitude": -1.286389,
        "longitude": 36.817223,
        "current": "temperature_2m"
    }

    response = requests.get(BASE_URL, params=params, timeout=10)

    assert response.status_code == 200

    data = response.json()

    temperature = data["current"]["temperature_2m"]

    assert isinstance(temperature, (int, float))

def test_hourly_temperature_data_matches_time_data():
    params = {
        "latitude": -1.286389,
        "longitude": 36.817223,
        "hourly": "temperature_2m"
    }

    response = requests.get(BASE_URL, params=params, timeout=10)

    assert response.status_code == 200

    data = response.json()

    times = data["hourly"]["time"]
    temperatures = data["hourly"]["temperature_2m"]

    assert len(times) == len(temperatures)

def test_invalid_latitude_returns_error():
    params = {
        "latitude": 91,
        "longitude": 36.817223,
        "current": "temperature_2m"
    }

    response = requests.get(BASE_URL, params=params, timeout=10)

    assert response.status_code == 400

    data = response.json()

    assert data["error"] is True

def test_invalid_longitude_returns_error():
    params = {
        "latitude": -1.286389,
        "longitude": 190,
        "current": "temperature_2m"
    }

    response = requests.get(BASE_URL, params=params, timeout=10)

    assert response.status_code == 400

    data = response.json()

    assert data["error"] is True

def test_non_numeric_latitude_returns_error():
    params = {
        "latitude": "queeen",
        "longitude": 36.817223,
        "current": "temperature_2m"
    }

    response = requests.get(BASE_URL, params=params, timeout=10)

    assert response.status_code == 400

    data = response.json()

    assert data["error"] is True

def test_missing_latitude_returns_error():
    params = {
        "longitude": 36.817223,
        "current": "temperature_2m"
    }

    response = requests.get(BASE_URL, params=params, timeout=10)

    assert response.status_code == 400

    data = response.json()

    assert data["error"] is True

def test_invalid_weather_variable_returns_error():
    params = {
        "latitude": -1.286389,
        "longitude": 36.817223,
        "hourly": "queen_temperature"
    }

    response = requests.get(BASE_URL, params=params, timeout=10)

    assert response.status_code == 400

    data = response.json()

    assert data["error"] is True

def test_boundary_latitude_90_is_accepted():
    params = {
        "latitude": 90,
        "longitude": 0,
        "current": "temperature_2m"
    }

    response = requests.get(BASE_URL, params=params, timeout=10)

    assert response.status_code == 200

def test_timezone_parameter_returns_timezone_information():
    params = {
        "latitude": -1.286389,
        "longitude": 36.817223,
        "current": "temperature_2m",
        "timezone": "auto"
    }

    response = requests.get(BASE_URL, params=params, timeout=10)

    assert response.status_code == 200

    data = response.json()

    assert "timezone" in data
    assert "timezone_abbreviation" in data