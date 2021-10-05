import pytest

# $ pytest --fixtures-per-test
# $ pytest --setup-plan
# $ pytest --setup-show


@pytest.fixture(autouse=True)
def auto():
    print('\nAutouse fixture')


def test_01():
    print('test_01 started')


def test_02():
    print('test_02 started')
