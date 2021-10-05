import pytest
import sys
import time


@pytest.mark.skip(reason='Skipped test example')
def test_skip():
    pass


@pytest.mark.skipif(sys.version_info > (3, 5), reason="requires python3.5 or lower")
def test_skip_if():
    pass


@pytest.mark.xfail(reason='Wrong comparison', strict=True)
def test_fail_comparison():
    assert 1 == 0


@pytest.mark.xfail(raises=(AssertionError, TimeoutError))
def test_fail_exception():
    raise AssertionError


@pytest.mark.slow
def test_custom_mark():
    time.sleep(3)
    assert 1 == 1
