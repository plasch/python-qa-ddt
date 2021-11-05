import pytest
import requests


# Example with single parameter
@pytest.mark.parametrize("param", [1, 2, 3, 4])
def test_one(param):
    assert param % 2 == 0


# Example with several parameters
@pytest.mark.parametrize("param1,param2", [
    (1, 2),
    (3, 4),
    (5, 6),
    (7, 8)
])
def test_two(param1, param2):
    assert (param1 + param2) % 3 == 0


# Example with nested parametrization
@pytest.mark.parametrize("param2", [1, 2, 3, 4, 5])
@pytest.mark.parametrize("param1", [6, 7, 8, 9, 0])
def test_three_nested(param1, param2):
    assert (param1 + param2) % 2 == 0


# Example with params ids
# Param filtering users posts by id
# https://jsonplaceholder.typicode.com/posts?userId=1
@pytest.mark.parametrize('userId', [-1, 0, 'a', 11, 9], ids=["negative", "zero", "letter", "out_of_range", "valid_value"])
def test_api_empty_response_on_user_id(userId, base_url):
    assert requests.get(base_url + "/posts", params={'userId': userId}).json() == []


@pytest.mark.parametrize("test_input, expected", [
                             ("3+5", 8),
                             ("2+4", 6),
                             pytest.param("6*9", 42, marks=pytest.mark.skip(reason="JIRA-12312"))
                         ])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize("param", [1, 2, 3], ids=["one", "two", "three"])
def test_with_fixture(param_fixture, param):
    assert (param_fixture + param) % 2 == 0
