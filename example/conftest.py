import pytest
import csv


@pytest.fixture(scope="session")
def base_url():
    return "https://my-api-examaple.herokuapp.com/api"


def pytest_generate_tests(metafunc):
    if "auth_availability" in metafunc.fixturenames:
        with open("test_data/auth_endpoints.csv") as file:
            reader = csv.reader(file)
            header = next(reader)
            metafunc.parametrize("auth_availability", reader)
