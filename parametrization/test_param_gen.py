import pytest

from test_data.test_data import auth_endpoints


def id_val(val):
    return val[0]


@pytest.mark.parametrize("data", auth_endpoints, ids=id_val)
def test_with_generator(data):
    print(data)
