import pytest


@pytest.mark.regress
@pytest.mark.skip(reason="JIRA-123")
def test_example_one():
    assert 0


@pytest.mark.regress
@pytest.mark.xfail(strict=True)
def test_example_two():
    assert False


@pytest.mark.auth
def test_example_three():
    pass
