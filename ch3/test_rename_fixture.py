import pytest


@pytest.fixture()
def ultimate_answer_fixture():
    return 42


def test_everything(ultimate_answer_fixture):
    assert ultimate_answer_fixture == 42


@pytest.fixture(name='ultimate')
def ultimate_answer_fixture2():
    return 42


def test_everything2(ultimate):
    assert ultimate == 42
