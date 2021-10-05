import pytest

pytest_plugins = ['db_fixtures']


@pytest.fixture
def data_3():
    return 3
