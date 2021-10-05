import os
import pytest


@pytest.fixture
def write_to_file(request):
    test_name = request.function.__name__
    with open(f'{test_name}', 'w') as f:
        f.write(test_name)
        path = os.path.abspath(f.name)
    return path


@pytest.fixture
def fixt_yield(write_to_file):
    path = write_to_file
    yield path
    os.remove(path)


@pytest.fixture
def fixt_fin(write_to_file, request):
    path = write_to_file
    def fin():
        os.remove(path)
    request.addfinalizer(fin)
    return path


def test_01(fixt_yield):
    with open(fixt_yield) as f:
        assert f.read() == 'test_01'


def test_02(fixt_fin):
    with open(fixt_fin) as f:
        assert f.read() == 'test_02'
