import requests


def test_methods_availability(base_url, auth_availability):
    endpoint, method, expected_status, description = auth_availability
    response = requests.request(method, f"{base_url}/auth/{endpoint}")

    assert response.status_code == int(expected_status), \
        f"Wrong status code on auth {endpoint} url for {method} method"

    assert response.json().get("description") == description
