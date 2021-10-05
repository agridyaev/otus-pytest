import pytest


@pytest.fixture
def data_1():
    """Return 1"""
    print('\nReturn 1')
    return 1


@pytest.fixture
def print_hello():
    """Print greetings"""
    print('\nHello')


def test_builtin_fixt(request, tmp_path):
    print(f'addopts: {request.config.getoption("verbose")}')
    print(f'unique tmp path: {tmp_path}')


def test_data_1(data_1, print_hello):
    assert data_1 == 1


def test_data_2(data_2):
    assert data_2 == 2


def test_data_3(data_3):
    assert data_3 == 3


def test_db(db_name):
    assert db_name == 'db_name'
