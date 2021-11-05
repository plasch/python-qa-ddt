import pytest


@pytest.mark.regress
@pytest.mark.auth
def test_example_one():
    pass


@pytest.mark.sec
def test_example_two():
    pass


@pytest.mark.regress
@pytest.mark.sec
def test_example_three():
    pass
