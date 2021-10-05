import pytest


@pytest.fixture(scope='function')
def func_scope():
    print('Function scope setup')
    yield
    print('Function scope teardown')


@pytest.fixture(scope='module')
def mod_scope():
    print('Module scope setup')
    yield
    print('Module scope teardown')


@pytest.fixture(scope='session')
def sess_scope():
    print('Session scope setup')
    yield
    print('Session scope teardown')


@pytest.fixture(scope='class')
def class_scope():
    print('Class scope setup')
    yield
    print('Class scope teardown')


def test_1(sess_scope, mod_scope, func_scope):
    print('Run test_1')


def test_2(sess_scope, mod_scope, func_scope):
    print('Run test_2')
